// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
  // Check if there are messages to display
  var messages = document.getElementsByClassName('messages')[0];

  if (messages) {
    // Loop through each message and display it using SweetAlert2
    messages.querySelectorAll('.message').forEach(function(message) {
      console.log(message)
      var messageText = message.textContent;
      var messageType = message.dataset.messageType || 'info'; // Default to 'info' if no type is specified
      var messageTitulo = 'exito!'

      Swal.fire({
        'title': messageTitulo.charAt(0).toUpperCase() + messageTitulo.slice(1), // Capitalize the first letter
        'text': messageText,
        'icon': messageType,
        showConfirmButton: false,
        timer: 2000,  // Adjust the timer as needed
        'confirmButtonText': 'Entendido'
      });
    });
  }
});

