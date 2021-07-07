checkDriverAge = (age=prompt('Enter your age')) => {
	if (age == 18)
	{
		console.log('Congratulations on your first year of driving. Enjoy the ride');
	}
	else if (age > 18)
	{
		console.log('You are old enough to drive, Powering On. Enjoy the ride');
	}
	else
	{
		console.log('Sorry, you are too young to drive this car. Powering off');
	}
}
checkDriverAge();
checkDriverAge(18);
