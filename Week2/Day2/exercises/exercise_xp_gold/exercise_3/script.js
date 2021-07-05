let verb = prompt('enter a verb');
if (verb.length > 2 && verb.search(/ing$/) == -1) {
	verb += 'ing';
}
else if (verb.length > 2) {
	verb += 'ly';
}
console.log(verb);
