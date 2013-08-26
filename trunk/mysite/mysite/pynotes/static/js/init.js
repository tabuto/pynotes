var django = {
    "jQuery": jQuery.noConflict(true)
};
var jQuery = django.jQuery;
var $=jQuery;
/* Nivo Slider */
$(window).load(function() {

    $('#slider').nivoSlider({directionNavHide:false});

});

$(document).ready(function(){
	

    /* Fancy Box */
    $('a.lightbox').fancybox({
        'titlePosition'	: 'over',
        'padding'       : 16,
        'opacity'		: true,
		'overlayShow'	: false,
		'transitionIn'	: 'elastic',
		'transitionOut'	: 'elastic'
  	});
   // youtube videos with fancy box
   $('a.lightbox-video').click(function() {

        $.fancybox( {
            'titlePosition'	: 'over',
            'padding'       : 16,
            'opacity'		: true,
		    'overlayShow'	: false,
		    'transitionIn'	: 'elastic',
		    'transitionOut'	: 'elastic',
            'href'          : this.href.replace(new RegExp("watch\\?v=", "i"), 'v/'),
            'type'          : 'swf',
            'swf'           : {'wmode':'transparent','allowfullscreen':'true'}

          });
            return false;
    });

    // Fade in/out on hover
    /*
    $("ul.folio-list li .thumb img").fadeTo("slow", 0.6);
    $("ul.folio-list li .thumb img").hover(function(){
        $(this).fadeTo("slow", 1.0);
    },function(){
        $(this).fadeTo("slow", 0.6);
    });
    */
});

/*
 * Funzioni specifiche per pynotes
 */

function toggleNoteBody(id){
	   //alert("this is an alert for id: "+id);
	   //alert('thumb clicked');
	   target="#note_body_"+id;
	    $(target).slideToggle('slow');
		//});
	}

