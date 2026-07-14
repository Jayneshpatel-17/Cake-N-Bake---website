const user_con = document.querySelector('.user-container');
const regis_btn = document.querySelector('.registration-btn');
const login_btn = document.querySelector('.login-btn');

regis_btn.addEventListener('click', () => {
    user_con.classList.remove('login-section--display')
})

login_btn.addEventListener('click', () => {
    user_con.classList.add('login-section--display')
})

function myfunction() {
        // onlyalphabets()
        // validateform()
        // number()
        if(onlyalphabets() == true && validateform() == true && number() == true && validatePassword() == true && confirmPassword() == true)
        {
            alert("you are enter data successfully!!");
            return true;
        }
        else{
            return false;
        }
}
function onlyalphabets() {
    var regex = /^[a-zA-Z /s]*$/;
    if (regex.test(document.myform.username.value)) {
        return true;
    }
    else {
        alert("Enter alphabets only");
        return false;
    }
}
function validateform() {
    var x = document.forms["myform"]["email"].value;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".");
    if (atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= x.length) {
        alert("Not a valid e-mail address");
        return false;
    }
    else
        return true;
}
function number() {
    var regex = /^[a-zA-Z]*$/;
    var v = document.getElementById("contact").value;
    var w = v.lastIndexOf("");
    if (regex.test(document.myform.contact.value)) {
        alert("Not a valid Mobile No.");
        return false;
    }
    else if (w <= 9 || w > 10) {
        alert("Not a valid Mobile No.");
        return false;
    }
    else
        return true;
}
function validatePassword() {
    // Define the criteria for a valid password
    var Password = document.getElementById("password").value;
    const minLength = 8;
    const hasUpperCase = /[A-Z]/;
    const hasLowerCase = /[a-z]/;
    const hasNumbers = /[0-9]/;
    const hasSpecialChars = /[\W_]/;
  
    if (Password.length < minLength || !hasUpperCase.test(Password) || !hasLowerCase.test(Password) || !hasNumbers.test(Password) || !hasSpecialChars.test(Password)) {
      alert("Password must be at least 8 characters long, one uppercase , one lowercase , one digit , one special character.");
      return false;
    }

    return true;
}

function confirmPassword(){
    var Password = document.getElementById("password").value;
    var Cpassword = document.getElementById("cpassword").value;

    if(Password == Cpassword){
        return true;
    }
    else
        alert("Confirm password is incorrect!");
        return false;
}

