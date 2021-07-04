let str1 = "mix";
let str2 = "pod";
let str1slc = str1.slice(-1);
let str2slc = str2.slice(-1);
let newWord = `${str2.slice(0,2)}${str1slc} ${str1.slice(0,2)}${str2slc}`;
console.log(newWord);
