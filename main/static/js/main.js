$(document).ready(function () {

    if ($('#fullpage').length > 0) {
        $('#fullpage').fullpage({
            anchors: ['block1', 'block2', 'block3', 'block4'],
            menu: '#menu',
            css3: true,
            scrollingSpeed: 1000
        });
    }
    if($('.phone_mask').length > 0)
        $(".phone_mask").mask("+7 (999) 999-99-99");
});