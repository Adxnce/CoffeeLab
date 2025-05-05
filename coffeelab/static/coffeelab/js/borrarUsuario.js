$(document).ready(function () {


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

    // Manejo del formulario
    $(document).on('click', '.btn-eliminar', function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional

        const username = $(this).data('id'); // Obtiene el ID del usuario a eliminar
        $.ajax({
            url: '/api/datos_usuarios/' + username,
            type: 'DELETE',
            contentType: 'application/json',
            success: function (response) {
                console.log("Usuario eliminado correctamente:", response);
                alert("Usuario eliminado correctamente.");
                location.reload(); // Recarga la página para actualizar la lista de usuarios
            },
            error: function (xhr, status, error) {
                console.error("Error al eliminar el usuario:", error);
                alert("Error al eliminar el usuario. Por favor, inténtelo de nuevo.");
            }
        });
    });
});
