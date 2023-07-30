function collapse(obj) {
    let element = obj;
    if (element.classList.contains("collapse-open")) {
        element.classList.remove("collapse-open");
        element.classList.add("collapse-close");
    } else {
        element.classList.add("collapse-open");
        element.classList.remove("collapse-close");

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

new TypeIt("#header-logo", {
    lifeLike: false,
    speed: 0
})
    .delete(5, {instant: true})
    .type("D")
    .pause(100)
    .type("o")
    .pause(100)
    .type("n")
    .pause(100)
    .type("'")
    .pause(100)
    .type("t")
    .pause(100)
    .type(" ")
    .pause(100)
    .type("B")
    .pause(100)
    .type("e")
    .pause(100)
    .type(" ")
    .pause(100)
    .type("R")
    .pause(100)
    .type("e")
    .pause(100)
    .type("j")
    .pause(100)
    .type("e")
    .pause(100)
    .type("c")
    .pause(100)
    .type("t")
    .pause(100)
    .type("e")
    .pause(100)
    .type("d")
    .pause(2160)
    .delete(1)
    .pause(623)
    .delete(1)
    .pause(40)
    .delete(1)
    .pause(36)
    .delete(1)
    .pause(38)
    .delete(1)
    .pause(40)
    .delete(1)
    .pause(36)
    .delete(1)
    .pause(39)
    .delete(1)
    .pause(41)
    .delete(1)
    .pause(37)
    .delete(1)
    .pause(35)
    .delete(1)
    .pause(39)
    .delete(1)
    .pause(42)
    .delete(1)
    .pause(34)
    .delete(1)
    .pause(37)
    .delete(1)
    .pause(38)
    .delete(1)
    .pause(37)
    .delete(1)
    .pause(660)
    .type("H")
    .pause(255)
    .type("I")
    .pause(271)
    .type("R")
    .pause(148)
    .type("E")
    .pause(207)
    .type("D")
    .pause(2000)
    .delete(1)
    .pause(37)
    .delete(1)
    .pause(37)
    .delete(1)
    .pause(37)
    .delete(1)
    .pause(37)
    .delete(1)
    .type("Y")
    .pause(100)
    .type("o")
    .pause(100)
    .type("u")
    .pause(100)
    .type(" ")
    .pause(100)
    .type("W")
    .pause(100)
    .type("e")
    .pause(100)
    .type("r")
    .pause(100)
    .type("e")
    .pause(100)
    .type(" ")
    .pause(100)
    .type("H")
    .pause(100)
    .type("i")
    .pause(100)
    .type("r")
    .pause(100)
    .type("e")
    .pause(100)
    .type("d")
    .go();


function showHidePassword(targetID) {
    let element = document.getElementById(targetID);
    let showPasswordIcon = document.getElementById("show-password-icon");
    let HidePasswordIcon = document.getElementById("hide-password-icon");

    if (element.type === "password") {
        element.type = "text";
        showPasswordIcon.classList.add("hidden");
        HidePasswordIcon.classList.remove("hidden");
    } else {
        element.type = "password";
        showPasswordIcon.classList.remove("hidden");
        HidePasswordIcon.classList.add("hidden");
    }

}


