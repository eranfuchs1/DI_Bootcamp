let unique = (arr) => {
	let obj = {};
	for (item of arr)
	{
		obj[item.toString()] = item;
	}
	let answer = [];
	for (key in obj)
	{
		answer.push(obj[key]);
	}
	return answer;
}

console.log(unique([1,2,3,3,3,3,4,5]));
