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


    $.get('/api/lista_productos/', function(data) {

        $('#in-productos').empty();

        $.each(data, function(index, producto) {
            console.log(producto.id);
            $('#in-productos').append(
                "<div class='col'>" +
                    "<div class='card h-100 shadow-sm' style='max-width: 22rem; margin: auto;'>" +
                        "<img src='/static/coffeelab/img/" + producto.imagen + "' class='card-img-top' alt='" + producto.nombre + "'>" +
                        "<div class='card-body d-flex flex-column'>" +
                            "<h5 class='card-title'>" + producto.nombreProducto + "</h5>" +
                            "<p class='card-text mb-2'>" + producto.descripcion + "</p>" +
                            "<p class='mt-auto fw-bold text-end'>$" + producto.precio + "</p>" +
                            "<button type='submit' class='btn btn-primary' data-id='" + producto.nombreProducto + "'>Agregar al Carrito</button>"+
                        "</div>" +
                    "</div>" +
                "</div>"
            );
        });
    });

    $(document).on('click', '.btn-primary', function(e) {
        e.preventDefault();

        const productoId = $(this).data('id'); 
        const cantidad = 1; 

        $.ajax({
            url: '/api/vista_carrito_usuario/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'producto': productoId,
                'cantidad': cantidad
            }),
            success: function(response) {
                console.log("Producto agregado al carrito:", response);
                alert("Producto agregado al carrito.");
            },
            error: function(xhr, status, error) {
                console.error("Error al agregar el producto al carrito:", error);
                alert("Error al agregar el producto al carrito. Por favor, inténtelo de nuevo.");
            }
        })

    });
});
