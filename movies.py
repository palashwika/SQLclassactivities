import sqlite3

import pandas as pd

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

cursor.executescript("""

DROP TABLE IF EXISTS Movie;

DROP TABLE IF EXISTS Actor;

DROP TABLE IF EXISTS Movie_Actor;

CREATE TABLE Movie (

Movie_Id INTEGER PRIMARY KEY,

Title TEXT,

Genre TEXT,

Year INTEGER,

Rating REAL,

Duration INTEGER

);

CREATE TABLE Actor (

Actor_Id INTEGER PRIMARY KEY,

Actor_Name TEXT,

Birth_Year INTEGER,

Country TEXT

);

CREATE TABLE Movie_Actor (

Movie_Id INTEGER,

Actor_Id INTEGER

);

INSERT INTO Movie VALUES

(1,'The Lion King','Animation',1994,8.5,88),

(2,'Toy Story','Animation',1995,8.3,81),

(3,'Frozen','Animation',2013,7.4,102),

(4,'Moana','Animation',2016,7.6,107),

(5,'Spider-Man','Action',2002,7.3,121),

(6,'Black Panther','Action',2018,7.3,134),

(7,'Avengers','Action',2012,8.0,143),

(8,'Matilda','Drama',1996,7.0,98),

(9,'Home Alone','Comedy',1990,7.7,103),

(10,'Elf','Comedy',2003,6.9,97),

(11,'Coco','Animation',2017,8.4,105),

(12,'Interstellar','Drama',2014,8.6,169);

INSERT INTO Actor VALUES

(1,'Tom Hanks',1956,'USA'),

(2,'Idris Elba',1972,'UK'),

(3,'Chadwick Boseman',1976,'USA'),

(4,'Scarlett Johansson',1984,'USA'),

(5,'Macaulay Culkin',1980,'USA'),

(6,'Will Smith',1968,'USA'),

(7,'Meryl Streep',1949,'USA'),

(8,'Lupita Nyongo',1983,'Kenya'),

(9,'Priyanka Chopra',1982,'India'),

(10,'Jackie Chan',1954,'China');

INSERT INTO Movie_Actor VALUES

(1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);

""")

conn.commit()

print('Database ready!')


# ---- PART 2: DISTINCT — Unique Values Only ----

# DISTINCT removes duplicate values — only one copy of each

# unique value is returned. Use it to see what the different

# values in a column are, without repeats.

# All unique genres in the Movie table

genres = pd.read_sql("""SELECT DISTINCT(Genre) FROM Movie;""", conn)
print(genres)

# All unique countries the actors come from

# ---- PART 3: ORDER BY — Sorting Results ----

# ORDER BY sorts the result by a chosen column.

# Default order is ascending — smallest or earliest first.

# Add DESC to flip it — largest or latest first.

# All movies sorted by Rating — highest rated first

rating = pd.read_sql("""SELECT Rating FROM Movie ORDER BY Rating DESC;""", conn)
print(rating)

# All movies sorted by Year — oldest first
year = pd.read_sql("""SELECT Year FROM Movie ORDER BY Year ASC;""", conn)
print(year)

# Actors sorted by Birth_Year — youngest first
birth = pd.read_sql("""SELECT Birth_Year FROM Actor ORDER BY Birth_Year DESC;""", conn)
print(birth)



# ---- PART 4: COUNT and SUM ----

# COUNT(column) returns the number of rows that match.

# SUM(column) returns the total of all values in a number column.

# Combine with WHERE to focus on specific rows.

# Total number of Action movies in the database

total_action = pd.read_sql("""SELECT SUM(Genre) AS total_action FROM Movie WHERE Genre="Action";""", conn)
print(total_action)

# Total screen time (Duration) of all Animation movies

total_st = pd.read_sql("""SELECT SUM(Duration) AS total_screentime FROM Movie WHERE Genre="Animation";""", conn)
print(total_st)



# ---- PART 5: AVG — Finding the Average ---- 

# AVG(column) calculates the mean of all values in a column.

# Use WHERE to average only rows that match a condition.

# Average rating of all movies in the database
avg_rating = pd.read_sql("""SELECT AVG(Rating) AS average_rating FROM Movie;""", conn )
print(avg_rating)

# Average duration of Action movies only
avg_duration = pd.read_sql("""SELECT AVG(Duration) AS average_duration FROM Movie WHERE Genre="Action";""", conn )
print(avg_duration)

# ---- PART 6: GROUP BY — Summarising by Category ----

# GROUP BY splits rows into groups by the values in one column.

# An aggregate function (COUNT, AVG, SUM) runs separately

# for each group — one result row per group.

# Count of movies in each genre
count_movies = pd.read_sql("""SELECT Genre, COUNT(Movie_Id) FROM Movie GROUP BY Genre;""", conn )
print(count_movies)

# Average rating per genre — sorted best genre first
average_pergenre = pd.read_sql("""SELECT Genre, AVG(Genre) FROM Movie GROUP BY Genre;""", conn )
print(average_pergenre)

conn.close()

