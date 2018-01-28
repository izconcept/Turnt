$(document).ready(function () {
    $('.drink-carousel').slick({
        centerMode: true,
        centerPadding: '60px',
        slidesToShow: 3,
        prevArrow:"<i class=\"fa fa-arrow-circle-o-left prev\" aria-hidden=\"true\" style=\"font-size: 2em;\"></i>",
        nextArrow:"<i class=\"fa fa-arrow-circle-o-right next\" aria-hidden=\"true\" style=\"font-size: 2em;\"></i>",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 1
                }
            }
        ]
    });
});