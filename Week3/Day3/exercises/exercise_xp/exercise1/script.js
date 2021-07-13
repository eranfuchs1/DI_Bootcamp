let x = 0;
let moveLeft = () => {
	let box = document.querySelector('#animate');
	let left = x < 350 ? x++ : x;
	box.style.left = `${left}px`;
};
let myMove = () => {
	setInterval(moveLeft, 20);
};
