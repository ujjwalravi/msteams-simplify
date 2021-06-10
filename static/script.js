$(document).ready(function() {
    $(".spin").hide();
    $(".endtime-info").hide();
    $("#flexRadioDefault2") 
    .change(function(){ 
        if( $(this).is(":checked") ){ 
            $(".endtime-info").hide();
        }
    });
    $("#flexRadioDefault1") 
    .change(function(){ 
        if( $(this).is(":checked") ){ 
            $(".endtime-info").show();
        }
    });
    $('a[href$="#Modal"]').on( "click", function() {
        $('#Modal').modal('show');
     });
    $('input[type=submit]').on("click", function() {
        $('.spin').show();
    });
});