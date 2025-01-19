import sqlite3
##Connection
connection=sqlite3.connect("products.db")
##Create cursor object used to create table, insert records,retrieve records.
cursor=connection.cursor()
##Create the table
table_info = """ 
CREATE TABLE PRODUCTS(PRODUCT_ID VARCHAR(25), PRODUCT_NAME VARCHAR(25), PRICE INT,
CATEGORY VARCHAR(25),SALES_PERCENTAGE_2023 INT,SALES_PERCENTAGE_2024 INT);
"""
cursor.execute(table_info)
## Insert few records
cursor.execute('''INSERT INTO PRODUCTS VALUES('S101','Dove',80,'Soap',56,63)''')
cursor.execute('''INSERT INTO PRODUCTS VALUES('S102','Pears',85,'Soap',67,45)''')
cursor.execute('''INSERT INTO PRODUCTS VALUES('S103','Colgate',110,'Tooth paste',76,75)''')
cursor.execute('''INSERT INTO PRODUCTS VALUES('S104','Close up',105,'Tooth paste',74,81)''')
##Display all the recors
prodcut_info = cursor.execute('''SELECT * FROM PRODUCTS''')
for row in prodcut_info:
  print("Inserted record is ---> ",row)

##Close the connection
connection.commit()
connection.close()