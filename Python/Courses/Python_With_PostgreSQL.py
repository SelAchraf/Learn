# ============================================== Install & import psycopg2 ==============================================

# pip3 install psycopg2
# pip install psycopg2-binary

# import psycopg2

# ============================================== Connect to database ==============================================

# We can only connect to one database with one connection object

# conn = psycopg2.connect(database="db_name",
#                         host="server's_ip_adress_or_url",
#                         user="postgreSQL_user",
#                         password="postgreSQL_user_password",
#                         port="server's_port_number_on_localhost")

# ============================================== Generate a cursor ==============================================

# cursor = conn.cursor()

# ============================================== Execute queries ==============================================

# cursor.execute("the_query")

# ============================================== Modify the database ==============================================

# conn.commit() finalizes all the operations performed since the last commit and makes the changes permanent in the database
# We use .commit() after executing statements that modify the database (e.g., INSERT, UPDATE, DELETE)

# ============================================== Retrieve data from a database ==============================================

# ------------------ fetchone() ------------------------

# The fetchone() function returns the first row in the form of a tuple

# code
# print(cursor.fetchone())

# output
# (1, 'A-CLASS', '2018', 'Subcompact executive hatchback')

# ------------------ fetchall() ------------------------

# The fetchall() function works the same way as fetchone() except that it returns not just one row but all the rows

# code
# print(cursor.fetchall())

# output
# [(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
#  (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
#  (3, 'CLA', '2019', 'Subcompact executive fastback sedan'),
#  (4, 'CLS', '2018', 'E-segment/executive fastback sedan'),
#  (5, 'E-CLASS', '2017', 'E-segment/executive sedan'),
#  (6, 'EQE', '2022', 'All-electric E-segment fastback'),
#  (7, 'EQS', '2021', 'All-electric full-size luxury liftback'),
#  (8, 'S-CLASS', '2020', 'F-segment/full-size luxury sedan.'),
#  (9, 'G-CLASS', '2018', 'Mid-size luxury SUV, known as the G-Wagen'),
#  (10, 'GLE', '2019', 'Mid-size luxury crossover SUV')]
# [...]

# ------------------ fetchmany() ------------------------

# The fetchmany() function allows us to get a number of records out of the database and gives us additional control 
# over the precise number of rows we get

# code
# print(cursor.fetchmany(size=3))

# output
# [(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
#  (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
#  (3, 'CLA', '2019', 'Subcompact executive fastback sedan')]

# ============================================== Close the connection ==============================================

# cursor.close()
# conn.close()