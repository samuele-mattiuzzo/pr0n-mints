$( document ).ready(function() {

    var $mintText = $('#mint-text'),
        $mintButton = $('#mint-request'),
        url = $mintButton.data('url-for');


    $mintButton.on('click', function(){
        $mintText.load(url);
    });

});
