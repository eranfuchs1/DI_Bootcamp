regex = /[a|e|i|o|u]{1}/g
word = prompt('enter a word');
word = word.replaceAll(regex, 'h');
console.log(word);
