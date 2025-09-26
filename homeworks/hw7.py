import sqlite3

DB_NAME = "library.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    conn.commit()
    conn.close()
    print("Таблица 'books' созданаааа")

def insert_books():
    books = [
        ("Ерунда 1", "Неизвестный", 2020, "Фантастика", 100, 1),
        ("Ничего интересного", "Не читаю", 2019, "Фантастика", 120, 2),
        ("Просто текст", "Автор Х", 2021, "Роман", 200, 3),
        ("Зачем читать?", "Автор Y", 2018, "Фэнтези", 150, 1),
        ("Книга о книге", "Студент", 2022, "Юмор", 90, 2),
        ("Бесполезные знания", "Неизвестный", 2017, "Энциклопедия", 300, 1),
        ("Ничего не понятно", "Автор Z", 2020, "Роман", 110, 3),
        ("Учусь для галочки", "Студент", 2021, "Учебник", 250, 2),
        ("Пропустил страницу", "Автор A", 2019, "Детектив", 180, 1),
        ("Сонная книга", "Автор B", 2022, "Фантастика", 220, 2)
    ]
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()
    conn.close()
    print("Книги добавлены")

def delete_book(book_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE name = ?", (book_name,))
    conn.commit()
    conn.close()
    print(f"Книга '{book_name}' удалена")

if __name__ == "__main__":
    create_table()
    insert_books()
    delete_book("Ерунда 1")
    delete_book("Сонная книга")