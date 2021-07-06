function findAvg(gradesList) {
	let sum = 0;
	for (grade of gradesList)
	{
		sum += grade;
	}
	let avg = sum / gradesList.length;
	console.log(`Average grade is: ${avg}`);
	return avg;
}
function avg_pass_msg(gradesList) {
	if (findAvg(gradesList) >= 65)
	{
		console.log('You passed the test.');
	}
	else
	{
		console.log('You failed the test and must repeat it.');
	}
}

avg_pass_msg([85,9,9,9,9,9,9,9]);
avg_pass_msg([85,90,49]);
