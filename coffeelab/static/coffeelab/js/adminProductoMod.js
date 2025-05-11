$(document).ready(function() {

    // Recuperar el token de localStorage
    const token = localStorage.getItem('token');
    const pathParts = window.location.pathname.split('/');
    const sku = pathParts[2]; // si es /productos/5/, esto devuelve "5"
    let img = "";
    
    $.ajax({
        url: '/api/lista_productos_id/' + sku,
        type: 'GET',
        contentType: 'application/json',
        headers: {
            'Authorization': 'Token ' + token
        },
        success: function (response) {      
            img = response.imagen;
        },
    })


    // Manejo del formulario
    $('#userForm').submit(function (e) {
        e.preventDefault(); // Evita que se envíe el formulario de forma tradicional
        
        const formData = {
            SKU: sku,
            nombreProducto: $('#id_nombreProducto').val(),
            descripcion: $('#id_descripcion').val(),
            precio: $('#id_precio').val(),
            imagen: img,
        };


        $.ajax({
            url: '/api/lista_productos_mod/' + sku  ,
            type: 'PUT',
            contentType: 'application/json',
            headers: {
                'Authorization': 'Token ' + token
            },
            data: JSON.stringify(formData),
            success: function (response) {

                console.log("Usuario actualizado correctamente:", response);
                alert("Usuario actualizado correctamente.");
                window.location.href = '/administrarProductos/'; // Redirige a la página del panel de administración
            },
            error: function (xhr, status, error) {
                console.error("Error al actualizar el usuario:", error);
                alert("Error al actualizar el usuario. Por favor, inténtelo de nuevo.");
            }
        });
    });
});
