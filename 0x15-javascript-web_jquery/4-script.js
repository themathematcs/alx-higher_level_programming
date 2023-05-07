//Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag
$(function(){
	$('DIV#toggle_header').click(function (){
		$('header').toggleClass('red green');
	});
});
