let div = document.querySelector('div');
let h2 = document.createElement('h2');
h2.innerHTML = 'Loading';
document.body.appendChild(h2);
let i = 0;
setInterval(() => {
	if (i > 360)
	{
		if (i < 10)
		{
			h2.innerHTML = 'Loading';
		}
		else if (i < 50)
		{
			h2.innerHTML = 'Loading.';
		}
		else if (i < 150)
		{
			h2.innerHTML = 'Loading..';
		}
		else if (i < 200)
		{
			h2.innerHTML = 'Loading...';
		}
		i = 0.0;
	}
	div.style.transform = `rotate(${i}deg)`;
	i += 0.9
}, 1);
