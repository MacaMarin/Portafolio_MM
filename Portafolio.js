// PORAFOLIO MACARENA MARIN

$(document).ready(function(){

  // Mostrar un mensaje al enviar el formulario
  $("#formConsulta").submit(function(e){
    $("#alerta").removeClass("d-none");  // Muestra el mensaje
    $(this)[0].reset();             // Limpia los campos
  });

});
