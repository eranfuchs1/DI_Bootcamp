let dragArr = document.querySelectorAll('.drag');
for (drag of dragArr)
{
	drag.addEventListener('dragstart', (e) => {
		e.dataTransfer.setData('text/plain', e.target.id);
	});
}

let dropArr = document.querySelectorAll('.drop');
for (drop of dropArr)
{
	drop.addEventListener('dragenter', (e) => {
		console.log(e.dataTransfer.getData('text/plain'));
		e.target.appendChild(document.getElementById(e.dataTransfer.getData('text/plain')));
	});
}

document.body.addEventListener('dragenter', (e) => {
	console.log(e.dataTransfer.getData('text/plain'));
	e.target.appendChild(document.getElementById(e.dataTransfer.getData('text/plain')));
});
