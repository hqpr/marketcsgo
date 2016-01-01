$(document).ready(function(){

    $('#insert_start').on('click', function(){
        $('#insert_form').hide();
        $('.alert-success').show();
        $('#insert_form').ajaxSubmit({
            success: function(data){
                if (data.success) {
                    console.log(success);
                    $('.alert-success').show();
                } else {
                    var errors = $('body');
                    errors.html(data.html);
                    $('.alert-danger').show();
                }
            }
        });
    });

    var update_form = $('#update_form');
    $('#update_start').on('click', function(){
        update_form.hide();
        $('.alert-warning').show();
        update_form.ajaxSubmit({
            success: function(data){
                if (data.success) {
                    console.log(success);
                    $('.alert-success').show();
                } else {
                    $('#result').fadeIn().text(data.msg);
                    console.log(data.msg);
                    $('.alert').removeClass('alert-warning').addClass('alert-success').text('Completed!');
                }
            }
        });
    });

});
