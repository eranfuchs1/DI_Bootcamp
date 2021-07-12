function insertRow() {
	let table = document.getElementsByTagName('tbody')[0];
	let row = document.createElement('tr');
	let num = table.children.length + 1;
	console.log(table);
	let columns = [
		document.createElement('td'),
		document.createElement('td')
	];
	columns[0].innerHTML = `Row${num} cell1`;
	columns[1].innerHTML = `Row${num} cell2`;
	row.appendChild(columns[0]);
	row.appendChild(columns[1]);
	table.appendChild(row);
}
