import sqlite3


#Создаем функцию, которая создает базу данных  и сохраняет ее в файл. 
#База данных содержит таблицу employees с полями id, name, middle_name, family, age,id_subdivision,mobile_phone
#База данных содержит таблицу request_support с полями id_request, id_employee,id_subdivision_support, date_request, status,date_support
#База данных содержит таблицу subdivision с полями id_subdivision, name_subdivision
#База данных содержит таблицу status с полями id_status, name_status
#База данных содержит таблицу subdivision_support с полями id_support, name_support,id_supervisor
#Таблица employees связана с таблицей subdivision по полю id
#Таблица request_support связана с таблицей employees по полю id_employee
#Таблица request_support связана с таблицей subdivision_support по полю id_subdivision_support
#Таблица request_support связана с таблицей status по полю status
#Поле id_supervisor таблицы subdivision_support связано с полем id таблицы employees

def create_db():
    conn = sqlite3.connect('support.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        middle_name TEXT,
        family TEXT,
        age INTEGER,
        id_subdivision INTEGER REFERENCES subdivision(id_subdivision),
        mobile_phone INTEGER 
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS subdivision(
        id_subdivision INTEGER PRIMARY KEY AUTOINCREMENT,
        name_subdivision TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS status(
        id_status INTEGER PRIMARY KEY AUTOINCREMENT,
        name_status TEXT
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS subdivision_support(
        id_support INTEGER PRIMARY KEY AUTOINCREMENT,
        name_support TEXT,
        id_supervisor INTEGER REFERENCES employees(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS request_support(
        id_request INTEGER PRIMARY KEY AUTOINCREMENT,
        id_employee INTEGER REFERENCES employees(id),
        id_subdivision_support INTEGER REFERENCES subdivision_support(id_support),
        description TEXT,
        date_request DATE,
        status INTEGER REFERENCES status(id_status),
        date_support DATE 
        )""")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()