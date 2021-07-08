let biggestNumberInArray = (arr) => {
	let num = 0;
	for (item of arr)
	{
		if (num < item)
		{
			num = item;
		}
	}
	return num;
}

console.log(biggestNumberInArray(['a', 3, 4, 2]));
