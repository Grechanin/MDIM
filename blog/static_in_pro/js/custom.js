// A $( document ).ready() block.
$( document ).ready(function() {
    console.log( "ready!" );
     $('.carousel-item-height').each(function(i, obj) {
	    $(this).css('top', $('#carousel').height() - $(this).height() + "px");
	    $('.carousel-control-btn-height').css('height', $('#carousel').height());
	});

 //    $('#carousel').on('slide.bs.carousel', function () {
 //    	console.log( "slide!" );
	//     $('.active').css('top', $('#carousel').height() - $('.active').height() + "px");
	//     $('.carousel-control-btn-height').css('height', $('#carousel').height());
	// })

    $(window).resize(function() {
    	console.log( "ok!" );
		$('.carousel-item-height').each(function(i, obj) {
		    $(this).css('top', $('#carousel').height() - $(this).height() + "px");
		    $('.carousel-control-btn-height').css('height', $('#carousel').height());
		});

	});

	$(".show-more button").on("click", function() {
	    var $this = $(this); 
	    var $content = $this.parent().prev("div.content");
	    var linkText = $this.text().toUpperCase();    
	    
	    if(linkText === "SHOW MORE"){
	        linkText = "Show less";
	        console.log( linkText );
	        $content.switchClass("hideContent", "showContent", 400);
	    } else {
	        linkText = "Show more";
	        console.log( linkText );
	        $content.switchClass("showContent", "hideContent", 400);
	    };

	    $this.text(linkText);
	});

});