var slideNow = 1;
var slideCount = $('#slidewrapper').children().length;
var slideInterval = 3000;
var navBtnId = 0;
var translateWidth = 0;

$(document).ready(function() {
    var switchInterval = setInterval(nextSlide, slideInterval);

    $('#viewport').hover(function() {
        clearInterval(switchInterval);
    }, function() {
        switchInterval = setInterval(nextSlide, slideInterval);
    });

    $('#next-btn').click(function() {
        nextSlide();
    });

    $('#prev-btn').click(function() {
        prevSlide();
    });

    $('.slide-nav-btn').click(function() {
        navBtnId = $(this).index();

        if (navBtnId + 1 != slideNow) {
            translateWidth = -$('#viewport').width() * (navBtnId);
            $('#slidewrapper').css({
                'transform': 'translate(' + translateWidth + 'px, 0)',
                '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
                '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
            });
            slideNow = navBtnId + 1;
        }
    });
});


function nextSlide() {
    if (slideNow == slideCount || slideNow <= 0 || slideNow > slideCount) {
        $('#slidewrapper').css('transform', 'translate(0, 0)');
        slideNow = 1;
    } else {
        translateWidth = -$('#viewport').width() * (slideNow);
        $('#slidewrapper').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        slideNow++;
    }
}

function prevSlide() {
    if (slideNow == 1 || slideNow <= 0 || slideNow > slideCount) {
        translateWidth = -$('#viewport').width() * (slideCount - 1);
        $('#slidewrapper').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        slideNow = slideCount;
    } else {
        translateWidth = -$('#viewport').width() * (slideNow - 2);
        $('#slidewrapper').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        slideNow--;
    }
}

$(document).ready(function () {
        var objToStick = $("#objToStick");
        var topOfObjToStick = $(objToStick).offset().top; 

        $(window).scroll(function () {
            var windowScroll = $(window).scrollTop(); 

            if (windowScroll > topOfObjToStick) { 
                $(objToStick).addClass("topWindow");
            } else {
                $(objToStick).removeClass("topWindow");
            };
        });
});
jQuery(document).ready(function($) {
        $('.btn-minus').click(function () {
            var $input = $(this).parent().find('input');
            var count = parseInt($input.val()) - 1;
            count = count < 1 ? 1 : count;
            $input.val(count);
            $input.change();
            return false;
        });
        $('.btn-plus').click(function () {
            var $input = $(this).parent().find('input');
            $input.val(parseInt($input.val()) + 1);
            $input.change();
            return false;
        });
    });
$(document).ready(function() {
    var overlay = $('#overlay');
    var open_modal = $('.open_modal');
    var close = $('.modal_close, #overlay');
    var modal = $('.modal_div, .modal_div1');
    var closedop = $('.samovivoz');
    var closedop1 = $('.na_dostavku1');
    var modal1 = $('.modal_div');
    var modal2 = $('.modal_div1');

     open_modal.click( function(event){
         event.preventDefault();
         var div = $(this).attr('href');
         overlay.fadeIn(400,
             function(){
                 $(div)
                     .css('display', 'block')
                     .animate({opacity: 1, top: '50%'}, 200);
         });
     });
     close.click( function(){
            modal
             .animate({opacity: 0, top: '45%'}, 200,
                 function(){
                     $(this).css('display', 'none');
                     overlay.fadeOut(400);
                 }
             );
     });
      closedop.click( function(evetn){
            modal1
             .animate({opacity: 0, top: '45%'}, 200,
                 function(){
                     $(this).css('display', 'none');
                 }
             );
     });
      closedop1.click( function(evetn){
            modal2
             .animate({opacity: 0, top: '45%'}, 200, 
                 function(){
                     $(this).css('display', 'none');
                 }
             );
     });
});
function summ5() {
var sumZ = $("#ms2_order_cost").text().replace(/\s/g, '');
if (sumZ<500) {
$.jGrowl("Минимальная сумма заказа 500р", { life:2000, theme: 'ms2-message-error' });
return false;
}
else {
return true;
}
}
