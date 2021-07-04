let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
delete fruits[0];
fruits.sort();
fruits.push('Kiwi');
fruits.splice(fruits.indexOf('Apples'), 1);
fruits.reverse();
console.log(fruits);
