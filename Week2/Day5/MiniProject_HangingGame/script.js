let word = '';
while (word.length < 8)
{
	word = prompt('player 1: enter a word (minimum of 8 characters)');
}
let guesses = '';
let correct = true;
for (let i = 0; i < 10; i++)
{
	let c = '';
	let str = '';
	while (!c.match(/^\w{1}$/) || (guesses.length > 0 ? c.match(RegExp(guesses.replace(/\|$/, ''))) : false))
	{
		if (guesses.length > 0 && c.match(/^\w{1}$/))
		{
			if (c.match(RegExp(guesses.replace(/\|$/, ''))))
			{
				c = prompt(`player 2: you already guessed ${c}! try again`);
				continue;
			}
		}
		c = prompt('player 2: guess and enter a single character');
	}
	guesses += `${c}`;
	console.clear();
	console.log(guesses);
	correct = true;
	for (letter of word)
	{
		if (letter.match(RegExp(guesses)))
		{
			str += letter;
		}
		else {
			str += '*';
			correct = false;
		}
	}
	guesses += `|`;
	console.log(str);
	if (correct)
	{
		console.log('you win!');
		break;
	}
}
if (!correct)
{
	console.log('you lose!');
}
