$(document).ready(function () {
    $("#recuperarForm").submit(function (event) {
        event.preventDefault();

        const formData = {
            email: $("#correo").val()
        }
        $.ajax({
            url: "/api/recuperar_clave/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function (response) {
                console.log("Correo enviado correctamente:", response);
                alert("Correo enviado correctamente. Por favor, revise su bandeja de entrada.");
                $("#recuperarForm")[0].reset(); // Limpiar el formulario
            },
            error: function (xhr, status, error) {
                console.error("Error al enviar el correo:", error);
                alert("Error al enviar el correo. Por favor, inténtelo de nuevo.");
                $("#recuperarForm")[0].reset(); // Limpiar el formulario
            }


        })

    });
});