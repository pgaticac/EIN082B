function saludar(){
   // alert("HOLA!")
   var miH1 = document.getElementById("miH1")
   //var cajaDeTexto = document.getElementById("txtNombre")
   var nombre = document.getElementById("txtNombre").value
   miH1.className = "saludo"
   miH1.innerHTML = "Hola " + nombre
}