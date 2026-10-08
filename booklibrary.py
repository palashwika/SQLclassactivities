import sqlite3
import pandas as pd

# ---- PART 1: What is a JOIN - Build and Explore the Tables ----

conn=sqlite3.connect(':memory:')

conn.execute("""CREATE TABLE author (
    author_id   INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL UNIQUE
)""")

conn.execute("""CREATE TABLE book (
    book_id     INTEGER PRIMARY KEY,
    book_title  TEXT NOT NULL,
    author_id   INTEGER
)""")

conn.executemany("INSERT INTO author VALUES (?,?)", [
    (1, 'Roald Dahl'),
    (2, 'JK Rowling'),
    (3, 'Rick Riordan'),
    (4, 'Jeff Kinney'),
    (5, 'Dav Pilkey'),
    (6, 'Lemony Snicket'),

])

conn.executemany("INSERT INTO book VALUES (?, ?, ?)", [

(1, 'Charlie and the Chocolate Factory', 1),

(2, 'James and the Giant Peach', 1),

(3, 'Harry Potter and the Philosophers Stone', 2),

(4, 'Harry Potter and the Chamber of Secrets', 2),

(5, 'The Lightning Thief', 3),

(6, 'The Sea of Monsters', 3),

(7, 'Diary of a Wimpy Kid', 4),

])

conn.commit()


authors = pd.read_sql("SELECT * FROM author", conn)

books = pd.read_sql("SELECT * FROM book", conn)

print("Author table:")

print(authors)

print()

print("Book table:")

print(books)

print()


#INNER JOIN:**

#Write a SQL query to display the author name along with the title of each book they have written.
#authors = pd.read_sql("SELECT author.author_name, book.book_title FROM book INNER JOIN author ON book.author_id = author.author_id;", conn)
#print(authors)





#2. **LEFT JOIN:**

#Write a SQL query to display **all authors** along with their book titles. If an author has no book, their book title should show as `NULL`.
all_authors = ("SELECT author.author_name, book.book_title FROM author LEFT JOIN ON book.author_id = author.author_id",conn)
print(all_authors)



#3. **CROSS JOIN:**

#Write a SQL query to pair the **first 2 authors** with **every book** in the `book` table.
two_authors = all_authors = ("SELECT ",conn)

#4. **UNION:**

#Write a SQL query to combine all author names and book titles into a single `name` column, with another column showing whether each row is an `"Author"` or a `"Book"`.


