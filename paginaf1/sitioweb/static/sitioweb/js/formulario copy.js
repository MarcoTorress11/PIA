// Inicializa EmailJS
(function(){
    emailjs.init("FLQ7IJgInhGy96MK5"); // Mi User ID de EmailJS
})();

// Manejar el envío del formulario
document.getElementById('formContacto').addEventListener('submit', function(event) {
    event.preventDefault(); 
    console.log("Paso1"); // Checkpoint 1

    // Obtener los datos de HTML
    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const duda = document.getElementById('duda').value;
    const fecha = document.getElementById('fecha').value;
    const informacion = document.getElementById('informacion').checked ? "Sí" : "No";
    console.log("Paso2"); // Checkpoint 2

    // Configurar los campos del correo
    emailjs.send("service_y8s7yat", "template_t01izmt", {
        nombre: nombre,
        correo: correo,
        duda: duda,
        fecha: fecha,
        informacion: informacion
    })
    .then(function(response) {
       alert('Correo enviado exitosamente!');
    }, function(error) {
       alert('Error al enviar el correo: ' + JSON.stringify(error));
    });
    console.log("Paso3"); // Checkpoint 3 (Finalizado)
});