from idlelib import query

import mysql.connector
from mysql.connector import cursor


class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user='root',password='root',host='localhost',database='Vehicle')
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")
    def list(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")
        self.connection.commit()
    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year) values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted successfully")
    def retrieve(self,id):
        query="select * from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
