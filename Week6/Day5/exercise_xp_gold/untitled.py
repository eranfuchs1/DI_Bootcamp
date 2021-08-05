import psycopg2
from getpass import getpass
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = ''
DATABASE = 'credentials'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE)

cursor = connection.cursor()
logged_in = []

def username_exists(username):
    try:
        cursor.execute(f"select username, password from users where username = '{username}'")
        if cursor.fetchone():
            return True
    except:
        return False
    return False

def get_username_password(username):
    try:
        cursor.execute(f"select password from users where username = '{username}'")
        result = cursor.fetchone()
        if result:
            return result[0]
    except:
        return ''
    return ''

def insert_new_user(username, password):
    try:
        cursor.execute(f"insert into users(username, password) values('{username}', '{password}')")
        connection.commit()
        return True
    except:
        return False


while True:
    user_input = input()
    if user_input == 'exit':
        exit(0)
    elif user_input == 'login':
        username = input('username: ')
        password = getpass('password: ')
        if username_exists(username):
            if get_username_password(username) == password:
                print('you are now logged in')
                logged_in.append(username)
        elif input('username doesn\'t exist, would you like to sign up? (Y/n)').lower() == 'y':
            if input('use given username? (Y/n)').lower() == 'y':
                pass
            else:
                username = input('enter new username: ')
            if input('use given password? (Y/n)').lower() == 'y':
                insert_new_user(username, password)
            else:
                insert_new_user(username, getpass('enter new password: '))
            logged_in.append(username)
connection.close()
