$(document).ready(function() {

    // Función para obtener el CSRF token de las cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Verifica si esta cookie es la que buscamos
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Configura jQuery para incluir el CSRF token en cada solicitud AJAX
    const csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        headers: { 'X-CSRFToken': csrftoken }
    });

    var preUsername = $('#id_username').val();
    // Manejo del formulario
    $('#userForm').submit(function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional


        console.log(preUsername)
        const formData = {
            username: $('#id_username').val(),
            email: $('#id_email').val(),
            password: $('#id_password').val(),
            direccion: $('#id_direccion').val(),
            ciudad: $('#id_ciudad').val()
        };

        $.ajax({
            url: '/api/datos_usuarios/' + preUsername  ,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function (response) {
                console.log("Usuario actualizado correctamente:", response);
                alert("Usuario actualizado correctamente.");
                window.location.href = '/adminPanel/'; // Redirige a la página del panel de administración
            },
            error: function (xhr, status, error) {
                console.error("Error al actualizar el usuario:", error);
                alert("Error al actualizar el usuario. Por favor, inténtelo de nuevo.");
            }
        });
    });
});