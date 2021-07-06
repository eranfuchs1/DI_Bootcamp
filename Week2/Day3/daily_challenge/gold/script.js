const numbers = [5,0,9,1,7,4,2,6,3,8];
let sorted_numbers = numbers;
for (let i = 0; i < sorted_numbers.length; i++)
{
	for (let j = 0; j < (sorted_numbers.length - 1) - i; j++)
	{
		if (sorted_numbers[j] > sorted_numbers[j + 1])
		{
			let local = sorted_numbers[j];
			sorted_numbers[j] = sorted_numbers[j + 1];
			sorted_numbers[j + 1] = local;
		}
	}
}
console.log(sorted_numbers.toString());

/* descending sort */
/* (always after working the above ascending sort, for standalone look below) */

for (let i = 0; i < sorted_numbers.length / 2; i++)
{
	let local = sorted_numbers[i];
	sorted_numbers[i] = sorted_numbers[(sorted_numbers.length - 1) - i];
	sorted_numbers[(sorted_numbers.length - 1) - i] = local;
}
console.log(sorted_numbers.toString());
/* standalone descending sort */
sorted_numbers = numbers;
for (let i = 0; i < sorted_numbers.length; i++)
{
	for (let j = 0; j < (sorted_numbers.length - 1) - i; j++)
	{
		if (sorted_numbers[j] < sorted_numbers[j + 1])
		{
			let local = sorted_numbers[j];
			sorted_numbers[j] = sorted_numbers[j + 1];
			sorted_numbers[j + 1] = local;
		}
	}
}
console.log(sorted_numbers.toString());
