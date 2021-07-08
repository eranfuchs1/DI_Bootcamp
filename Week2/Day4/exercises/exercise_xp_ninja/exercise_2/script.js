let capitalize = (str) => {
	let answer = ['',''];
	for (let i = 0; i < str.length; i++)
	{
		if (i % 2 == 0) {
			answer[0] += str[i].toUpperCase();
			answer[1] += str[i].toLowerCase();
		}
		else {
			answer[1] += str[i].toUpperCase();
			answer[0] += str[i].toLowerCase();
		}
	}
	return answer;
}

console.log(capitalize("abcdef"));
