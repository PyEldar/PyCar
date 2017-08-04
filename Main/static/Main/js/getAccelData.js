var x = 0, y = 0,
vx = 0, vy = 0,
ax = 0, ay = 0;   
	


if (window.DeviceMotionEvent != undefined) {
	window.ondevicemotion = function(e) {
		ax = event.accelerationIncludingGravity.x * 5;
		ay = event.accelerationIncludingGravity.y * 5;
		
		document.getElementById("val").value = e.accelerationIncludingGravity.y;
		
	}
	
} 

