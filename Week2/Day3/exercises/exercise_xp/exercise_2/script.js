let people = ["Greg", "Mary", "Devon", "James"];
people.splice(people.indexOf('Greg'), 1);
console.log(people);

people.splice(people.indexOf('James'), 1, 'Jason');
console.log(people);

people.push('Eran');
console.log(people);

people = ["Greg", "Mary", "Devon", "James"];
people.push('Eran');

let cpy = [];
while (people.length > 0) {
	if (!(people[0] == 'Mary' || people[0] == 'Eran')) {
		cpy = cpy.concat(people.splice(0,1));
	}
	else {
		people.splice(0,1);
	}
}
console.log(cpy);

people = ["Greg", "Mary", "Devon", "James"];
console.log(people.indexOf('Mary'));
console.log(people.indexOf('Foo'));
last = people[people.length - 1];

