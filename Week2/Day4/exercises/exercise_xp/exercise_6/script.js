let changeEnough = (change, amt) => {
	let sum = change[0] * 0.25;
	sum += change[1] * 0.1;
	sum += change[2] * 0.05;
	sum += change[3] * 0.01;
	let answer;
	sum >= amt? answer = true : answer = false;
	return answer;
};
console.log(changeEnough([2, 100, 0, 0], 14.11));
