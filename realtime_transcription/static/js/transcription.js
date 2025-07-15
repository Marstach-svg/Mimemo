window.addEventListener("DOMContentLoaded", () => {
  const transcriptionBox = document.getElementById("transcriptionBox");
  if (!transcriptionBox) return; 
  const root = document.getElementById("transcriptionRoot");
  if (!root) return; 
  const meetingId = root.dataset.meetingId;

  const micBtn = document.querySelector("button[title='文字起こし開始']");
  const stopBtn = document.querySelector("button[title='録音停止']");
  const downloadBtn = document.getElementById("downloadBtn");
  const minutesBtn = document.querySelector("button[title='要約を生成']");

  // Web Speech API の準備
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'ja-JP';
  recognition.continuous = true;
  recognition.interimResults = true;

  function getCsrfToken() {
    return document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];
  }

  micBtn.addEventListener("click", () => {
    // 録音開始前に末尾に改行を入れておく
    if (!transcriptionBox.value.endsWith('\n') && transcriptionBox.value.trim() !== '') {
      transcriptionBox.value += '\n';
    }

    recognition.start();
  });

  stopBtn.addEventListener("click", () => {
    recognition.stop();

    const text = transcriptionBox.value;
    fetch("/realtime/save-minutes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken(),
      },
      body: JSON.stringify({
        meeting_id: meetingId,
        data: text,
      }),
    })
  });

  let seen = new Set();  // 表示済みの result を保存

  recognition.onresult = (event) => {
    for (let i = event.resultIndex; i < event.results.length; ++i) {
      const result = event.results[i];
      const transcript = result[0].transcript.trim();

      // isFinalなものだけを対象にする（中間認識は無視）
      if (result.isFinal) {
        // resultIndex + transcript のペアで重複検出（Setで記録）
        const key = `${i}:${transcript}`;
        if (!seen.has(key)) {
          transcriptionBox.value += transcript + '\n';
          seen.add(key);
        }
      }
    }
  };

  // ダウンロード処理
  downloadBtn.addEventListener("click", () => {
    const text = transcriptionBox.value;
    const blob = new Blob([text], { type: 'text/plain' });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "transcription.txt";
    link.click();
    URL.revokeObjectURL(link.href);
  });

  // 議事録作成処理
  minutesBtn.addEventListener("click", async () => {
    const text = transcriptionBox.value;
    
    if (!text.trim()) {
      alert("文字起こしテキストが空です。");
      return;
    }

    // ボタンを無効にしてローディング表示
    minutesBtn.disabled = true;
    minutesBtn.textContent = "作成中...";

    try {
      const response = await fetch("/realtime/create-minutes/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCsrfToken(),
        },
        body: JSON.stringify({
          meeting_id: meetingId,
          transcript: text,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      if (result.success) {
        // 議事録をダウンロード
        const blob = new Blob([result.minutes], { type: 'text/plain' });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = `minutes_${new Date().toISOString().slice(0, 10)}.txt`;
        link.click();
        URL.revokeObjectURL(link.href);
      } else {
        alert("議事録の作成に失敗しました: " + result.error);
      }
    } catch (error) {
      console.error("Error creating minutes:", error);
      alert("議事録の作成中にエラーが発生しました。");
    } finally {
      // ボタンを元に戻す
      minutesBtn.disabled = false;
      minutesBtn.textContent = "議事録作成";
    }
  });
});
