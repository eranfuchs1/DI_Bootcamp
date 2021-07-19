basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(basket.index("Banana"))
basket.pop(basket.index("Blueberries"))
basket.append('Kiwi')
basket.insert(0,'Apples')
print(basket.count('Apples'))
del basket[0:]
print(basket)
