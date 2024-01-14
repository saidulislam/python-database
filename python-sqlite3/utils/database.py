from utils.database_connection import DatabaseConnection

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        # SQLite automatically makes `integer primary key` row auto-incrementing
        cursor.execute('CREATE TABLE IF NOT EXISTS books (id integer primary key, name text, author text, read integer default 0)')

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    return books

def insert_book(name: str, author: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO books (name, author) VALUES (?, ?)', (name, author))
        
def mark_book_as_read(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
        
def delete_book(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('DELETE FROM books WHERE name=?', (name,))
        
        
        