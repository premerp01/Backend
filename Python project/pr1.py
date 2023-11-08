import os
import platform
import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(host='localhost', user='root',passwd='',database='fee_management')
mycursor=mydb.cursor()



def stuInsert():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    classs=input("Enter the Class : ")
    L.append(classs)
    city=input("Enter the City ofthe Student : ")
    L.append(city)
    stud=(L)
    sql="insert into student_info (roll,name,age,class,city) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()

def stuView():
    print("Select the search criteria : ")
    print("1. Roll")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter roll no : "))
        rl=(s,)
        sql="select * from student_info where roll=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from student_info where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input("Enter age : "))
        rl=(s,)
        sql="select * from student_info where age=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter City : ")
        rl=(s,)
        sql="select * from student_info where City=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from student_info"
        mycursor.execute(sql)   
    res=mycursor.fetchall()
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
        
def feeDeposit():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    feedeposit=int(input("Enter the Fee to be deposited : "))
    L.append(feedeposit)
    month=input("Enter month of fee : ")
    L.append(month)
    fee=(L)
    sql="insert into fee_info (roll,feeDeposit,month) values (%s,%s,%s)"
    mycursor.execute(sql,fee)
    mydb.commit()

def feeView():
    print("Please enter the details to view the fee details :")
    roll=int(input("Enter the roll number of the student whose fee is to be viewed : "))
    sql="Select student_info.roll, student_info.name, student_info.class, sum(fee_info.feeDeposit), fee_info.month from student_info INNER JOIN fee_info ON student_info.roll=fee_info.roll and fee_info.roll = %s"
    rl=(roll,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    
    
def removeStu():
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="Delete from fee_info where roll=%s"
    mycursor.execute(sql,rl)
    sql="Delete from student_info where roll=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    
def authenticate_user():
    users = {
        'prem': 'prem@1604',
        'raja': 'raja@004',
        'mani': 'mani@122'
        
    }
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False


def MenuSet(): #Function For The Student Management System menu
    authenticated = False
    
    while not authenticated:
        authenticated = authenticate_user()
        
        
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Student ")
    print("Enter 3 : To Deposit Fee ")
    print("Enter 4 : To Remove Student")
    print("Enter 5 : To View Fee of Any Student")
    
    try: #Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n")
        if(userInput == 1):
            stuInsert()
            print("Student details added successfully..")
        elif (userInput==2):
            stuView()
        elif (userInput==3):
            feeDeposit()
            print("Fee deposited successfully..")
        elif (userInput==4):
            removeStu()
            print("Student details removed successfully..")
        elif (userInput==5):
            feeView()
        else:
            print("Enter correct choice. . .  ")    
            
        
MenuSet()
def runAgain():
    runAgn = input("\nwant To Run Again y/n: ")
    while(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
        
runAgain()		

