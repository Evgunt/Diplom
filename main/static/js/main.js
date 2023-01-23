$(document).ready(function () {

    if ($('#fullpage').length > 0) {
        $('#fullpage').fullpage({
            anchors: ['block1', 'block2', 'block3', 'block4'],
            menu: '#menu',
            css3: true,
            scrollingSpeed: 1000
        });
    }
});