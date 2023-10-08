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

const marquee = document.getElementById('alert-text');
const link = document.getElementById('alert-link');

// Add a class to stop the marquee animation when hovered
link.addEventListener('mouseover', () => {
    marquee.classList.add('stop-marquee');
});

// Remove the class to resume the marquee animation when not hovered
link.addEventListener('mouseout', () => {
    marquee.classList.remove('stop-marquee');
});

//feedback form
document.getElementById("feedback-form").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get user input
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var feedback = document.getElementById("feedback").value;

  // Construct email content
  var subject = "New Feedback from " + name;
  var body = "Name: " + name + "\nEmail: " + email + "\nFeedback: " + feedback;

  // Open user's default email client
  window.open("mailto:mohdalilavi786@gmail.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body));
});
