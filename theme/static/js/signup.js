new TypeIt("#signup-title", {
    speed: 10,
    waitUntilVisible: true,
}).go();


function calculateDistance(x1, y1, x2, y2) {
    const xDistance = x2 - x1;
    const yDistance = y2 - y1;

    return Math.sqrt(Math.pow(xDistance, 2) + Math.pow(yDistance, 2));
}


document.addEventListener('mousemove', (event) => {
    const hoverMe = document.getElementById('signup-button');
    const hoverMeRect = hoverMe.getBoundingClientRect();
    const cursorX = event.clientX;
    const cursorY = event.clientY;

    const distance = calculateDistance(
        cursorX,
        cursorY,
        hoverMeRect.left + hoverMeRect.width / 2,
        hoverMeRect.top + hoverMeRect.height / 2
    );

    const threshold = 50;

    if (distance <= threshold) {
        changePosition();
    }
});


function inputChange(valueHere) {
    const element = document.getElementById('signup-button');
    let regularExpression = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    let result = regularExpression.test(valueHere);
    if (result) {
        element.style.left = '0';
        element.style.right = 'initial';
        element.classList.remove("btn-error");
        element.classList.add("btn-success");
        element.classList.add("w-full");
    } else {
        element.classList.remove("btn-info");
        element.classList.add("btn-error");
        element.classList.remove("w-full");

    }
}


function changePosition() {

    const element = document.getElementById('signup-button');

    const computedStyle = window.getComputedStyle(element);

    const position = computedStyle.getPropertyValue('left');
    const password = document.getElementById('id_password1');


    if (password.value.length !== 10) {
        if (position === '0px') {
            element.style.right = '0';
            element.style.left = 'initial';

        }
        if (position >= '170px') {
            element.style.left = '0';
            element.style.right = 'initial';
        }
    } else {
        element.style.left = '0';
        element.style.right = 'initial';
    }

}