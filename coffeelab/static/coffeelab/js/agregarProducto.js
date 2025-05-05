$(document).ready(function () {

    // Función para obtener el CSRF token de las cookies
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
