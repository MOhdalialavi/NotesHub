function toggleSubParts(classId) {
    var subParts = document.getElementsByClassName(classId);
    for (var i = 0; i < subParts.length; i++) {
      subParts[i].classList.toggle("active");
    }
  }
// Add this script at the end of your HTML body or in an external JS file
document.addEventListener('DOMContentLoaded', () => {
  const passwordToggle = document.querySelector('.password-toggle');
  const leftEye = document.querySelector('.left-eye');
  const rightEye = document.querySelector('.right-eye');
  const passwordField = document.querySelector('input[name="password"]');

  passwordToggle.addEventListener('click', () => {
      if (passwordField.type === 'password') {
          passwordField.type = 'text';
          leftEye.style.transform = 'scale(1, 0.1)';
          rightEye.style.transform = 'scale(1, 0.1)';
      } else {
          passwordField.type = 'password';
          leftEye.style.transform = 'scale(1)';
          rightEye.style.transform = 'scale(1)';
      }
  });
});
