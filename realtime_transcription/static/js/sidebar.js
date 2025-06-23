document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const openBtn = document.getElementById("openSidebarBtn");
  let isDragging = false;
  let dragStarted = false;
  let offsetX, offsetY;

  // ✅ トグル処理（位置も動的に調整）
  window.toggleSidebar = function () {
    if (isDragging) return; // ← ドラッグ中ならキャンセル

    if (sidebar.style.display === "none" || sidebar.style.display === "") {
      // トグルボタンの位置を取得
      const btnRect = openBtn.getBoundingClientRect();
      sidebar.style.left = `${btnRect.left}px`;
      sidebar.style.top = `${btnRect.top}px`;
      sidebar.style.transform = "none";  // 中央固定解除
      sidebar.style.display = "block";
      openBtn.style.display = "none";
    } else {
      sidebar.style.display = "none";
      openBtn.style.display = "block";
    }
  };

  // ✅ ドラッグ処理
  openBtn.addEventListener("mousedown", function (e) {
    isDragging = false;
    dragStarted = true;
    offsetX = e.clientX - openBtn.getBoundingClientRect().left;
    offsetY = e.clientY - openBtn.getBoundingClientRect().top;
  });

  document.addEventListener("mousemove", function (e) {
    if (dragStarted) {
      isDragging = true;
      openBtn.style.left = `${e.clientX - offsetX}px`;
      openBtn.style.top = `${e.clientY - offsetY}px`;
    }
  });

  document.addEventListener("mouseup", function () {
    // クリック判定：短距離＆短時間で mouseup → click 扱い
    if (dragStarted && !isDragging) {
      toggleSidebar();  // ← ここでのみトグル呼ぶ
    }
    dragStarted = false;
    isDragging = false;
  });
});
