let sentence = prompt('enter words seperated by commas');
regex = /[\s|,]*[[\s]*,{1,}[\s]*]*[[,]*[\s]*[,]*]*[\s|,]*/g;
let arr = sentence.split(regex);

let max_length = 0;

let symbol = '*';
for (l of arr)
{
	if (max_length < l.length) {
		max_length = l.length;
	}
}

for (let i = 0; i < arr.length + 2; i++)
{
	let line = '';
	if (i == 0 || i == arr.length + 1)
	{
		for (let j = 0; j < max_length + 2; j++)
		{
			line += symbol; 
		}
	}
	else
	{
		line += '*';
		line += arr[i - 1];
		for (let j = line.length; j < max_length + 1; j++)
		{
			line += ' ';
		}
		line += '*';
	}
	console.log(line);
}
