let userCart = {
  username: "John",
  password: 1234,
  isUserSignedIn: true,
  cart: {
    apple: 2,
    banana: 1,
    pear: 5,
  },
  prices: {
    apple: 0.5,
    banana: 0.8,
    pear: 0.2,
  },
};
// userCart["username"] = "Josh";
// let taxes = 1.17;
// for (key in userCart["prices"]) {
//   userCart["prices"][key] *= taxes;
// }
// console.log(userCart);
// console.log(userCart["cart"]["pear"]);
// console.log(userCart["prices"]["pear"]);
// let numberPear = userCart["cart"]["pear"];
// let pricePerPear = userCart["prices"]["pear"];
// let totalPricePear = numberPear * pricePerPear;
// console.log(
//   `The pears cost ${totalPricePear} shekels to ${userCart["username"]}`
// );
// let fruits = [];

// for (key in userCart["cart"]) fruits.push(key);
// let choice = prompt(`pick a fruit: ${fruits}`).toLowerCase();

// console.log(userCart["prices"][choice]);

userCart["signedIn"] = true;

if (userCart["signedIn"]) {
  alert(`username:${userCart["username"]}\npassword:${userCart["password"]}`);
} else {
  alert("you need to sign in");
}

if (userCart["username"] == "John" && userCart["password"] === 1234) {
  alert("you're signed in");
} else if (userCart["username"] == "John" || userCart["password"] === 1234) {
  alert("one credential is wrong");
} else {
  alert("you need to sign in");
}
