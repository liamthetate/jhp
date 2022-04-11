
function sendMail(contactForm) {
  emailjs.send("service_jhp", "template_jhp", {
      "from_name": contactForm.name.value,
      "from_email": contactForm.emailaddress.value,
      "subject": contactForm.subject.value,
      "message": contactForm.message.value,
  })
  .then(
      alert("Message sent!"),
      document.getElementById("submit-btn").disabled = true,
      document.getElementById('contact-form').reset(),
      document.getElementById("submit-btn").value = "Message sent!",
  )
  return false
}