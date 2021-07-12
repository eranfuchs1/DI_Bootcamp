function getBold_items() {
	let p = document.querySelector('p');
	let allBold = [];
	for (let elem of p.children)
	{
		if (elem.tagName == 'STRONG')
		{
			allBold.push(elem);
		}
	}
	return allBold;
}

function highlight(color='blue')
{
	allBold = getBold_items();
	for (let elem of allBold)
	{
		elem.style.color = color;
	}
}

function return_normal()
{
	highlight('black');
}

let p = document.querySelector('p');
p.addEventListener('mouseover', (event) => {
	highlight();
});
p.addEventListener('mouseout', (event) => {
	return_normal();
});
