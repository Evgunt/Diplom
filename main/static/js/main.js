$(document).ready(function () {
    if($('.phone_mask').length > 0)
        $(".phone_mask").mask("+7 (999) 999-99-99");

    $("#id_docs").change(function(){
        if(this.files.length > 0)
            $('.errors_file').html(this.files[0].name)
        console.log(this.files);
    });
});