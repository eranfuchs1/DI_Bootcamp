regex = /^[0-9]{5}$/g
zipcode = prompt("enter your zip code");
if (regex.test(zipcode)) {
	console.log('success');
}
else {
	console.log('error');
}
