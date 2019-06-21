$(document).ready(function(){
	setTimeout(function()
	{
		swip1()
	},500)
})
function swip1(){
	var swiper = new Swiper('.swiper-container', {
		direction:'horizontal',
		loop:true,
		speed:1000,
		autoplay:true,
		autoplayDisableOnInteraction : false,
		effect : 'cube',
		slideShadows: true,
    	shadow: true,
    	shadowOffset:0,
    	shadowScale: 0,
    	autoHeight: true,
//
    	pagination: {
       		el: '.swiper-pagination',
//      	type: 'progressbar',
			hideOnClick :true,
		},
//  	control:true,
    	//
   }
)}
