#define a class to perform database operations on book table
# create a class named BookListCreateRetrieveUpdateDelete and define methods
# list() --> for reading all records
# create() -->for creating a new record
# retrieve(id) --> for reading a specific record
# update(id,data) --> for updating a specific record
# delete(id) --> for deleting a specific record
from idlelib import query

import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):

        self.connection=mysql.connector.connect(user='root',password='root',host='localhost',database='library_db')
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")

    def list(self):

        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("not records found")

    def create(self,title,author,price,pages,language):

        query="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted successfully")

    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no record found")
        self.connection.commit()
    def update(self,id,title,author,price,pages,language):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.connection.rowcount>0:
            print("row updated")
        else:
            print("no record found")
    def delete(self,id):
        query = "delete from book where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("data is deleted")
        else:
            print("no record found")
book_instance=BookListCreateRetrieveUpdateDelete()
while(1):
    print(("MENU DRIVEN\n"))
    print("1.Display all records.\n2.Insert new record.\n3.Retrieve a record.\n4.Update a record.\n5.Delete a record.\n6.Exit\n")
    ch=int(input("enter choice:"))
    if ch==1:
        book_instance.list()
    elif ch==2:
        title=input("enter title:")
        author=input("enter author name:")
        price=int(input("enter price:"))
        pages=int(input("enter pages:"))
        language=input("enter language:")
        book_instance.create(title,author,price,pages,language)
    elif ch==3:
        id=int(input("enter id to retrieve:"))
        book_instance.retrieve(id)
    elif ch==4:
        id=int(input("enter id to update:"))
        title = input("enter title:")
        author = input("enter author name:")
        price = int(input("enter price:"))
        pages = int(input("enter pages:"))
        language = input("enter language:")
        book_instance.update(id,title,author,price,pages,language)
    elif ch==5:
        id=int(input("enter id to delete:"))
        book_instance.delete(id)
    elif ch==6:
        exit(0)



