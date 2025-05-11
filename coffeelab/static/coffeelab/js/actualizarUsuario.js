$(document).ready(function() {

    // Recuperar el token de localStorage
    const token = localStorage.getItem('token');
    
    var preUsername = $('#id_username').val();
    // Manejo del formulario
    $('#userForm').submit(function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional



        const formData = {
            username: $('#id_username').val(),
            email: $('#id_email').val(),
            password: $('#id_password').val(),
            direccion: $('#id_direccion').val(),
            ciudad: $('#id_ciudad').val(),
            rol: $('#id_rol').val(),
        };

        $.ajax({
            url: '/api/datos_usuarios/' + preUsername  ,
            type: 'PUT',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
            data: JSON.stringify(formData),
            success: function (response) {
                localStorage.setItem('username', formData.username);
                localStorage.setItem('rol', formData.rol);
                localStorage.setItem('token', response.token);

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
