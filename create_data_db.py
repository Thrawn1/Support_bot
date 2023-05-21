import sqlite3
import faker
import os 


def create_db():
    conn = sqlite3.connect('support.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS subdivision(
        id_subdivision INTEGER PRIMARY KEY AUTOINCREMENT,
        name_subdivision TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        middle_name TEXT,
        family TEXT,
        age INTEGER,
        id_subdivision INTEGER,
        mobile_phone INTEGER,
        FOREIGN KEY (id_subdivision) REFERENCES subdivision(id_subdivision)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS status(
        id_status INTEGER PRIMARY KEY AUTOINCREMENT,
        name_status TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS subdivision_support(
        id_support INTEGER PRIMARY KEY AUTOINCREMENT,
        name_support TEXT,
        id_supervisor INTEGER,
        FOREIGN KEY (id_supervisor) REFERENCES employees(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS request_support(
        id_request INTEGER PRIMARY KEY AUTOINCREMENT,
        id_employee INTEGER ,
        id_subdivision_support INTEGER ,
        description TEXT,
        date_request DATE,
        status INTEGER ,
        date_support DATE,
        FOREIGN KEY (id_employee) REFERENCES employees(id),
        FOREIGN KEY (id_subdivision_support) REFERENCES subdivision_support(id_support),
        FOREIGN KEY (status) REFERENCES status(id_status) 
        )""")
    conn.commit()
    conn.close()




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
