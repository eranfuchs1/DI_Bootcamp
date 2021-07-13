let x;
let y;
window.addEventListener('dragover', (e) => {
	console.log(e.clientX, e.clientY);
	x = e.clientX;
	y = e.clientY;
});

for (let i of Array(26).keys())
{
	let box = document.createElement('div');
	box.innerHTML = String.fromCharCode(97 + i);
	box.classList.add('box');
	box.style.color = `rgb(${Math.random() * 127}, ${Math.random() * 127}, ${Math.random() * 127})`;
	box.style.backgroundColor = `rgb(${126 + Math.random() * 127}, ${126 + Math.random() * 127}, ${126 + Math.random() * 127})`;
	box.style.left = `${i * 10}px`;
	box.setAttribute('draggable', 'true');
	box.addEventListener('dragend', (e) => {
		e.target.style.left = `${x}px`;
		e.target.style.top = `${y}px`;
	});
	document.body.appendChild(box);
}
