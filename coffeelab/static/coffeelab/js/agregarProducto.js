$(document).ready(function () {
    const token = localStorage.getItem('token');

    // Manejo del formulario
    $('#productoForm').submit(function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional

        const formData = {
            nombreProducto: $('#id_nombreProducto').val(),
            precio: $('#id_precio').val(),
            descripcion: $('#id_descripcion').val(),
            imagen: $('#id_imagen').val(),
            SKU: $('#id_SKU').val()
        };

        $.ajax({
            url: '/api/lista_productos_post/',
            type: 'POST',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
            data: JSON.stringify(formData),
            success: function (response) {
                console.log("Producto agregado correctamente:", response);
                $('#productoForm')[0].reset(); // Limpia el formulario
                alert("Producto agregado correctamente.");
            },
            error: function (xhr, status, error) {
                console.error("Error al agregar el producto:", error);
                alert("Error al agregar el producto. Por favor, inténtelo de nuevo.");
            }
        });
    });
});
