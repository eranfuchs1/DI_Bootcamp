let checkNumber = () => {
	for (let i = 0; i <= 100; i++)
	{
		if (i%2 == 0)
		{
			console.log(`the number ${i} is even`);
		}
		else {
			console.log(`the number ${i} is odd`);
		}
	}
};
checkNumber();
