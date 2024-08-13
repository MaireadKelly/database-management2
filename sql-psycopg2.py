import psycopg2

# CONNECT TO CHINOOK DATABASE
connection = psycopg2.connect(database="chinook")

# BUILD A CURSOT OBJECT OF THE DATABASE
cursor = connection.cursor()

# FETCH THE RESULTS (MULTIPLE)
results = cursor.fetchall()

# FETCH THE RESULT (SINGLE)
# RESULTS = CURSOR.FETCHONE()

# CLOSE CONNECTION 
connection.CLOSE()

# PRINT RESULTS 
for results in results:
    print(results)
    