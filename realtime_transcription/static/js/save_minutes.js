// static/js/save_minutes.js
document.addEventListener("DOMContentLoaded", () => {
  const saveBtn = document.getElementById("saveBtn");
  const modal = document.getElementById("saveModal");
  const modalText = document.getElementById("modalText");
  const cancelModal = document.getElementById("cancelModal");
  const confirmSave = document.getElementById("confirmSave");
  const transcriptionBox = document.getElementById("transcriptionBox");
  const root = document.getElementById("transcriptionRoot");
  const meetingId = root.dataset.meetingId;

  saveBtn.addEventListener("click", () => {
    modalText.value = transcriptionBox.innerText;
    modal.classList.remove("hidden");
  });

  cancelModal.addEventListener("click", () => {
    modal.classList.add("hidden");
  });

  confirmSave.addEventListener("click", () => {
    fetch("/realtime/save-minutes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCsrfToken(), // Django用のCSRFトークン
      },
      body: JSON.stringify({
        meeting_id: meetingId,
        data: modalText.value,
      }),
    }).then((res) => {
      if (res.ok) {
        alert("保存されました！");
        modal.classList.add("hidden");
      } else {
        alert("保存に失敗しました");
      }
    });
  });

  function getCsrfToken() {
    return document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];
  }
});
