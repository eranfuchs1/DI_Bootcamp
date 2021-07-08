let swapCase = (word) => {
	let answer = ''
	for (c of word) {
		if (/[a-z]/.test(c))
		{
			answer += c.toUpperCase();
		}
		else if (/[A-Z]/.test(c))
		{
			answer += c.toLowerCase();
		}
	}
	return answer;
};
console.log(swapCase('AbCdE'));
