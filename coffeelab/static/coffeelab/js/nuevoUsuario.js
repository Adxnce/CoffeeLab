$(document).ready(function () {


    // Manejo del formulario
    $('#userForm').submit(function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional

        const confirmPassword = $('#id_confirmPassword').val();
        const formData = {
            username: $('#id_username').val(),
            email: $('#id_email').val(),
            password: $('#id_password').val(),
            direccion: $('#id_direccion').val(),
            ciudad: $('#id_ciudad').val(),
            rol: $('#id_rol').val(),
        };
        console.log("contraseña: ", formData.password);
        console.log("confirmar contraseña :", confirmPassword);
        
        // Validación de contraseñas
        if (formData.password == confirmPassword){
            $.ajax({
                url: '/api/lista_usuarios/',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(formData),
                success: function (response) {
                    console.log("Usuario agregado correctamente:", response);
                    $('#userForm')[0].reset(); // Limpia el formulario
                    alert("Usuario creado correctamente.");
                },
                error: function (xhr, status, error) {
                    console.error("Error al crear el nuevo usuario:", error);
                    alert("Error al crear el nuevo usuario. Por favor, inténtelo de nuevo.");
                }
            });
        }else{
            alert("Las contraseñas no coinciden. Por favor, verifícalas.");
        };

    });
});
