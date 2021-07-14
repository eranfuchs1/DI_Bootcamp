let listTasks = [];

let addTask = () => {
	let val = document.forms[0].elements[0].value;
	if (val != '')
	{
		listTasks.push({'task_id': listTasks.length,'text': val, 'done': false});
		let todo = document.createElement('div');
		todo.addEventListener('mouseover', (e) => {
			e.target.style.zIndex = '3';
		});
		todo.addEventListener('mouseenter', (e) => {
			e.target.style.zIndex = '3';
		});
		todo.addEventListener('mouseleave', (e) => {
			e.target.style.zIndex = '2';
		});
		todo.setAttribute('data-task-id', `${listTasks[listTasks.length - 1]['task_id']}`);
		let p = document.createElement('p');
		p.innerHTML = val;
		let input = document.createElement('input');
		input.setAttribute('type', 'checkbox');
		input.addEventListener('click', (e) => {
			listTasks[parseInt(e.target.parentNode.getAttribute('data-task-id'))]['done'] = e.target.checked;
			if (e.target.checked)
			{
				e.target.parentNode.style.backgroundColor = 'lightpink';
				let del = document.createElement('del');
				del.appendChild(e.target.parentNode.children[0]);
				e.target.parentNode.appendChild(del);
				e.target.parentNode.insertBefore(del, e.target.parentNode.children[0]);
			}
			else {
				e.target.parentNode.setAttribute('class', '');
				e.target.parentNode.style.backgroundColor = 'white';
				e.target.parentNode.appendChild(p);
				e.target.parentNode.children[0].remove();
				e.target.parentNode.insertBefore(p, e.target.parentNode.children[0]);
			}
		});
		let x = document.createElement('button');
		x.innerHTML = 'x';
		x.addEventListener('click', (e) => {
			e.target.parentNode.remove();
		})
		todo.appendChild(p);
		todo.appendChild(input);
		todo.appendChild(x);
		document.querySelector('.listTasks').appendChild(todo);
	}
};

document.forms[0].addEventListener('submit', (e) => {
	addTask();
	e.preventDefault();
});
