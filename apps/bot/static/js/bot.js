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
        $('.alert-warning').show();
        update_form.ajaxSubmit({
            success: function(resp){
                if (resp.success) {
                    console.log('success');
                    $('.alert-success').show();
                    $('#result').fadeIn().text(resp.msg);
                } else {
                    console.log('error');
                    $('#result').fadeIn().text(resp.msg);
                    //console.log(data.msg);
                    //$('.alert').removeClass('alert-warning').addClass('alert-success').text('Completed!');
                }
            }
        });
    });

});
