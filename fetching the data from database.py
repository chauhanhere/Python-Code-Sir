'''
#Getting data from database1
import sqlite3
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done successfully")
    cur=conn.cursor()
    cur.execute("Select * from allbooks")
    for record in cur:
        id,name,price,subject=record #Unpacking of tuples
        print(id,name,price,subject,sep=",")
except sqlite3.DatabaseError as ex:
    print("Error in Connecting",ex)
finally:
    if conn is not None:
        conn.close()
        print("Disconnected with the db successfully")

#Geting data from from database by fetchone() method
import sqlite3
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done successfully")
    cur=conn.cursor()
    cur.execute("Select * from allbooks")
    while True:
        record=cur.fetchone()
        if record is None:
            break
        id,name,price,sub=record
        print(id,name,price,sub,sep=",")
except sqlite3.DatabaseError as ex:
    print("Error in Connecting",ex)
finally:
    if conn is not None:
        conn.close()
        print("Disconnected with the db successfully")

#Printing the data of the costliest book
import sqlite3
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done successfully")
    cur=conn.cursor()
    cur.execute("Select bookname,bookprice from allbooks")
    max=0
    bname=""
    while True:
        record=cur.fetchone()
        if record is None:
            break
        name,price=record
        if price>max:
            max=price
            bname=name
    print(f"Costliest Book is {bname} with price of {max}")
except sqlite3.DatabaseError as ex:
    print("Error in Connecting",ex)
finally:
    if conn is not None:
        conn.close()
        print("Disconnected with the db successfully")

#Printing the data of the costliest book by order by clause
import sqlite3
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done successfully")
    cur=conn.cursor()
    cur.execute("Select bookname,bookprice from allbooks order by bookprice desc")
    record=cur.fetchone()
    bname,price=record
    print(f"Costliest Book is {bname} with price of {max}")
except sqlite3.DatabaseError as ex:
    print("Error in Connecting",ex)
finally:
    if conn is not None:
        conn.close()
        print("Disconnected with the db successfully")
'''
#fetching the data by fetchall() method

import sqlite3
conn=None
try:
    conn=sqlite3.connect("C:/DRIVERS/Python 310/programs/DBMS/library.db")
    print("Connection done successfully")
    cur=conn.cursor()
    cur.execute("Select bookname,bookprice from allbooks order by bookprice desc")
    record=cur.fetchall() #It will return list of tuples
    print(record)
    for i in record:
        print(i)
except sqlite3.DatabaseError as ex:
    print("Error in Connecting",ex)
finally:
    if conn is not None:
        conn.close()
        print("Disconnected with the db successfully")

start = 0
end = 0

result = []

while start < len(nums) and end<len(nums):

    if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
	end=end+1

    else:
	if start == end:
	    result.append(str(nums[start]))
	    start = start + 1
	    end = end + 1
	else:
	    result.append(str(nums[start])+'->'+str(nums[end]))
	    start = end + 1
	    end = end + 1

return result












