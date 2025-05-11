$(document).ready(function() {

    const token = localStorage.getItem('token');

    $.ajax({
        url: '/api/lista_productos/',
        type: 'GET',
        contentType: 'application/json',
        success: function (response) {
            $.each(response, function(index, producto) {
                console.log(producto);
                $('#in-productos').append(
                    "<tr><td>" + producto.SKU + "</td>" +
                    "<td>" + producto.nombreProducto + "</td>" +
                    "<td>" + producto.precio + "</td>" +
                    // "<td>" + usuario.rol + "</td>" +
                    "<td><button type='button' class='btn btn-primary btn-modificar' data-id='" + producto.SKU + "'>Modificar</button></td>" +
                    "<td><button type='button' class='btn btn-danger btn-eliminar' data-id='" + producto.SKU + "'>Eliminar</button></td>" +
                    "</tr>"
                );
                
            });
        }
    });

    $(document).on('click', '.btn-modificar', function() {
        const SKU = $(this).data('id');
        console.log(SKU);
        window.location.href = '/administrarProductoModificar/' + SKU + '/';
    });

    // Manejo del formulario
    $(document).on('click', '.btn-eliminar', function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional

        const SKU = $(this).data('id'); // Obtiene el ID del usuario a eliminar
        $.ajax({
            url: '/api/lista_productos_mod/' + SKU,
            type: 'DELETE',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
            success: function (response) {
                console.log("Producto eliminado:", response);
                alert("Producto eliminado correctamente.");
                location.reload(); // Recarga la página para actualizar la lista de usuarios
            },
            error: function (xhr, status, error) {
                console.error("Error al eliminar el Producto:", error);
                alert("Error al eliminar el usuario. Por favor, inténtelo de nuevo.");
            }
        });
    });


});


