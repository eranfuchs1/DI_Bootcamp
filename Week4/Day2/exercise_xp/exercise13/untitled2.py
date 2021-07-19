sandwich_orders = [input('enter a sandwich: \n') for i in range(3)][::-1]
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    print(f'making your {finished_sandwiches[-1]} sandwich...')
for sandwich in finished_sandwiches:
    print(f"your {sandwich} sandwich is ready!")
