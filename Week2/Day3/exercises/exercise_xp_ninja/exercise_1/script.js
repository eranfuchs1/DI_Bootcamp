
details = {
	FullName: 'anon',
	Mass: 80,
	Height: 1.8,
	calculateBMI: function () {
		return this['Mass'] / this['Height'];
	}
};

let person1 = Object.assign({}, details);
person1['FullName'] = 'jon';
let person2 = Object.assign({}, details);
person2['FullName'] = 'doe';
person2['Mass'] = 95;
person2['Height'] = 1.85;

person1['calculateBMI']() > person2['calculateBMI']()? console.log(person1['FullName']) : console.log(person2['FullName']);
