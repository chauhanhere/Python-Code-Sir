import sqlite3
'''
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done Successfully")
    curr=conn.cursor()
    curr.execute("Insert into allbooks values(106,'Web Dev',800,'FrontEnd')")
    conn.commit()
    print("record Inserted")
except sqlite3.DatabaseError as ex:
    print("Error in connecting to database",ex)
finally:
    if conn is not None:
        conn.close()
        print("Database closed Successfully")

#Taking data from the user and then inserting it into the table
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done Successfully")
    curr=conn.cursor()
    id=int(input("Enter the id of book"))
    name=input("Enter the name of book")
    price=float(input("Enter the price of book"))
    sub=input("Enter the sub of book")
    curr.execute("Insert into allbooks values(:1,:2,:3,:4)",(id,name,price,sub))
    conn.commit()
    print("record Inserted")
except sqlite3.DatabaseError as ex:
    print("Error in connecting to database",ex)
finally:
    if conn is not None:
        conn.close()
        print("Database closed Successfully")

#updating the values of table with static queries
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done Successfully")
    curr=conn.cursor()
    curr.execute("update allbooks set bookprice=1000 where bookid=102")
    n=curr.rowcount
    print("Rows updated=",n)
    conn.commit()
except sqlite3.DatabaseError as ex:
    print("Error in connecting to database",ex)
finally:
    if conn is not None:
        conn.close()
        print("Database closed Successfully")

#updating the values of table by taking values from the user
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done Successfully")
    curr=conn.cursor()
    booksub=input("Enter the subject name")
    pri=float(input("Enter the increment in price"))
    curr.execute("update allbooks set bookprice=bookprice+:1 where booksub=:2",(pri,booksub))#codition is case sensitive
    if curr.rowcount==0:#our condition may not match thats why we will check our data updated or not
        print("No Books Updated")
    else:
        print(curr.rowcount,"books updated")
        conn.commit()
except sqlite3.DatabaseError as ex:
    print("Error in connecting to database",ex)
finally:
    if conn is not None:
        conn.close()
        print("Database closed Successfully")

#deleting data from the table statitically
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done Successfully")
    curr=conn.cursor()
    curr.execute("delete from allbooks where bookid=107")
    if curr.rowcount==0:#our condition may not match thats why we will check our data updated or not
        print("No Books deleted")
    else:
        print(curr.rowcount,"books deleted")
        conn.commit()
except sqlite3.DatabaseError as ex:
    print("Error in connecting to database",ex)
finally:
    if conn is not None:
        conn.close()
        print("Database closed Successfully")
''' 
#deleting data from the table dynamically
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done Successfully")
    curr=conn.cursor()
    id=input("Enter the book id")
    curr.execute("delete from allbooks where bookid=:1",(id,))#codition is case sensitive
    if curr.rowcount==0:#our condition may not match thats why we will check our data updated or not
        print("No Books deleted")
    else:
        print(curr.rowcount,"books deleted")
        conn.commit()
except sqlite3.DatabaseError as ex:
    print("Error in connecting to database",ex)
finally:
    if conn is not None:
        conn.close()
        print("Database closed Successfully")
     














