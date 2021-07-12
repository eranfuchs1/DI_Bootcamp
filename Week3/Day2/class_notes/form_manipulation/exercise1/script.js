function getvalue(event) {
	for (elem of event.target.elements)
	{
		if (elem.type == 'text')
		{
			console.log(elem.value);
		}
	}
	event.preventDefault();
}
