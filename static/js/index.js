document.addEventListener("DOMContentLoaded", function() {
    // Obtener una referencia a los elementos del formulario
    const formulario = document.getElementById("formulario");
    const capitalInput = document.getElementById("capital");
    const tasaInteresInput = document.getElementById("tasa_interes");
    const tiempoInput = document.getElementById("tiempo");
  
    // Obtener una referencia a los elementos del resultado
    const resultadoElement = document.getElementById("resultado");
    const interesesElement = document.getElementById("intereses");
    const tasaMensualElement = document.getElementById("tasa_mensual");
  
    // Agregar un evento al botón "Limpiar"
    const btnLimpiar = document.getElementById("btn-limpiar");
    btnLimpiar.addEventListener("click", function(event) {
      event.preventDefault();
      capitalInput.value = "";
      tasaInteresInput.value = "";
      tiempoInput.value = "";
  
      resultadoElement.textContent = "";
      interesesElement.textContent = "";
      tasaMensualElement.textContent = "";
    });
  });
  