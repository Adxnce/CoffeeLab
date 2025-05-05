$(document).ready(function() {
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

    $.ajax({
        url: '/api/vista_carrito_usuario/',
        type: 'GET',
        contentType: 'application/json',
        success: function (response) {
            console.log(response.items[1]);
            let precio_total_carrito = 0;
            $.each(response.items, function(index, carrito) {
                $('#carrito_container').empty();
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
        console.log(itemId);
        $.ajax({
            url: '/api/borrar_producto_carrito/'+itemId,
            type: 'DELETE',
            contentType: 'application/json',
            success: function (response) {
                alert("Producto borrado del carrito.");
                location.reload(); // o remover el div del DOM manualmente
            },
            error: function () {
                alert("Error al borrar el producto.");
            }
        });
    });



});
