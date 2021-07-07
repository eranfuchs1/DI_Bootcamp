let calculateTip = (bill) => {
	if (bill < 50)
	{
		return bill * 0.2;
	}
	else if (bill > 50 && bill < 200)
	{
		return bill * 0.15;
	}
	else {
		return bill * 0.1;
	}
}


let bill = prompt('write your bill');
let tip = calculateTip(bill);
console.log(`the tip amount is ${tip}`);
console.log(`the total bill amount is ${tip + bill}`);
