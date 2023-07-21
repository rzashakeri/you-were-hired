function collapse(obj) {
    let element = obj;
    if (element.classList.contains("collapse-open")) {
        element.classList.remove("collapse-open");
    } else {
        element.classList.add("collapse-open");
    }
}