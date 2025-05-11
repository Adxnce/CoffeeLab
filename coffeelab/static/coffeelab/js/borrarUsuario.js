$(document).ready(function () {

    const token = localStorage.getItem('token');

    // Manejo del formulario
    $(document).on('click', '.btn-eliminar', function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional
        const username = $(this).data('id'); // Obtiene el ID del usuario a eliminar
        $.ajax({
            url: '/api/datos_usuarios/' + username,
            type: 'DELETE',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
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
