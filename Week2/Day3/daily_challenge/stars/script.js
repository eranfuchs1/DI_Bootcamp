let count = 8;
let str = '';

for (let i = 0; i < count; i++)
{
	str += '*';
	console.log(str);
}
/* nested loop */
for (let i = 0; i < count; i++)
{
	let str = '*'
	for (let j = 0; j < i; j++)
	{
		str += '*';
	}
	console.log(str);
}

