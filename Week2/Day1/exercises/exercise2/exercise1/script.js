let me = ["my","favorite","color","is","blue"];
let str = me.toString().replaceAll('[', '').replaceAll(']','').replaceAll('"', '').replaceAll(',', ' ');
console.log(str);
