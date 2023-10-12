import mysql.connector
from mysql.connector import connect

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="employee"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee_info")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
# INSERT INTO 'table_name'('attribute1', 'attribute1','.....') VALUES ('attribute1value', 'attributevalue2', '.......');

# Here are some commonly used MySQL queries that you may find useful when working with XAMPP:

# 1. Creating and managing databases:

# - Create a new database: `CREATE DATABASE database_name;`
# - Select a database: `USE database_name;`
# - Show all databases: `SHOW DATABASES;`
# - Rename a database: `ALTER DATABASE old_name RENAME TO new_name;`
# - Drop a database: `DROP DATABASE database_name;`

# 2. Creating and managing tables:

# - Create a new table: `CREATE TABLE table_name (column1 datatype1, column2 datatype2, ...);`
# - Show all tables in a database: `SHOW TABLES;`
# - Describe a table: `DESCRIBE table_name;`
# - Rename a table: `ALTER TABLE old_name RENAME TO new_name;`
# - Add a new column to a table: `ALTER TABLE table_name ADD column_name datatype;`
# - Modify a column in a table: `ALTER TABLE table_name MODIFY column_name new_datatype;`
# - Drop a column from a table: `ALTER TABLE table_name DROP COLUMN column_name;`
# - Drop a table: `DROP TABLE table_name;`

# 3. Inserting, updating, and deleting data:

# - Insert a new row into a table: `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`
# - Update data in a table: `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`
# - Delete data from a table: `DELETE FROM table_name WHERE condition;`

# 4. Retrieving data:

# - Select data from a table: `SELECT * FROM table_name;`
# - Select specific columns from a table: `SELECT column1, column2, ... FROM table_name;`
# - Filter data using a WHERE clause: `SELECT * FROM table_name WHERE condition;`
# - Sort data using ORDER BY: `SELECT * FROM table_name ORDER BY column_name ASC/DESC;`
# - Limit the number of rows returned: `SELECT * FROM table_name LIMIT number_of_rows;`

# These are just a few examples of the many MySQL queries that you can use with XAMPP. The specific queries you need will depend on your specific use case and database schema.