document.addEventListener("DOMContentLoaded", function() {
    const inicioLink = document.querySelector('.navbar-nav .nav-item:nth-child(1) .nav-link');
    const planesLink = document.querySelector('.navbar-nav .nav-item:nth-child(2) .nav-link');
    const contactoLink = document.querySelector('.navbar-nav .nav-item:nth-child(3) .nav-link');

    // Agregar un evento de clic al enlace "Inicio"
    inicioLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
        
        // Hacer scroll a la parte superior de la página
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Desplazamiento suave
        });
    });

    // Agregar un evento de clic al enlace "Planes"
    planesLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
        
        // Hacer scroll a la parte superior de la página
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Desplazamiento suave
        });
    });

    // Agregar un evento de clic al enlace "Contacto"
    contactoLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
        
        // Hacer scroll al final de la página
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth' // Desplazamiento suave
        });
    });
});