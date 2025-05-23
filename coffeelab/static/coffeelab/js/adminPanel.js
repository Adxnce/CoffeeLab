$(document).ready(function() {

    $.get('/api/lista_usuarios/', function(data) {
        $('#in-usuarios').empty();
        $.each(data, function(index, usuario) {
            $('#in-usuarios').append(
                "<tr><td>" + usuario.username + "</td>" +
                "<td>" + usuario.email + "</td>" +
                "<td>" + usuario.direccion + "</td>" +
                "<td>" + usuario.ciudad + "</td>" +
                "<td>" + usuario.rol + "</td>" +
                "<td><button type='button' class='btn btn-primary btn-modificar' data-id='" + usuario.username + "'>Modificar</button></td>" +
                "<td><button type='button' class='btn btn-danger btn-eliminar' data-id='" + usuario.username + "'>Eliminar</button></td>" +
                "</tr>"
            );
            
        });
    });

// recuperar el token de localStorage
    const token = localStorage.getItem('token');
    const rol = localStorage.getItem('rol');

    $(document).on('click', '.btn-modificar', function() {
        const username = $(this).data('id');
        window.location.href = '/adminPanelUpdate/' + username + '/';
    });
});



