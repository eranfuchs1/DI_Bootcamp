let x;
let y;
window.addEventListener('dragover', (e) => {
	console.log(e.clientX, e.clientY);
	x = e.clientX;
	y = e.clientY;
});

let box = document.createElement('div');
box.innerHTML = `A paragraph inside a div`;
box.classList.add('box');
box.style.color = `rgb(${Math.random() * 127}, ${Math.random() * 127}, ${Math.random() * 127})`;
box.style.backgroundColor = `rgb(${126 + Math.random() * 127}, ${126 + Math.random() * 127}, ${126 + Math.random() * 127})`;
box.style.left = `0px`;
box.setAttribute('draggable', 'true');
box.addEventListener('dragend', (e) => {
	e.target.style.left = `${x}px`;
	e.target.style.top = `${y}px`;
});
box.addEventListener('drag', (e) => {
	e.target.style.color = `rgb(${x % 256}, ${y % 256}, ${(x + y) % 256})`;
	e.target.style.backgroundColor = `rgb(${x % 100}, ${y % 100}, ${(x + y) % 100})`;
});
document.body.appendChild(box);
