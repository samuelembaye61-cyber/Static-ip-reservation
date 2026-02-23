

document.addEventListener("DOMContentLoaded", function () {

  const modal = document.getElementById("confirmModal");
  const confirmYes = document.getElementById("confirmYes");
  const confirmNo = document.getElementById("confirmNo");
  const modalMessage = document.getElementById("modalMessage");

  let formToSubmit = null;

  document.querySelectorAll(".action-btn").forEach(button => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      formToSubmit = this.closest("form");

      if (this.dataset.action === "reserve") {
        modalMessage.textContent = "Are you sure you want to reserve this IP address?";
      } else {
        modalMessage.textContent = "Are you sure you want to release this IP address?";
      }

      modal.style.display = "flex";
    });
  });

  confirmYes.addEventListener("click", function () {
    if (formToSubmit) formToSubmit.submit();
  });

  confirmNo.addEventListener("click", function () {
    modal.style.display = "none";
  });

  window.addEventListener("click", function (e) {
    if (e.target === modal) {
      modal.style.display = "none";
    }
  });

});