my_fav_numbers = {1,2,3}
my_fav_numbers.add(4)
my_fav_numbers.add(5)
my_fav_numbers.remove(5)
friend_fav_numbers = {4,5,6}
our_fav_numbers = set()
for num in friend_fav_numbers:
    our_fav_numbers.add(num)

for num in my_fav_numbers:
    our_fav_numbers.add(num)
print(our_fav_numbers)
