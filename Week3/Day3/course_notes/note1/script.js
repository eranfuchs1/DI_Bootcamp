let x = 0;
setInterval(() => {
	let screenWidth = window.screen.availWidth;
	document.getElementById("box").style.left = `${x < screenWidth - 40? x++ : screenWidth - 40}px`;
}, 5);
