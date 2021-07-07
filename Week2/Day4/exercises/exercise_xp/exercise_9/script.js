let isValidNumber = (input) {
	return /^[0-9]{1,}$/g.test(input);
}

let hotelCost = () => {
	let nights = prompt('how many nights are you planning to stay?');
	if (!isValidNumber(nights))
	{
		return hotelCost();
	}
	return parseInt(nights) * 140;
}

console.log(hotelCost());


let planeRideCost = () => {
	let dest = prompt("what's your destination?");
	if (!isValidNumber(dest))
	{
		return planeRideCost();
	}
	let price = 0;
	price += {'London':183,'Paris':220}[dest];
	if (price == 0)
	{
		price = 300;
	}
	return price;
}

let rentalCarCost = () => {
	let days = prompt('how many days will you rent the car for?');
	if (!isValidNumber(days))
	{
		return rentalCarCost();
	}
	days = parseInt(days);
	if (days > 10)
	{
		return days * 40 * 0.95;
	}
	return days * 40;
}

let totalVacationCost = () => {
	return hotelCost() + planeRideCost() + rentalCarCost();
}
totalVacationCost();


