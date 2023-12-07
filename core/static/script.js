window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var heroHeight = document.getElementById('landing').offsetHeight;
    var textElement = document.querySelector('#landing .placeholder-text');
    var navbar = document.querySelector('.navbar');
    var mainContent = document.getElementById('main-content');
    
    var navbarHeight = 60;


    // Parallax effect for text
    textElement.style.transform = 'translate(-50%, calc(-50% + ' + scrollPosition * 0.5 + 'px))';

    // Hide text after scrolling past the hero section
    if (scrollPosition > heroHeight) {
        textElement.style.display = 'none';
    } else {
        textElement.style.display = 'block';
    }
       // Check if the user has scrolled past the hero section
       if (scrollPosition >= heroHeight) {
        navbar.style.top = '0'; // Bring navbar into view
        mainContent.style.paddingTop = navbarHeight + 'px';
    } else {
        navbar.style.top = '-100%'; // Hide navbar
        mainContent.style.paddingTop = '0';
    }
});

document.querySelector('.scroll-for-more').addEventListener('click', function(e) {
    e.preventDefault(); // Prevent the default anchor behavior

    // Smoothly scroll to the main content section
    document.getElementById('main-content').scrollIntoView({
        behavior: 'smooth'
    });
});

