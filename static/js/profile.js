function change(event) {
  event.preventDefault()
  var username = document.getElementById('username').value;
  var email = document.getElementById('email').value;
  var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  if (username.trim() == '' || email.trim() === '') {
    Swal.fire({
        title: "ناموفق",
        text: 'یوزرنیم یا ایمیل معتبر نیست',
        icon: "error"
      });
      return;
  }

  if (username.length < 6 || username.length > 20) {
    Swal.fire({
      title: "ناموفق",
      text: "یوزرنیم باید بین 6 تا 20 کاراکتر باشد",
      icon: "error"
    })
    return;
  }

  if (email.length < 15 || email.length > 40) {
    Swal.fire({
      title: "ناموفق",
      text: "ایمیل باید بین 15 تا 40 کاراکتر باشد",
      icon: "error"
    })
    return;
  }




  fetch('/profile/profile-edit/', {
    method: 'POST',
    headers: {"Content-Type":"application/x-www-form-urlencoded", "X-CSRFToken":csrftoken},
    body: "username=" + encodeURIComponent(username) + "&email=" + encodeURIComponent(email)
  })
  .then(response => response.json())
  .then(data => {
    Swal.fire({
        title: "موفق",
        html: data.message.email + "<br>" + data.message.username,
        icon: "success"
      });
    })
  .catch(err => {
    Swal.fire({
      title: "Error",
      text: err.message.username,
      icon: 'error'
    })
  })
    
  
}