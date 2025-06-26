window.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("downloadBtn");

  if (!btn) return;

  btn.addEventListener("click", () => {
    const text = document.getElementById("transcriptionBox").innerText;

    const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "transcription.txt";
    link.click();
    URL.revokeObjectURL(link.href);
  });
});
