document.addEventListener("DOMContentLoaded", function() {
    var navbar = document.querySelector('.navbar');
    var heroSection = document.getElementById('landing');
    var mainContent = document.getElementById('main-content');
    var navbarHeight = 60; // Adjust as needed

    if (heroSection) {
        // Initially hide the navbar if hero section exists
        navbar.style.top = '-100%';

        window.addEventListener('scroll', function() {
            if (window.scrollY >= heroSection.offsetHeight) {
                navbar.style.top = '0';
                if (mainContent) mainContent.style.paddingTop = navbarHeight + 'px';
            } else {
                navbar.style.top = '-100%';
                if (mainContent) mainContent.style.paddingTop = '0';
            }
        });
    }

    // Add smooth scroll for 'Scroll for more' if it exists
    var scrollMoreButton = document.querySelector('.scroll-for-more');
    if (scrollMoreButton) {
        scrollMoreButton.addEventListener('click', function(e) {
            e.preventDefault();
            mainContent.scrollIntoView({ behavior: 'smooth' });
        });
    }
});
