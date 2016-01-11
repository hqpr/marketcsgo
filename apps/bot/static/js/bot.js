$(document).ready(function(){

    $('#insert_start').on('click', function(){
        $('#insert_form').hide();
        $('.alert-success').show();
        $('#insert_form').ajaxSubmit({
            success: function(resp){
                if (resp.success) {
                    console.log(success);
                    $('.alert-success').show();
                } else {
                    var errors = $('body');
                    errors.html(resp.html);
                    $('.alert-danger').show();
                }
            }
        });
    });

    var update_form = $('#update_form');
    $('#update_start').on('click', function(){
        update_form.hide();
        var status = $('.alert-warning');
        status.show().addClass('temp');
        update_form.ajaxSubmit({
            success: function(resp){
                if (resp.success) {
                    console.log('success');
                    $('.alert-warning').hide();
                       $('.temp').removeClass('alert-warning').fadeOut().addClass('alert-success').fadeIn().text('Completed!');
                    $('#result').fadeIn().text(resp.msg);
                } else {
                    console.log('error');
                    $('#result').fadeIn().text('Error');
                    //console.log(data.msg);

                }
            }
        });
    });

    //$('#on_debug').on('click', function(){
        //window.location.replace("");
    //})


});
