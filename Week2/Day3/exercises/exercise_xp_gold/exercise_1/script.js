let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
            "1": 3,
            "2": 4,
            "3": 9,
            "4": 2,
        },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
            "Sarah": [3, 990],
            "Dan":  [4, 1000],
            "David": [1, 500],
        },
};
console.log(building['numberLevels']);
console.log(building['numberOfAptByLevel']['1'], building['numberOfAptByLevel']['3']);
console.log(building['numberOfRoomsAndRent'][building['nameOfTenants'][1]][0]);
if (building['numberOfRoomsAndRent']['Sarah'][1] + building['numberOfRoomsAndRent']['David'][1] > building['numberOfRoomsAndRent']['Dan'][1])
{
	building['numberOfRoomsAndRent']['Dan'][1] *= 6;
}
console.log(building['numberOfRoomsAndRent']['Dan'][1]);
