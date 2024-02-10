
import sqlite3
conn = sqlite3.connect('car.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        car_title TEXT NOT NULL CHECK(car_title != ''),
        price FLOAT DEFAULT 0.0 CHECK(price >= 0 AND price <= 9999999999),
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

conn.commit()

def add_car(car_title, price, quantity):
    cursor.execute('''
        INSERT INTO cars_list (car_title, price, quantity) VALUES (?, ?, ?)
    ''', (car_title, price, quantity))
    conn.commit()
    print(f"Машина '{car_title}' успешно добавлена в базу данных.")

def delete_car_by_id(car_id):
    cursor.execute('DELETE FROM cars_list WHERE id = ?', (car_id,))
    conn.commit()
    print(f"Машина с id {car_id} успешно удалена из базы данных.")


def select_cars_below_100():
    cursor.execute('SELECT * FROM cars_list WHERE price < 100')
    cars = cursor.fetchall()
    if not cars:
        print("Нет машин дешевле 100$.")
    else:
        print("Машины дешевле 100$: ")
        for car in cars:
            print(f"ID: {car[0]}, Название: {car[1]}, Цена: {car[2]}, Количество: {car[3]}")

add_car('Toyota Camry', 89.99, 5)
add_car('Honda Accord', 105.5, 3)
add_car('Ford Mustang', 75.0, 8)

delete_car_by_id(2)

select_cars_below_100()
conn.close()
