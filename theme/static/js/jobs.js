(function ($) {
    $.fn.tilt = function () {
        //Variables
        let perspective = "1000px",
            delta = 20,
            width = this.width(),
            height = this.height(),
            midWidth = width / 2,
            midHeight = height / 2;
        //Events
        this.on({
            mousemove: function (e) {
                let pos = $(this).offset(),
                    cursPosX = e.pageX - pos.left,
                    cursPosY = e.pageY - pos.top,
                    cursCenterX = midWidth - cursPosX,
                    cursCenterY = midHeight - cursPosY;

                $(this).css(
                    "transform",
                    "perspective(" +
                    perspective +
                    ") rotateX(" +
                    cursCenterY / delta +
                    "deg) rotateY(" +
                    -(cursCenterX / delta) +
                    "deg)"
                );
                $(this).removeClass("is-out");
            },
            mouseleave: function () {
                $(this).addClass("is-out");
                $(this).removeAttr("style");
            }
        });
        //Return
        return this;
    };
})(jQuery);

//Set plugin on cards
$(".job-card").tilt();

new TypeIt(".project-head-text", {
    speed: 10,
    waitUntilVisible: true,
}).go();