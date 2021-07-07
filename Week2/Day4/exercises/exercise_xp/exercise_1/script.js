infoAboutMe = () => console.log("Hi I'm Eran, and I'm 25 years old.");
infoAboutMe();

infoAboutPerson = (personName, personAge, personFavoriteColor) => console.log(`Hi I'm ${personName}, I'm ${personAge} and my favorite color is ${personFavoriteColor}`);
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");
infoAboutPerson = (personName, personAge, personFavoriteColor, personHobbies) => {
	console.log(`Hi I'm ${personName}, I'm ${personAge} and my favorite color is ${personFavoriteColor}.\nmy hobbies are:`);
	for (hobby of personHobbies)
	{
		console.log(hobby);
	}
};
infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])
