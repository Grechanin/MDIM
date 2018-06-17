
$( document ).ready(function() {

	carouselResize ();

	$(window).resize(function() {
		carouselResize ();
	});





 //     $('.carousel-item-height').each(function(i, obj) {
	//     $(this).css('top', $('#carousel').height() - $(this).height() + "px");
	//     $('.carousel-control-btn-height').css('height', $('#carousel').height());
	// });

 //    $('#carousel').on('slide.bs.carousel', function () {
 //    	console.log( "slide!" );
	//     $('.active').css('top', $('#carousel').height() - $('.active').height() + "px");
	//     $('.carousel-control-btn-height').css('height', $('#carousel').height());
	// })

 //    $(window).resize(function() {
 //    	console.log( "ok!" );
	// 	$('.carousel-item-height').each(function(i, obj) {
	// 	    $(this).css('top', $('#carousel').height() - $(this).height() + "px");
	// 	    $('.carousel-control-btn-height').css('height', $('#carousel').height());
	// 	});

	// });

	$(".show-more a").on("click", function(e) {
	    var $this = $(this); 
	    var $content = $this.parent().prev("div.content");
	    var linkText = $this.text().toUpperCase();    
	    
	    if(linkText === "ДЕТАЛЬНІШЕ"){
	        $content.switchClass("hideContent", "showContent", 400);
	        $this.addClass("opened", 400);
	        linkText = "Згорнути";
	    } else {
	        $content.switchClass("showContent", "hideContent", 400);
	        $this.removeClass("opened", 400);
	        linkText = "Детальніше";
	    };

	    $this.text(linkText);

	    e.preventDefault();
	});

});

function carouselResize () {
	var viewportHeight = $( window ).height();
	var headerHeight = $('.header').height();
	var navbarHeight = $('.navbar').height();
	var navbarPadding = parseInt($('.navbar').css('padding-top'));
	var headerNavbarHeight = headerHeight + navbarHeight;

    // console.log( "ready!" );
    // console.log( viewportHeight );
    // console.log( navbarPadding );

	$('.carosel-image-resize').css('max-height', viewportHeight - headerNavbarHeight - navbarPadding*2);
}