let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
society_name = '';
for (val of names.sort())
{
	society_name += val[0];
}
console.log(society_name);
