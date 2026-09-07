import sqlite3
import pandas as pd

conn = sqlite3.connect('planets.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Planet;

CREATE TABLE Planet (
    Planet_Id       INTEGER PRIMARY KEY,
    Planet_Name     TEXT,
    Planet_Type     TEXT,
    Distance_AU     REAL,
    Moons           INTEGER
);

INSERT INTO Planet VALUES
    (1, 'Mercury', 'Terrestrial', 0.39, 0),
    (2, 'Venus', 'Terrestrial', 0.72, 0),
    (3, 'Earth', 'Terrestrial', 1.00, 1),
    (4, 'Mars', 'Terrestrial', 1.52, 2),
    (5, 'Jupiter', 'Gas Giant', 5.20, 95),
    (6, 'Saturn', 'Gas Giant', 9.58, 146),
    (7, 'Uranus', 'Ice Giant', 19.19, 28),
    (8, 'Neptune', 'Ice Giant', 30.07, 16);
""")

conn.commit()

print('Database ready!')

# -- PART 2: See ALL Tables in the Database ---

tables = pd.read_sql("""
SELECT * FROM sqlite_master WHERE type='table'; """, conn)

print(tables)


# Return values from Planet Table
planet = pd.read_sql(""" SELECT * FROM Planet;""", conn)
print(planet)

#Fetch ONLY Planet_Name and Planet_Type
p1 = pd.read_sql(""" SELECT Planet_Name, Planet_Type FROM Planet; """, conn)
print(p1)

#Fetch Planet_Name and Moons
p2 = pd.read_sql("""SELECT Planet_Name, Moons FROM Planet; """, conn)
print(p2)



#Part 4: Filter Rows with WHERE

#Final all terrestrial planets

terrestrial = pd.read_sql("""SELECT Planet_Name, Planet_Type FROM Planet WHERE Planet_Type = "Terrestrial";  """, conn)

print(terrestrial)

#Find planets that have more than 20 moons

moons = pd.read_sql("""SELECT Planet_Name, Planet_Type, Moons FROM Planet WHERE Moons>20;""", conn)
print(moons)


#Find gas giants that have more than 100 moons

gasgiant_moons = pd.read_sql("""SELECT Planet_Name, Planet_Type, Moons FROM Planet WHERE Moons>100 AND Planet_Type="Gas Giant";""", conn)
print(gasgiant_moons)

#Part 5: Search for a Pattern with LIKE

#Find all planets whose name begins with 'M'

m_planets = pd.read_sql("""SELECT Planet_Name FROM Planet WHERE Planet_Name LIKE "m%"; """, conn)
print(m_planets)

#Find all planets whose name wnds with 's'
s_planets = pd.read_sql("""SELECT Planet_Name FROM Planet WHERE Planet_Name LIKE "%s"; """, conn)
print(s_planets)

#Find the Smallest and Largest values
minimum = pd.read_sql("""SELECT Planet_Name, Planet_Type, min(Distance_AU) FROM Planet ;""", conn)
print(minimum)
maximum = pd.read_sql("""SELECT Planet_Name, Planet_Type, max(Distance_AU) FROM Planet ;""", conn)
print(maximum)

#Find the smallest and largest number of moons

small = pd.read_sql("""SELECT Planet_Name, Planet_Type, min(Moons) FROM Planet ;""", conn)
print(small)
large = pd.read_sql("""SELECT Planet_Name, Planet_Type, max(Moons) FROM Planet ;""", conn)
print(large)



