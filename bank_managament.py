
import mysql.connector

class bank_mgmt:

    def __init__(self):
        try:
            self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="bank_management")
            print(self.con)
        except:
            print("Connection Failed")

    def create(self,customer_name, account_type, phone, balance):
        try:
            cursor=self.con.cursor()
            query="insert into accounts(customer_name, account_type, phone, balance) values(%s,%s,%s,%s)"
            data=(customer_name, account_type, phone, balance)
            cursor.execute(query,data)
            self.con.commit()
        except:
            print("creation failed")

    def read(self):
        try:
            cursor = self.con.cursor()
            query="select * from accounts"
            cursor.execute(query)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print("no records found")
        except:
            print("no records found")

    def retrieve(self,account_id):
        try:
            cursor = self.con.cursor()
            query = "select * from accounts where account_id=%s"
            data=(account_id,)
            cursor.execute(query,data)
            record= cursor.fetchone()
            if record:
                print(record)
            else:
                print("no records found")
        except:
            print("no records found")

    def deposit(self,account_id,deposit_amount):
        try:
            cursor=self.con.cursor()
            query="update accounts set balance=balance+%s where account_id=%s"
            data=(deposit_amount,account_id)
            cursor.execute(query,data)
            self.con.commit()
        except:
            print("invalid user")

    def withdraw(self,account_id,with_amount):
        try:
            cursor=self.con.cursor()
            if balance>=withdraw_amount:
                query="update accounts set balance=balance-%s where account_id=%s"
                data=(with_amount,account_id)
                cursor.execute(query,data)
            self.con.commit()
        except:
            print("insufficient balance")

    def delete(self, account_id):
        try:
            cursor = self.con.cursor()
            query = "delete from accounts where account_id=%s"
            data = (account_id,)
            cursor.execute(query, data)
            self.con.commit()
            if cursor.rowcount > 0:
                print("Data deleted successfully")
            else:
                print("No record found")
        except:
            print("Failed to delete")

    def summary(self):
        cursor=self.con.cursor()
        query="select count(*),sum(balance),avg(balance) from accounts"
        cursor.execute(query)
        records=cursor.fetchone()
        print("Total acc:",records[0])
        print("Total Balance:", records[1])
        print("Avg Blanace:",records[2])
        query = "select account_type, count(*) from accounts group by account_type"
        cursor.execute(query)
        records = cursor.fetchall()
        print("Account Type \tNo.")
        for row in records:
            print(row[0],"\t",row[1])

b=bank_mgmt()

while(1):
    print("Menu Driven")
    print("1.Create Account")
    print("2.View All Accounts")
    print("3.Search Account")
    print("4.Deposit Amount")
    print("5.Withdraw Amount")
    print("6.Delete Account")
    print("7.Summary")
    print("8.Exit")

    ch = int(input("Enter your choice:"))
    if ch==1:
        customer_name=input("enter name:")
        account_type=input("account_type:")
        phone=int(input("phone:"))
        balance=int(input("balance:"))
        if balance>=0:
            b.create(customer_name, account_type, phone, balance)

    elif ch==2:
        b.read()

    elif ch==3:
        account_id=int(input("enter account_id:"))
        b.retrieve(account_id)

    elif ch==4:
        account_id=int(input("enter account_id:"))
        deposit_amount=int(input("enter amount:"))
        if deposit_amount>0:
            b.deposit(account_id,deposit_amount)

    elif ch==5:
        account_id = int(input("enter account_id:"))
        withdraw_amount = int(input("enter amount:"))
        if withdraw_amount>0:
            b.withdraw(account_id, withdraw_amount)

    elif ch==6:
        account_id=int(input("enter account_id:"))
        b.delete(account_id)

    elif ch==7:
        b.summary()

    elif ch==8:
        exit(0)