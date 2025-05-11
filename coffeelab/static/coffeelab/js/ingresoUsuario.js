$(document).ready(function() {
    // prevent default form submission
    $(document).on('click', '#submit-button', function(){
        
        const formData = {
            username: $('#id_username').val(),
            password: $('#id_password').val()
        }
        
        $.ajax({
            url: '/api/login/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {

                localStorage.setItem('token', response.token);
                localStorage.setItem('rol', response.rol);    
                localStorage.setItem('username', response.username);
                
                alert("Usuario logueado correctamente.");
                if (response.rol == "admin") {
                    window.location.href = '/adminPanel/'; // Redirigir al panel de administración
                }
                else if (response.rol == "cliente") {
                    window.location.href = '/userPanel/'; // Redirigir al panel de usuario
                }
            },
            error: function(xhr, status, error) {
                console.error("Error al loguear el usuario:", error);
                alert("Error al loguear el usuario. Por favor, inténtelo de nuevo.");
                }
            });
        });
    });