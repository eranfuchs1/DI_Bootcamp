let isDivisble = (divisor=500) => {
	let sum = 0;
	for (let i = 0; i <= divisor; i++)
	{
		if (i%23 == 0)
		{
			sum += i;
			console.log(i);
		}
	}
	console.log(`sum: ${sum}`);
}
isDivisble(1000);
