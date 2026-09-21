import sqlite3
import pandas as pd

conn = sqlite3.connect('cities.db')

conn.execute("DROP TABLE IF EXISTS City;")

conn.execute("""
CREATE TABLE City (
    City_Id     INTEGER     PRIMARY KEY,
    City_Name   TEXT        NOT NULL UNIQUE,
    Country     TEXT        NOT NULL,
    Population  INTEGER,
    Is_Capital  TEXT        DEFAULT 'No'
);
""")

conn.commit()
print("Table created successfully!")

# --- PART 2: INSERT - Adding Rows to the Table ---
#INSERT INTO adds one row at a time.
#Every NOT NULL column must receive a value.
#Columns with a DEFAULT can be left out - the default fills in.
#conn.commit() saves all inserts permanently.

conn.execute("INSERT INTO City VALUES (1, 'Tokyo', 'Japan', 13960000, 'Yes');")
conn.execute("INSERT INTO City VALUES (2, 'Nairobi', 'Kenya', 4397000, 'Yes');")
conn.execute("INSERT INTO City VALUES (3, 'Mumbai', 'India', 20667656, 'No');")
conn.execute("INSERT INTO City VALUES (4, 'Sao Paulo', 'Brazil', 12325232, 'No');")
conn.execute("INSERT INTO City VALUES (5, 'London', 'UK', 9541000, 'Yes');")
conn.execute("INSERT INTO City VALUES (City_Id, City_Name, Country) VALUES (6, 'Sydney', 'Australia');")
conn.commit()

print("Rows inserted successfully!")

cities = pd.read_sql("SELECT * FROM City;", conn)
print(cities)

# --- PART 3: PRIMARY KEY in ACTION ----
# PRIMARY KEY uniquely identifies every row.
# No two rows can share the same City_Id
# The column also cannot be NULL.
# Trying to insert a duplicate PRIMARY KEY raises an error.

print("\n--- Testing PRIMARY KEY ---")
try:
    conn.execute("INSERT INTO City VALUES(1, 'Cairo', 'Egypt', 21323000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Id 1 already belongs to Tokyo - PRIMARY KEY must be unque. ")

# --- PART 4: NOT NULL and UNIQUE in ACTION ---
# NOT NULL means the column cannot be left without value.
# UNIQUE means no two rows can share the same value in that column.
# City_Name is both NOT NULL and UNIQUE - it must exist and must differ per row.

print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO City VALUES(7, 'Berlin', NULL, 3645000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Country is NOT NULL - every row must provide a country value.")

print("\n--- Testing UNIQUE ---")
try:
    conn.execute("INSERT INTO City VALUES(8, 'Tokyo', 'Japan', 99999, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Name is UNIQUE - 'Tokyo' is already in the table.")

# ---- PART 5: DEFAULT in Action ---
# DEFAULT sets an automatic value when no value is provided for a column.
# Sydney (row 6) was inserted without Is_Capital.
#The DEFAULT 'No' was applied automatically.

print("\n--- DEFAULT value check for Sydney ---")
sydney = pd.read_sql("""SELECT City_Name, Country, Is_Capital 
    FROM City
    WHERE City_Name == 'Sydney'; """, conn)
print(sydney)
print("Is_Capital was not given - DEFAULT 'No' was used automatically.")

# --- PART 6 Null Values
# Null means no value is stored, it is not zero and not an empty string
#It is the complete absecne of data
# A column wihtout NOT NULL can store NULL
# Use IS NULL to find rows where data is missing
# USE IS NOT NULL to find rows where data was prvodied

print("\n--- NULL in the Population column ---")
all_cities = pd.read_dql("""SELECT City_Name, Country, Population FROM City;""", conn)
print(all_cities)

missing = pd.read_sql("""SELECT City_Name FROM City WHERE Population is NULL;""", conn)
print("Cities with no population data:")
print(missing)

has_data = ("""SELECT City_Name FROM City WHERE Population is NOT NULL;""", conn)
print("Cities with population data:")
print(has_data)

conn.close()


    