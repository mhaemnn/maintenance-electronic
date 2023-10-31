document.addEventListener("DOMContentLoaded", function () {
  var errorList = document.querySelector(".errorlist");

  if (errorList) {
    var errorMessages = errorList.querySelectorAll("li");

    errorMessages.forEach(function (message) {
      message.textContent = message.textContent.replace(".", "");
    });
  }
});
