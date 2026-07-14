function myfunction(){
    // onlyalphabets()
    // validateform()
    // number()
    if(onlyalphabets() == true  && number() == true)
    {
        return true;
    }
    else{
        return false;
    }
}
function onlyalphabets(){
var regex = /^[a-zA-Z /s]*$/;
if (regex.test(document.myform.name.value)) {
    return true;
}
else {
    alert("Enter alphabets only");
    return false;
}
}

function number(){
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
