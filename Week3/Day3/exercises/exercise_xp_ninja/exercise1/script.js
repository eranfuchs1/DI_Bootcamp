let random_rgb = () => `rgb(${Math.random() * 256}, ${Math.random() * 256}, ${Math.random() * 256})`;
let plus = document.createElement('div');
plus.style.backgroundColor = 'blue';
plus.classList.add('box');
plus.addEventListener('click', (e) => {
	let box = document.createElement('div');
	e.target.parentNode.appendChild(box);
	box.classList.add('box');
	box.classList.add('box_anim');
	box.style.backgroundColor = random_rgb();
});
document.body.querySelector('div').appendChild(plus);
