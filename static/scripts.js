// scripts.js

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');

  form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form from submitting the default way

      const title = document.querySelector('#title').value;
      const description = document.querySelector('#description').value;

      if (title && description) {
          fetch('/add_course', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded'
              },
              body: new URLSearchParams({
                  title: title,
                  description: description
              })
          })
          .then(response => response.json())
          .then(data => {
              alert(data.message);
              form.reset(); // Reset form fields
          })
          .catch(error => {
              console.error('Error:', error);
          });
      } else {
          alert('Please fill in all fields.');
      }
  });
});
