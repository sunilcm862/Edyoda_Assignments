import csv
#from food_project_for_admin import *

def askUser():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    checkPass(username, password)
    #csv_file()

def checkPass(use, pwd):
    if use == "admin" and pwd == "admin":
        login(use)
        #food_project_for_admin.food_project()
    else:
        print("Your username and/or password was incorrect")
        askUser()

def login(use):
    print("Welcome " + use)
    print("You have successfully logged in!")
   # askCom()

def askCom():
    command = input("Enter your command: ")
    if command == "log off" or command == "quit":
        username = ""
        password = ""
        print("You have logged off")
        askUser()
    else:
        print("Unknown command")
        askCom()

def csv_file():
     with open('F:\EdYoda\Data Science\Python\Assignments\Python_Final_Project\hfood.csv', 'r') as file:
          reader = csv.reader(file)
     for row in reader:
        print(row)


#askUser()
