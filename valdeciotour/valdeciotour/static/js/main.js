$(document).ready(function() {
	// Header Scroll
	$(window).on('scroll', function() {
		var scroll = $(window).scrollTop();

		if (scroll >= 50) {
			$('#header').addClass('fixed');
		} else {
			$('#header').removeClass('fixed');
		}
	});

	// Fancybox
	$('.work-box').fancybox();

	// Flexslider
	$('.flexslider').flexslider({
		animation: "fade",
		directionNav: false,
	});

	// Page Scroll
	var sections = $('section')
		nav = $('nav[role="navigation"]');

	$(window).on('scroll', function () {
	  	var cur_pos = $(this).scrollTop();
	  	sections.each(function() {
	    	var top = $(this).offset().top - 76
	        	bottom = top + $(this).outerHeight();
	    	if (cur_pos >= top && cur_pos <= bottom) {
	      		nav.find('a').removeClass('active');
	      		nav.find('a[href="#'+$(this).attr('id')+'"]').addClass('active');
	    	}
	  	});
	});
	nav.find('a').on('click', function () {
	  	var $el = $(this)
	    	id = $el.attr('href');
		$('html, body').animate({
			scrollTop: $(id).offset().top - 75
		}, 500);
	  return false;
	});

	// Mobile Navigation
	$('.nav-toggle').on('click', function() {
		$(this).toggleClass('close-nav');
		nav.toggleClass('open');
		return false;
	});	
	nav.find('a').on('click', function() {
		$('.nav-toggle').toggleClass('close-nav');
		nav.toggleClass('open');
	});
});

/* ******************************************
	   Filtro para Imagens de Pacotes
   ****************************************** */

	if ($('.isotope-container').length>0) {
		  $(window).load(function() {
			$('.isotope-container').fadeIn();
			var $container = $('.isotope-container').isotope({
			  itemSelector: '.isotope-item',
			  layoutMode: 'masonry',
			  transitionDuration: '0.6s',
			  filter: "*"
			});
			// filter items on button click
			$('.filters').on( 'click', 'ul.nav li a', function() {
			  var filterValue = $(this).attr('data-filter');
			  $(".filters").find("li.active").removeClass("active");
			  $(this).parent().addClass("active");
			  $container.isotope({ filter: filterValue });
			  return false;
			});
		  });
		};

/* ****************************************** */


/* ******************************************
	 Configuração do Carousel de Galeria 
   ****************************************** */

	$('.owl-carousel').owlCarousel({
		loop:true,
		margin:10,
		dots:true,
		nav:true,
		autoPlay: 3000, 
		responsive:{
			0:{
				items:1
			},
			600:{
				items:3
			},
			1000:{
				items:3
			}
		}
	});

/* ****************************************** */