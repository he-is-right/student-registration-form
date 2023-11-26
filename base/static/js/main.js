// Get the form element
const form = document.querySelector('form');

// Add an event listener for the form submit event
form.addEventListener('submit', function(event) {
  // Prevent the default form submission
  event.preventDefault();

  // Validate the form data
  const name = form.querySelector('input[name="name"]').value;
  const email = form.querySelector('input[name="email"]').value;

  // Check if the name field is empty
  if (name === '') {
    

    // Focus the name input field
    form.querySelector('input[name="name"]').focus();

    // Return to prevent the form from submitting
    return;
  }

  // Check if the email field is empty
  if (email === '') {
    // Display an error message
    alert('Please enter your email address');

    // Focus the email input field
    form.querySelector('input[name="email"]').focus();

    // Return to prevent the form from submitting
    return;
  }

  // Validate the email address
  const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if (!emailRegex.test(email)) {
    // Display an error message
    alert('Please enter a valid email address');

    // Focus the email input field
    form.querySelector('input[name="email"]').focus();

    // Return to prevent the form from submitting
    return;
  }

  // Submit the form
  form.submit();
});
