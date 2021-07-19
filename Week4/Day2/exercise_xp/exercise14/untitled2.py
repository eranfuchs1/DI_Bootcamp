sandwich_orders = [input('enter a sandwich: \n') for i in range(3)][::-1] + ['pastrami'] * 3
print('the deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiches.append(sandwich_orders.pop())
    if 'pastrami' in finished_sandwiches:
        exit(1)
    print(f'making your {finished_sandwiches[-1]} sandwich...')
for sandwich in finished_sandwiches:
    print(f"your {sandwich} sandwich is ready!")
