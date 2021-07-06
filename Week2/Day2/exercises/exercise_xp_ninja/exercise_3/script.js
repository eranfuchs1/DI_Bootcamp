regex = /[a|e|i|o|u]/g
word = prompt('enter a word');
console.log(word.replaceAll(regex, ''));
console.log(word.replaceAll(regex, 'h'));
