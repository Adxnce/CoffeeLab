$(document).ready(function() {

    const token = localStorage.getItem('token');
    const rol = localStorage.getItem('rol');
    const username = localStorage.getItem('username');

    
    $('#enviar').on('click', function() {

        const confirmPassword = $('#id_confirmPassword').val();
        const formData = {
            username: $('#id_username').val(),
            email: $('#id_email').val(),
            password: $('#id_password').val(),
            direccion: $('#id_direccion').val(),
            ciudad: $('#id_ciudad').val(),
            rol: rol,
        }
        if (formData.password == confirmPassword){
            $.ajax({
                url: '/api/datos_usuarios/' + username ,
                type: 'PUT',
                headers: {'Authorization': 'Token ' + token},
                contentType: 'application/json',
                data: JSON.stringify(formData),
                success: function(response) {

                    localStorage.setItem('username', formData.username);

                    console.log("Datos del perfil actualizados: ", response);
                    alert("Datos del perfil actualizados correctamente.");
                    $('#userForm')[0].reset(); 
                    location.reload();
                },
                error: function(xhr, status, error) {
                    console.error("Error al obtener los datos del perfil:", error);
                    alert("Error al obtener los datos del perfil. Por favor, inténtelo de nuevo.");
                }
            });
        }else{
            alert("Las contraseñas no coinciden. Por favor, verifícalas.");
        };
        console.log("Datos enviados: ", formData);
    });
});