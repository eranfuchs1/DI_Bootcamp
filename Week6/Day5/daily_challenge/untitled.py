import psycopg2
import requests
from random import shuffle

endpoint = 'https://restcountries.eu/rest/v2/all'
data = requests.get(endpoint).json()

shuffle(data)





HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = ''
DATABASE = 'countries'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE)

cursor = connection.cursor()
def sanitize_sql(sql):
    return sql.replace("'", "")
for country in data[:10]:
    try:
        query = f"insert into country(country_name, capital, flag, subregion, population) values('{sanitize_sql(country['name'])}', '{sanitize_sql(country['capital'])}', '{sanitize_sql(country['flag'])}', '{sanitize_sql(country['subregion'])}', {country['population']});"
        cursor.execute(query)
        connection.commit()
    except:
        print('error...')
connection.close()
