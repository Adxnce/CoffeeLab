$(document).ready(function() {
    
    const token = localStorage.getItem('token');
    const rol = localStorage.getItem('rol');
    const username = localStorage.getItem('username');

    if (token && rol == "admin") {
        $('#welcome').css('display', 'block');
    };

    $.ajax({
        url: '/api/lista_productos/',
        type: 'GET',
        contentType: 'application/json',
        success: function (response) {

            $('#in-productos').empty();
            $.each(response, function(index, producto) {
                $('#in-productos').append(
                    "<div class='col'>" +
                    "<div class='card h-100 shadow-sm' style='max-width: 22rem; margin: auto;'>" +
                        // "<img src='/static/coffeelab/img/" + producto.imagen + "' class='card-img-top' alt='" + producto.nombre + "'>" +
                        "<img src='/static/coffeelab/img/" + producto.imagen + "' " +
                        "onerror=\"this.onerror=null;this.src='/static/coffeelab/img/default.jpeg';\" " +
                        "class='card-img-top' alt='" + producto.nombreProducto + "'>" +
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
        }
    });



    });

    $(document).on('click', '.btn-primary', function(e) {
        e.preventDefault();

        const token = localStorage.getItem('token');
        const productoId = $(this).data('id'); 
        const cantidad = 1; 
        $.ajax({
            url: '/api/vista_carrito_usuario/',
            type: 'POST',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
            data: JSON.stringify({
                'producto': productoId,
                'cantidad': cantidad,
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

