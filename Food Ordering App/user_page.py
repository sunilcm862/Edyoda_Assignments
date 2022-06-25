from food import *
import user_regi_and_login

class user_food_project:
     user_regi_and_login.checkdetails()

     def execute(self,choice):
          food_list = [(1,"Tandoori Chicken","(4 pieces)","[INR 240]"),(2,"Vegan Burger","(1 Piece)","[INR 320]"),(3,"Truffle Cake","(500gm)","[INR 900]")]
          #print(type(food_list))
          print(food_list)

          new_food_list=[]
          #print("Before append : ")
          #print(new_food_list)

          if choice == 1:
               print("---------------Add Food To List------------------")
               b=input("Enter number : ")                        #print(type(b))
               a = b.split()                                      #print(a)  print(type(a))
               print("New Order(Food) : ")                      #print(a[0])   print(type(a[0]))  print(type(int(a[0])))

               for i in range(0,len(a)):
                    c=int(a[i])                        #print(int(a[i]))   #print(type(a[i]))  #print("food list : ")   #print(food_list[c-1])
                    new_food_list.extend(food_list[c-1])                    #print("after append ")
               print(new_food_list)
     

     # elif choice == 2:
     #        print("---------------Search Food------------------")
     #        found=False
     #        food_id = int(input("Enter the Food ID of the Food you want : "))
     #        for foods in self.food_list:
     #            if foods.food_id==food_id:
     #                print(foods)
     #                found=True
     #                break
     #        if found==False:
     #            print("Food not in List")

     # elif choice == 3:
     #      print("---------------Update Profile------------------")
          
          elif choice == 4:
               u_email=""
               password=""
               user_regi_and_login.checkdetails()
          
          else:
               print("Invalid Input")

while(True):
    print("\nEnter \n1.Place New Order \n2.Order History \n3.Update prifile \n4.Log off")
    choice = int(input("Enter your choice : "))
    user_food_project_obj = user_food_project()
    user_food_project_obj.execute(choice)