$(document).ready(function() {

    function nextSlide() {
        var currentImg = $('.active');
        var nextImg = currentImg.next();
    
        if(nextImg.length){
          currentImg.removeClass('active').css('z-index', -10);
          nextImg.addClass('active').css('z-index', 10);
        }
        else {
            var firstImg = $('.slide img:first-child');
            currentImg.removeClass('active').css('z-index', -10);
            firstImg.addClass('active').css('z-index', 10);
        }
    }
  
    function prevSlide() {
        var currentImg = $('.active');
        var prevImg = currentImg.prev();
    
        if(prevImg.length){
          currentImg.removeClass('active').css('z-index', -10);
          prevImg.addClass('active').css('z-index', 10);
        }
        else {
            var lastImg = $('.slide img:last-child');
            currentImg.removeClass('active').css('z-index', -10);
            lastImg.addClass('active').css('z-index', 10);
        }
    }

    function autoNextSlide() {
        setInterval(nextSlide, 3000);
    }

    // autoNextSlide();
  
    $('.next').click(nextSlide);
    $('.prev').click(prevSlide);
  
  });
  