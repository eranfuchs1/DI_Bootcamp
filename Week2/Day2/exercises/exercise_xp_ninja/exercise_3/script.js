regex = /[a|e|i|o|u]{1}/g
word = prompt('enter a word');
console.log(word.replaceAll(regex, ''));
console.log(word.replaceAll(regex, 'h'));
