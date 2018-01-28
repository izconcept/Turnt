function shazamAll(){
	shazam("one");
	shazam("two");
	shazam("three");
}
function shazam(divnumber){
	var quantity = $('input[name=quantity-'+divnumber+']').val();
	document.getElementById('text-'+divnumber).innerHTML = quantity +"oz";
	// console.log(quantity);
	document.getElementById('liquid-'+divnumber).style.backgroundPosition = "0 100%";
}
