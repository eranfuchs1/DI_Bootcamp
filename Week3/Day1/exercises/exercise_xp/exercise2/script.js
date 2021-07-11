for (elem of document.querySelectorAll('li'))
{
	if (elem.innerText == 'Pete')
	{
		elem.innerText = 'Richard';
		break;
	}
}
let lastLi = document.createElement('li');
lastLi.innerText = 'Hey students';
for (elem of document.querySelectorAll('ul'))
{
	elem.children[0].innerText = 'Eran';
	elem.appendChild(lastLi);
	elem.classList.add('student_list');
}
document.querySelector('ul').classList.add('university');
document.querySelector('ul').classList.add('attendance');

for (elem of document.querySelectorAll('ul')[1].children)
{
	if (elem.innerText == 'Sarah')
	{
		elem.remove();
	}
}
