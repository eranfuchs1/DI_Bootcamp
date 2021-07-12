for (key in document.body)
{
	if (key.match(/^on.{1,}/))
	{
		document.body.addEventListener(key.replace(/^on/, ''), (event) => {
			event.target.style = `background-color: rgb(${Math.random() * 256},${Math.random() * 256},${Math.random() * 256});`;
		});
	}
}
