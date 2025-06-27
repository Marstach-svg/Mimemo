window.addEventListener("DOMContentLoaded", () => {
  const transcriptionBox = document.getElementById("transcriptionBox");
  if (!transcriptionBox) return; 

  const micBtn = document.querySelector("button[title='文字起こし開始']");
  const stopBtn = document.querySelector("button[title='録音停止']");
  const downloadBtn = document.getElementById("downloadBtn");

  // Web Speech API の準備
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'ja-JP';
  recognition.continuous = true;
  recognition.interimResults = true;

  micBtn.addEventListener("click", () => recognition.start());
  stopBtn.addEventListener("click", () => recognition.stop());

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
          document.getElementById("transcriptionBox").innerText += transcript + '\n';
          seen.add(key);
        }
      }
    }
  };

  // ダウンロード処理
  downloadBtn.addEventListener("click", () => {
    const text = transcriptionBox.innerText;
    const blob = new Blob([text], { type: 'text/plain' });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "transcription.txt";
    link.click();
    URL.revokeObjectURL(link.href);
  });
});
