var cont=0
function cambia() {
cont++;
switch(cont%4+1)
 {
 case 1:
 document.getElementById("fotocambia").src="img/eye2.png";
 break;
 case 2:
 document.getElementById("fotocambia").src="img/eye3.png";
 break;
 }

}
function inicio() {
setInterval(cambia, 1000);
}
window.onload=inicio;

function saludar(){
    alert("holiis")
}

function colorear(){
   // console.log("si")
   var h1 = document.getElementById("saludo")
   h1.innerHTML = "JavaScript"
   h1.classList.add("fondo")

}