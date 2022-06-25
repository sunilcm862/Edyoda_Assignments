def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For Sigining Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError

def getdetails():
    print("Please Provide")
    name = str(input("Full Name: "))
    Phone_Number=input("Enter phone number: ")
    u_email=input("Enter email number: ")
    u_address=input("Enter address number: ")
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    if u_email in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +name + " " + Phone_Number+ " " +u_email + " " + password + " " + u_address
    f.write(info)

def checkdetails():
    print("Please Provide")
    u_email = str(input("Email : "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if u_email in info:
        index = info.index(u_email) + 1
        usr_password = info[index]
        index1=info.index(u_email) -2
        name_fetch=info[index1]
        #print(name_fetch)
        print(usr_password)
        print(u_email +" " + name_fetch)                                       #user name fetch
        if usr_password == password:
          print(name_fetch)                                                    #if chechdetails() return does not work
          return "Welcome Back, " + name_fetch                                 #if print(chechdetails()) return works
            
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."

#print(choices())
#print(checkdetails())