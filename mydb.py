from doctest import register_optionflag
from idlelib import query

import mysql.connector
# con=mysql.connector.connect(user="root",password="root",host="localhost")
#             #establish conncetion between python and mysql server
#             #it returns a conncetion object
# print(con)
#
# c=con.cursor()  #cursor object used to execute sql queries
#
# #c.execute(command)
# #create database file
#
# c.execute("create database school_db")
# print("database file created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")
c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,
#                     name varchar(20),
#                     age int,
#                     place varchar(20),
#                     phone varchar(20),
#                     total_mark int)''')
# print("table created successfully")

# c.execute('''
# insert into student(roll_no,name,age,place,phone,total_mark)
#             values(101,'arun',11,'ekm','9748284731',145),
#             (102,'amal',12,'ekm','9472847573',140),
#             (103,'anu',11,'tvm','9384828482',147),
#             (104,'hari',12,'tcr','8963548163',144),
#             (105,'ramu',11,'ekm','9372647281',141)
# ''')

# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(106,'kiran',12,'ekm','9874058375',140)
# c.execute(query,data)
# con.commit()
# print("data inserted")

#         # READ OPERATION

# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("no records found")


        #read all attributes of a student with rollno entered by user

# rollno=int(input("enter rollno:"))
# query="select * from student where roll_no=%s"
# data=(rollno,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print("no record found")
# con.commit()

        #update mark of a student with rollno entered by user

# rollno=int(input("enter rollno:"))
# mark=int(input("enter new mark:"))
# query="update student set total_mark=%s where roll_no=%s"
# data=(mark,rollno)
# c.execute(query,data)
# con.commit()

        #delete a record with rollno entered by user

# rollno=int(input("enter roll no:"))
# query="delete from student where roll_no=%s"
# data=(rollno,)
# c.execute(query,data)
# con.commit()

        # create a new record using values entered by user

# rollno=int(input("enter rollno:"))
# name=input("enter name:")
# age=int(input("enter age:"))
# place=input("enter place:")
# phone=int(input("enter phone no:"))
# mark=int(input("enter mark:"))
# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(rollno,name,age,place,phone,mark)
# c.execute(query,data)
# con.commit()


