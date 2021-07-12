let form = document.forms[0];
form.addEventListener('submit', (event) => {
	let vol_elem;
	let radius = '';
	for (elem of event.target.elements)
	{
		if (elem.name == 'radius')
		{
			radius = elem.value;
		}
		else if (elem.name == 'volume')
		{
			vol_elem = elem;
		}
	}
	if (radius.match(/[0-9]{1,}|[0-9]{1,}\.[0-9]{1,}/))
	{
		vol_elem.value = (4/3) * Math.PI * Math.pow(radius, 3);
	}

	event.preventDefault();
});
