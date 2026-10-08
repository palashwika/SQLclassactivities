import sqlite3
import pandas as pd

conn = sqlite3.connect('basketball (3).sqlite')


conn = sqlite3.connect('basketball.db')

cursor = conn.cursor()


cursor.executescript("""
                     
DROP TABLE IF EXISTS Basketball;
CREATE TABLE Basketball (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT,
    team TEXT,
    position TEXT,
    age INTEGER,
    points_per_game REAL,
    rebounds_per_game REAL,
    assists_per_game REAL
);

INSERT INTO Basketball VALUES
(1, 'LeBron James', 'Lakers', 'SF', 41, 24.5, 7.8, 8.2),
(2, 'Stephen Curry', 'Warriors', 'PG', 38, 26.1, 4.5, 6.4),
(3, 'Jayson Tatum', 'Celtics', 'SF', 28, 27.2, 8.1, 4.7),
(4, 'Nikola Jokic', 'Nuggets', 'C', 31, 29.4, 12.3, 10.1),
(5, 'Luka Doncic', 'Lakers', 'PG', 27, 28.7, 8.9, 9.3),
(6, 'Giannis Antetokounmpo', 'Bucks', 'PF', 31, 30.2, 11.4, 6.1),
(7, 'Anthony Edwards', 'Timberwolves', 'SG', 25, 27.5, 5.2, 4.8),
(8, 'Shai Gilgeous-Alexander', 'Thunder', 'PG', 28, 31.0, 5.4, 6.3),
(9, 'Victor Wembanyama', 'Spurs', 'C', 22, 24.8, 11.7, 3.5),
(10, 'Devin Booker', 'Suns', 'SG', 30, 26.3, 4.2, 6.7);""")
conn.commit()

print('Database ready!')

all = pd.read_sql("""Select * FROM Basketball""", conn)
print(all)
