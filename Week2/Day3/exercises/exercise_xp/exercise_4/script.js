let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let name = prompt('enter your name');
if (name in guestList)
{
	console.log(`Hi, I'm ${name} from ${guestList[name]}.`);
}
else {
	console.log(`Hi, I'm a guest.`);
}
