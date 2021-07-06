let colors = ['red', 'green', 'blue'];
let suffix_arr = ['st', 'nd', 'rd'];


for (let id of colors.keys()) {
	let color = colors[id];
	let suffix = suffix_arr[id];
	console.log(`my ${id+1}${suffix} choice is ${color}`);
}
