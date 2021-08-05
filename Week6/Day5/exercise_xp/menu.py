import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = ''
DATABASE = 'restaurant'


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def save(self):
        try:
            with psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE) as connection:
                cursor = connection.cursor()
                cursor.execute(f"insert into items(item_name, item_price) values('{self.name}', {self.price})")
                connection.commit()
                return True
        except:
            return False
    def update(self, name, price):
        try:
            with psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE) as connection:
                cursor = connection.cursor()
                cursor.execute(f"update items set item_name='{name}', item_price={price} where name='{self.name}'")
                connection.commit()
                self.name = name
                self.price = price
                return True
        except:
            return False
    def delete(self):
        try:
            with psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE) as connection:
                cursor = connection.cursor()
                cursor.execute(f"delete from items where item_name='{self.name}'")
                connection.commit()
                return True
        except:
            return False
    @classmethod
    def get_item_by_name(cls, name):
        with psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE) as connection:
            cursor = connection.cursor()
            cursor.execute(f"select item_name, item_price from items where item_name='{name}'")
            result = cursor.fetchone()
            if result:
                return cls(result[0], result[1])
    @classmethod
    def all(cls):
        with psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE) as connection:
            cursor = connection.cursor()
            cursor.execute(f"select item_name, item_price from items")
            results = cursor.fetchall()
            return [cls(result[0], result[1]) for result in results]
