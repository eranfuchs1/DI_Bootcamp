let sentence = 'The movie is not that bad, I like it';
let wordNot = sentence.indexOf('not');
let wordBad = sentence.indexOf('bad');
if (wordBad > wordNot)
{
	sentence = sentence.replaceAll(/not.*bad/g, 'good');
}
console.log(sentence);
