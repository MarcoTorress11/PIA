// Inicializa EmailJS
(function(){
    emailjs.init("FLQ7IJgInhGy96MK5"); // Mi User ID de EmailJS
})();

document.getElementById('formContacto').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log("Paso1"); // Checkpoint 1

    // Obtener los datos de HTML
    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const duda = document.getElementById('duda').value;
    const fecha = document.getElementById('fecha').value;
    const informacion = document.getElementById('informacion').checked ? "Si" : "No";

    // Guardar en la base de datos Django
    fetch('/guardar_respuesta/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: new URLSearchParams({
            nombre: nombre,
            correo: correo,
            duda: duda,
            fecha: fecha,
            informacion: informacion
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Envía el correo con EmailJS
            emailjs.send("service_y8s7yat", "template_t01izmt", {
                nombre: nombre,
                correo: correo,
                duda: duda,
                fecha: fecha,
                informacion: informacion
            })
            .then(function(response) {
                alert('Formulario guardado y correo enviado exitosamente!');
            }, function(error) {
                alert('Error al enviar el correo: ' + JSON.stringify(error));
            });
        } else {
            alert('Error al guardar la respuesta en la base de datos.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al procesar el formulario.');
    });
});