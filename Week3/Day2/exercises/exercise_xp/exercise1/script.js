let elem = document.getElementsByTagName('article')[0];

let p = elem.querySelectorAll('p');
p = p[p.length - 1];
p.remove();
let h2 = elem.querySelector('h2');
h2.addEventListener('click', (event) => {
	event.target.style = 'background-color: red';
});
let h1 = elem.querySelector('h1');
h1.style = `font-size: ${Math.floor(Math.random() * 101)}px`;
let h3 = elem.querySelector('h3');
h3.addEventListener('click', (event) => {
	event.target.style.display = 'none';
});
let btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click', (event) => {
	for (let elem of document.getElementsByTagName('p'))
	{
		let nelem = document.createElement('b');
		elem.parentNode.appendChild(nelem);
		elem.parentNode.insertBefore(nelem, elem);
		nelem.appendChild(elem);
	}
});
let form = document.forms[0];
form.addEventListener('submit', (event) => {
	let table = document.createElement('table');
	let theader = document.createElement('tr');
	let fname = document.createElement('td');
	let lname = document.createElement('td');
	fname.innerHTML = 'first name';
	lname.innerHTML = 'last name';
	theader.appendChild(fname);
	theader.appendChild(lname);
	let row = document.createElement('tr');
	for (let elem of event.target.elements)
	{
		if (elem.value.length > 0 && elem.type == 'text')
		{
			let td = document.createElement('td');
			td.innerHTML = elem.value;
			row.appendChild(td);
		}
	}
	table.appendChild(theader);
	table.appendChild(row);
	document.querySelector('.usersAnswer').appendChild(table);
	event.preventDefault();
});
let p2 = elem.querySelectorAll('p')[1];
p2.addEventListener('mouseover', (event) => {
	event.target.style = 'color: red; transition: 0.8s;';
});
p2.addEventListener('mouseout', (event) => {
	event.target.style = 'color: black; transition: 0.8s;';
});
