//alert("hola mundo 1")

function saludar(){
    alert("hola mundo 3")
}

function colorear(){
   // console.log("Si")
  var h1 =  document.getElementById("saludo")

  h1.innerHTML = "Javascript!"

  h1.classList.add("fondo")

}

function abrir(){
  var ojo =  document.getElementById("imgOjo")
  ojo.src='img/ojo1.png'

}


function cerrar(){
  var ojo =  document.getElementById("imgOjo")
  ojo.src='img/ojo2.png'


}