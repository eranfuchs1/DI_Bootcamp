let age = [20,5,12,43,98,55];
let sum = 0;
for (a of age)
{
	sum += a;
}
console.log(sum);
let biggest = 0;
for (a of age)
{
	if (biggest < a)
	{
		biggest = a;
	}
}
console.log(biggest);
