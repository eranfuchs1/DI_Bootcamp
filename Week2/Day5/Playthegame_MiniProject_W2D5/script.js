let test = (userNumber,computerNumber) => {
	if (userNumber == computerNumber)
	{
		alert('WINNER');
		return true;
	}
	else if (userNumber < computerNumber)
	{
		alert('your number is too small');
	}
	else {
		alert('your number is too big');
	}
	return false;
}

let playTheGame = () => {
	if (!confirm('Do you want to play the game?')) {
		console.log('Goodbye.');
		return;
	}
	let numberStr = '';
	let number = parseInt(numberStr);
	let randomNumber = Math.ceil(Math.random() * 10);
	for (let i = 0; i < 3; i++)
	{
		numberStr = '';
		while (!numberStr.match(/^[0-9]{1}$|^10$/))
		{
			numberStr = prompt('pick a number between 0 and 10');
		}
		number = parseInt(numberStr);
		if (test(number, randomNumber)){
			return;
		}
	}
	console.log('out of chances');
}

