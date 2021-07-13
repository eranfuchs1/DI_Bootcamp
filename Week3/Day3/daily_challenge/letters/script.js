document.querySelector('input').addEventListener('keyup', (e) => {
	e.target.value = e.target.value.split('').filter(l => l.match(/[a-zA-Z]{1}/)).join('');
});
