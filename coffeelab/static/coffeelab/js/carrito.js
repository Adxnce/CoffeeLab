$(document).ready(function() {

    const token = localStorage.getItem('token');

    $.ajax({
        url: '/api/vista_carrito_usuario/',
        type: 'GET',
        contentType: 'application/json',
        headers: {
            'Authorization': 'Token ' + token
        },
        success: function (response) {
            let precio_total_carrito = 0;
            $.each(response.items, function(index, carrito) {
                precio_total_carrito += carrito.precio_unitario * carrito.cantidad;
                precio_total_producto = carrito.precio_unitario * carrito.cantidad;
                    $('#carrito_container').append(
                    "<div class='card mb-3'>"+
                        "<div class='card-body'>"+
                            "<h5 class='card-title'>"+carrito.producto+"</h5>"+
                            "<p class='card-text'>Cantidad: "+carrito.cantidad+"</p>"+
                            "<p class='card-text'><strong>Precio Unitario: "+carrito.precio_unitario+"</strong></p>"+
                            "<button type='button' class='btn btn-primary' data-id='"+carrito.id+"'>Borrar producto</>"+
                            
                        "</div>"+
                    "</div>"
                );

                $('#carrito_detalle').append(
                    "<p class='card-text'>"+carrito.producto+".   Precio total: $"+precio_total_producto+"</p>"
                );

                
            });


            $("#carrito_total").append(
                "<strong>Total: $"+precio_total_carrito+"</strong>"
            )

        },
        error: function (xhr, status, error) {
            console.error("Error al obtener el carrito de usuario:", error);
            alert("Error al obtener el carrito de usuario. Por favor, inténtelo de nuevo.");
        }
    })

    $(document).on('click', '.btn-primary', function() {
        const itemId = $(this).data('id');
        $.ajax({
            url: '/api/borrar_producto_carrito/'+itemId,
            type: 'DELETE',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
            success: function (response) {
                alert("Producto borrado del carrito.");
                location.reload();
            },
            error: function () {
                alert("Error al borrar el producto.");
            }
        });
    });



});
