from menu import MenuItem

def load_manager():
    pass

def show_restaurant_menu():
    for item in MenuItem.all():
        print(f'{item.name}:\t{item.price}$')


def add_item_to_menu():
    name = input('item name: ')
    price = input('item price: ')
    item = MenuItem(name, price)
    if item.save():
        print('item was added successfully.')
    else:
        print('error')


def remove_item_from_menu():
    name = input('item\'s name to remove: ')
    item = MenuItem.get_item_by_name(name)
    if item.delete():
        print('deleted successfully')
    else:
        print('error')


def show_user_menu():
    selection = input('''\tMENU
(a) Add an item
(d) Delete an item
(v) View the menu
(q) Exit
''')
    if 'a' in selection:
        add_item_to_menu()
    elif 'd' in selection:
        remove_item_from_menu()
    elif 'v' in selection:
        show_restaurant_menu()
    elif 'q' in selection:
        show_restaurant_menu()
        return
    show_user_menu()


if __name__ == '__main__':
    show_user_menu()
