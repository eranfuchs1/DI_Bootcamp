let mdown = false;
let color = '';
document.body.addEventListener('mousedown',(e) => {
	mdown = true;
});
document.body.addEventListener('mouseup',(e) => {
	mdown = false;
});

for (let i of Array(8100).keys())
{
	let fclick = (e) => {
		e.target.style.backgroundColor = color;
	}
	let fmove = (e) => {
		if (mdown)
		{
			fclick(e);
		}
	}
	let box = document.createElement('div');
	box.setAttribute('draggable', 'false');
	box.classList.add('box');
	box.addEventListener('click', fclick);
	box.addEventListener('mouseenter', fmove);
	box.addEventListener('mouseleave', fmove);
	document.querySelector('.container').appendChild(box);
}
let colors = [
	'blue',
	'red',
	'grey',
	'pink',
	'lightblue',
	'lime',
	'orange',
	'brown',
	'black',
	'white'
];

for (let i of Array(10).keys())
{
	let fclick = (e) => {
		color = e.target.style.backgroundColor;
	}
	let box = document.createElement('div');
	box.setAttribute('draggable', 'false');
	box.classList.add(`color${i}`);
	box.addEventListener('click', fclick);
	box.style.backgroundColor = `${colors[i]}`;
	document.querySelector('.palette').appendChild(box);
}

document.querySelector('button').addEventListener('click', (e) => {
	for (div of document.querySelectorAll('.box'))
	{
		div.style.backgroundColor = 'white';
	}
});
