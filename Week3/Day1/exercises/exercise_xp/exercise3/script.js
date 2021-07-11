document.querySelector('div').style = 'background-color:lightblue;padding: 20px;';
document.querySelector('ul').children[0].style = 'visibility: hidden;';
document.querySelector('ul').children[1].style = 'border: 1px solid black;';
document.body.style = 'font-size: 30px;';
if (document.querySelector('div').style.backgroundColor == 'lightblue')
{
	let elemArr = document.querySelector('ul').querySelectorAll('li');
	alert(`Hello ${elemArr[0].innerHTML} and ${elemArr[1].innerText}`);
}
