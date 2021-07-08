let lyrics = (number) => {
	let bottles = number;
	let sub = 0;
	while (bottles > 0)
	{
		console.log(`${bottles} bottles of beer on the wall`);
		console.log(`${bottles} bottles of beer on the wall`);
		console.log(`${bottles} bottles of beer`);
		sub = bottles <= sub ? bottles : ++sub;
		if (sub > 1)
		{
			console.log(`Take ${sub} down, pass them around`);
		}
		else
		{
			console.log(`Take ${sub} down, pass it around`);
		}
		bottles -= sub;
	}
	console.log(`no more bottles of beer`);
}

lyrics(99);
