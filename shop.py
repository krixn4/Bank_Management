import mysql.connector
from unicodedata import category

con=mysql.connector.connect(user="root",password="root",host="localhost",database='shop')
# #             #establish conncetion between python and mysql server
# #             #it returns a conncetion object
c=con.cursor()
# Create a database named shop
#
# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit

# query="create database shop"
# c.execute(query,)

# c.execute('''
# create table product(product_id int not null primary key,
#                     name varchar(20),
#                     brand varchar(20),
#                     category varchar(20),
#                     price int,
#                     stock int)''')
# print("table created successfully")

def insert():
    id=input("enter product id:")
    name=input("enter product name:")
    brand=input("enter brand:")
    category=input("enter category:")
    price=int(input("enter price:"))
    stock=int(input("enter stock"))
    query="insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)"
    data=(id,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
def read():
    query="select * from product"
    c.execute(query,)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("no records found")
    con.commit()
def search():
    pid=int(input("enter product id:"))
    query="select * from product where product_id=%s"
    data=(pid,)
    c.execute(query,data)
    record=c.fetchone()
    if record:
        print(record)
    else:
        print("no record found")
    con.commit()
def update():
    pid=int(input("enter product id:"))
    stock=int(input("enter stock:"))
    query="update product set stock=%s where product_id=%s"
    data=(stock,pid)
    c.execute(query,data)
    print("stock updated")
    con.commit()
def delete():
    pid=int(input("enter product oid:"))
    query="delete from product where product_id=%s"
    data=(pid,)
    c.execute(query,data)
    print("product deleted")
    con.commit()
while(1):
    print("MENU DRIVEN\n")
    print("1. Insert Product details\n2. Read all Product details\n3. Search a Product by product_id\n4. Update the stock of a Product\n5. Delete a Product record\n6. Exit")
    ch=int(input("enter choice:"))
    if ch==1:
        insert()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        exit(0)