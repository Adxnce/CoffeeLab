$(document).ready(function() {
    // Obtener imagen aleatoria de café
    $.getJSON('https://coffee.alexflipnote.dev/random.json', function(data) {
        $('#coffee-img').attr('src', data.file);
    });

    // Obtener frase motivacional
    $.getJSON('https://api.adviceslip.com/advice', function(data) {
        $('#advice-text').text('"' + data.slip.advice + '"');
    });
});
