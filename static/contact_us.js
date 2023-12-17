// This function validates the contact form and submits it if it is valid.
function validateForm() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;

  if (name == "") {
    alert("Please enter your name.");
    return false;
  }

  if (email == "") {
    alert("Please enter your email address.");
    return false;
  }

  if (!validateEmail(email)) {
    alert("Please enter a valid email address.");
    return false;
  }

  if (message == "") {
    alert("Please enter your message.");
    return false;
  }

  document.getElementById("form").submit();
}

// This function validates an email address.
function validateEmail(email) {
  var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return re.test(email);
}
