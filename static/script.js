$( document ).ready(function() {

    var $mintContainer = $('.jumbotron'),
        $mintText = $('#mint-text'),
        $mintButton = $('#mint-request'),
        url = $mintText.data('url-for'),
        steps = [
            'A learning experience through the finest pieces of literature...',
            '...taken directly from one of the best sites...',
            '...where the wisest gather to share the most ancient of the lores...',
            'Click/tap here to begin.'
        ],
        timer = 3500;

    function beginSteps() {
        var i = 0;
        var loop = setInterval(function() {
            if (i < steps.length) {
                changeMint(steps[i]);
                if (i == steps.length-1) {
                    $mintContainer.on('click', getMint);
                    clearInterval(loop);
                }
                i = i + 1;
            } else {
                clearInterval(loop);
            }
        }, timer);
    }

    function changeMint(text, reminder=false) {
        $mintText.find("span")
            .animate({opacity:0}, 1050)
            .queue(function(){
                $(this).text(text).dequeue();
            })
            .animate({opacity:1}, 1050);

        //if (reminder) {
        //    setTimeout(function() {
        //        $mintText.html(text + '<p class="text-muted"><small><em>tap for more</em></small></p>');
        //    }, 5000);
        //}
    }

    function getMint() {
        $mintText.load(url, function(response, status, xhr) {
            if (status === 'success') {
                changeMint(response, reminder=true);
            }
            if (status === 'error') {
                changeMint('Something bad happened, try again.');
            }
        });
    }

    $mintButton.on('click', function(){
        $mintButton.animate({opacity:0});
        beginSteps();
    });

});
