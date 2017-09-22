$(document).ready(function(){
	$('.skillbar').on('each',function(){
		$(this).find('.skillbar-bar').animate({
			width: $(this).attr('data-percent')
		},6000);
	});
});