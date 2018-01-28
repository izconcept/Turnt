$(document).ready(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function () {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
    $('.drink-carousel').slick({
        centerMode: true,
        centerPadding: '60px',
        slidesToShow: 3,
        arrows: false,
        prevArrow: "<i class=\"fa fa-arrow-circle-o-left prev\" aria-hidden=\"true\" style=\"font-size: 2em;\"></i>",
        nextArrow: "<i class=\"fa fa-arrow-circle-o-right next\" aria-hidden=\"true\" style=\"font-size: 2em;\"></i>",
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
    $("#getTurnt").click(function() {
        var drink = $('.slick-center').data('drink');
        console.log(drink);
        socket.emit('get turnt', {data: drink});
    })
});

