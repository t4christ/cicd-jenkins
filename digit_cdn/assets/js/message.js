// Take Off Popup Messages

function removePopup(){
setTimeout(() => {
const box = document.getElementById('message-info');
// const success = document.querySelector(".success-wrapper")
// const error = document.querySelector(".error-wrapper")
// const cancel = document.querySelector(".cancel-wrapper")

// const errorText = document.getElementsByClassName('errorlist').length > 0
// if (errorText){
//  const errorBoxes = Array.from(document.getElementsByClassName('errorlist'))
//  errorBoxes.forEach(box => {
//   box.classList.add("errorText");
//   box.style.display = 'none';
// });
//   document.querySelector('form .errorlist').style.display = 'none';
// }


// 👇️ removes element from DOM
box.style.display = 'none';
// success.style.display = 'none';
// error.style.display = 'none';
// cancel.style.display = 'none';
}, 9000)};


if(window.addEventListener) {
    window.addEventListener('load',removePopup,false); //W3C
} else {
    window.attachEvent('onload',removePopup); //IE
}