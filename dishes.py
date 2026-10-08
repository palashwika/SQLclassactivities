import sqlite3

import pandas as pd

# ---- PART 1: Build and Explore the Tables ----

conn = sqlite3.connect(':memory:')

conn.execute("CREATE TABLE recipe (recipe_id INTEGER PRIMARY KEY, recipe_name TEXT NOT NULL, cuisine TEXT NOT NULL, prep_mins INTEGER NOT NULL)")

conn.execute("CREATE TABLE ingredient (ingredient_id INTEGER PRIMARY KEY, recipe_id INTEGER NOT NULL, item TEXT NOT NULL, quantity_g INTEGER NOT NULL)")

conn.executemany("INSERT INTO recipe VALUES (?, ?, ?, ?)", [

(1, 'Pasta', 'Italian', 20),

(2, 'Tacos', 'Mexican', 15),

(3, 'Sushi', 'Japanese', 45),

(4, 'Pizza', 'Italian', 30),

(5, 'Salad', 'Greek', 10),

])

conn.executemany("INSERT INTO ingredient VALUES (?, ?, ?, ?)", [

(1, 1, 'Pasta', 200),

(2, 1, 'Sauce', 150),

(3, 2, 'Tortilla', 80),

(4, 2, 'Beef', 120),

(5, 3, 'Salmon', 180),

(6, 4, 'Dough', 250),

(7, 5, 'Lettuce', 50),

(8, 5, 'Feta', 40),

])

conn.commit()

### Part 1 — Column Aliases

##Question 1:**

##From the `recipe` table, display the recipe name, cuisine, and preparation time. Rename the output columns to `dish`, `style`, and `time` respectively.


dishes =  pd.read_sql("SELECT recipe_name AS dish, cuisine AS style, prep_mins AS time FROM recipe", conn)
print(dishes)



### Part 2 — Table Aliases + JOIN

##**Question 2:**

#The `recipe` table contains recipe information and the `ingredient` table contains ingredients for each recipe.

##Join these two tables and display:

##* Recipe name as `dish`

#* Ingredient name as `item`

#* Ingredient quantity as `grams`

##Use short aliases for both tables to make the query easier to read.

recipe_info=pd.read_sql("SELECT recipe.recipe_name AS dish, item, ingredient.quantity_g AS grams FROM recipe INNER JOIN ON recipe.recipe_id==ingredient.ingredient_id ", conn)
print(recipe_info)


### Part 3 — Subquery with `IN`

#**Question 3:**

#Find all recipes that use **at least one ingredient with a quantity greater than 100 grams**.

#Display:

#* Recipe name as `dish`

#* Cuisine as `style`

#Use a subquery to first find the `recipe_id` values of recipes having an ingredient quantity greater than 100 grams.

greater_than100 = pd.read_sql("SELECT recipe_name AS dish, cuisine AS style FROM recipe WHERE recipe_id IN (SELECT ) ")
print(greater_than100)


### Part 4 — Subquery with `=`

#**Question 4:**

#Find the recipe or recipes that have the **shortest preparation time**.

#Display:

###
# Use a subquery to find the minimum preparation time rather than sorting the table.



### Challenge — Combine Concepts

#**Question 5:**

#Find all recipes that contain an ingredient weighing more than 100 grams. Display the recipe name as `dish`, cuisine as `style`, and preparation time as `time`.

#Use:

#* A column alias

#* A table alias

#* A subquery with `IN`

#**Expected concepts:** `AS`, table aliases, `WHERE ... IN`, and subqueries.
