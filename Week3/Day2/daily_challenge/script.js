let btn = document.body.querySelector('button');
btn.addEventListener('click', (event) => {
	let inps = Array.from(document.body.querySelectorAll('input')).filter(elem => elem.type == 'text' && elem.value != '');
	let noun = inps.filter(elem => elem.id == 'noun')[0].value;
	let adjective = inps.filter(elem => elem.id == 'adjective')[0].value;
	let name = inps.filter(elem => elem.id == 'person')[0].value;
	let verb = inps.filter(elem => elem.id == 'verb')[0].value;
	let place = inps.filter(elem => elem.id == 'place')[0].value;
	let story_elem = document.querySelector('#story');
	story_elem.innerHTML = `Long time ago, in ${place}, there was a person named ${name}.`;
	story_elem.innerHTML += ` ${name} had a ${noun}, and every time ${name} ${verb} with the ${noun},`;
	story_elem.innerHTML += ` the ${noun} broke and exploded. After the explosion the ${noun} looked ${adjective}.`;
});
