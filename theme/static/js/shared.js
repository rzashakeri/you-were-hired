function collapse(obj) {
    let element = obj;
    if (element.classList.contains("collapse-open")) {
        element.classList.remove("collapse-open");
    } else {
        element.classList.add("collapse-open");
    }
}


document.addEventListener('DOMContentLoaded', function () {
    const targetElement = document.querySelector('#header');

    // Function to add the class when scrolling starts
    function addClassOnScroll() {
        if (window.scrollY > 0) {
            targetElement.classList.add('shadow-sm');
        } else {
            targetElement.classList.remove('shadow-sm');
        }
    }

    // Event listener for scroll event
    window.addEventListener('scroll', addClassOnScroll);
});
