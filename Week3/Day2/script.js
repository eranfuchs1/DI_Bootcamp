

let elem = document.getElementsByTagName('h2')[0];
elem.addEventListener('click', (obj) => {
	hello(obj, 'hello');
});


function hello(obj, msg)
{
	console.log(msg);
	console.log(obj);
}
