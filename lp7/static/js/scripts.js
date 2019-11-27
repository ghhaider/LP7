$(document).ready(function () {
// Function for Moving text
    $(function () {
        "use strict";
        $(".perfectMatchText h5, .aboutWelcome span strong").typed({
            strings: ["Freelancers", "SMEs", "Co-Workers"], //Headlines(Change It)
            loop: true,
            startDelay: 1500,
            backDelay: 2000
        });
    });

//Members Logos Slider
    $('.memberSlide').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });

// Testimonial Slider
    $("#testimonial-slider").owlCarousel({
        items: 1,
        itemsDesktop: [1000, 2],
        itemsDesktopSmall: [979, 1],
        itemsTablet: [768, 1],
        pagination: false,
        navigation: false,
        slideSpeed: 1000,
        singleItem: true,
        transitionStyle: "goDown",
        navigationText: ["", ""],
        autoPlay: true
    });

// LP7 Features Card
    $('.LP7featuresBody').mouseover(function () {
        $(this).css({
                'background-color': '#f64c72',
            }
        )
    });
    $('.LP7featuresBody').mouseleave(function () {
        $(this).css({
                'background-color': '#130959',
            }
        )
    });
    // LP7 Pricing Tables
    $('.packageBody').mouseover(function () {
        $(this).css({
                'background-color': '#f64c72',
            }
        )
    });
    $('.packageBody').mouseleave(function () {

        $(this).css({
                'background': '#130959'
            }
        )
    });
    // LP7 Pricing Tables
    $('.optionalAddonBody').mouseover(function () {
        $(this).css({
                'background-color': '#f64c72',
            }
        )
    });
    $('.optionalAddonBody').mouseleave(function () {

        $(this).css({
                'background': '#130959'
            }
        )
    });

// Scroll to top button
    $(window).scroll(function () {
        var height = $(window).scrollTop();
        if (height > 1000) {
            $('#back2Top').fadeIn();
        } else {
            $('#back2Top').fadeOut();
        }
    });
    $("#back2Top").click(function (event) {
        event.preventDefault();
        $("html, body").animate({scrollTop: 0}, "slow");
        return false;
    });


    // Animation on scroll initialize
    AOS.init();

 // Small font size if discount offers in RWP
    let discountRWP = $(".discountedPriceRWP");
    if(discountRWP.length > 0){
    discountRWP.each(function() {
        let disc = $(this).text();
        let discPrice = parseInt(disc);
        let price = "RWP"+discPrice;
          $('#' +  price).css({
            'font-size': '15px',
              'color': 'sandybrown'
         });
        let discountPriceOffered = $('#' +  price).text()
         $('#' +  price).empty();
        $('#' +  price).html("<del></del>");
        $('#' +  price+" "+ "del").text(discountPriceOffered);
    })
    }

    // Small font size if discount offers in ISD
    let discountISD = $(".discountedPriceISD");
    if(discountISD.length > 0){
    discountISD.each(function() {
        let disc = $(this).text();
        let discPrice = parseInt(disc);
        let price = "ISD"+discPrice;
          $('#' +  price).css({
            'font-size': '15px',
              'color': 'sandybrown'
         });
        let discountPriceOffered = $('#' +  price).text()
         $('#' +  price).empty();
        $('#' +  price).html("<del></del>");
        $('#' +  price+" "+ "del").text(discountPriceOffered);
    })
    }


// Date Time Picker
    $(function () {
       $('#datePicker').datetimepicker({
           format: 'DD/MM/YYYY'
       });
        $('#timePicker').datetimepicker({
            format: 'LT'
        });
    });

// Gallery Call
$('[data-fancybox="gallery"], [data-fancybox="gallery1"]').fancybox({
	keyboard: true,
    loop: false,
    arrows: true,
    buttons: [
    "zoom",
    //"share",
    "slideShow",
    //"fullScreen",
    //"download",
    "thumbs",
    "close"
  ],
});



});


