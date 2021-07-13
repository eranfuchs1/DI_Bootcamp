let count = 0;
let color_count = 0;

document.querySelector('body').addEventListener('mousemove', (e) => {
	/*if (count++ % 4 != 0)
	{
		return;
	}*/
	let div = document.createElement('div');
	div.style.left = `${e.clientX}px`;
	div.style.top = `${e.clientY}px`;
	if (color_count++ % 2 == 0)
	{
		div.classList.add('blue');
	}
	else
	{
		div.classList.add('yellow');
	}
	document.body.appendChild(div);
	setTimeout(() => {
		div.remove();
	}, 2000);
});
