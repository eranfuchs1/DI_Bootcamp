let isOmnipresent = (arr, elem) => {
	let found = false;
	for (e of arr)
	{
		if (elem == e)
		{
			found = true;
			break;
		}
	}
	if (!found) {
		return false;
	}
	for (e of arr)
	{
		if (typeof(e) === typeof([]))
		{
			if (!isOmnipresent(e, elem))
			{
				return false;
			}
		}
	}
	return true;
};

console.log(isOmnipresent([1,2,3,5,[3,1,[4,1,[5,4],5],5],[5,1],[1,5]], 5));
