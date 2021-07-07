let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
let checkBasket = () => {
	let item = prompt('enter an item');
	if (item in amazonBasket)
	{
		console.log(`${item} is in the basket`);
	}
	else {
		console.log(`${item} is not in the basket`);
	}
}
checkBasket();
