import sqlite3
import faker
import os 
from create_db import create_db

def create_data():
    cn = '+7'
    on = ('922','986','910','905')
    fake = faker.Faker('ru_RU')
    name = fake.name()
    age = fake.random_int(min=18, max=75)    
    phone = cn + on[fake.random_int(min=0, max=3)] + str(fake.random_int(min=1000000, max=9999999))
    return (name, age, phone)

#Проврека, есть ли файл в каталоге
if os.path.exists('support.db'):
    conn = sqlite3.connect('support.db')
    cursor = conn.cursor()
    for i in range(100):
        name, age, phone = create_data()
        cursor.execute(f"""INSERT INTO employees(name, age, mobile_phone) VALUES('{name}', {age}, '{phone}')""")
    conn.commit()
    conn.close()
else:
    print('Файл support.db не найден')
    create_db()
    conn = sqlite3.connect('support.db')
    cursor = conn.cursor()
    for i in range(100):
        name, age, phone = create_data()
        cursor.execute(f"""INSERT INTO employees(name, age, mobile_phone) VALUES('{name}', {age}, '{phone}')""")
    conn.commit()
    conn.close()
