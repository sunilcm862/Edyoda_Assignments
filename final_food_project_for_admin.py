#for admin page
from multiprocessing import Value
from final_food import *
import final_admin_page
import random

class food_project:
    final_admin_page.askUser()                                                      #admin login
    food_list = []

    def execute(self,choice):
        
        if choice == 1:
            print("---------------Add Food To List------------------")
            food_id = int(random.randrange(1,50))
            #print(food_id)
            # food_id = int(input("Enter Food ID : "))
            food_name = input("Enter Food Name : ")
            food_quantity = input("Enter Food Quantity : ")
            food_price = float(input("Enter Food Price : "))
            food_discount = float(input("Enter Food Discount : "))
            food_obj = food(food_id,food_name,food_quantity,food_price,food_discount)
            self.food_list.append(food_obj)
            print(food_obj)
            
        elif choice == 2:
            print("---------------Search Food------------------")
            found=False
            food_id = int(input("Enter the Food ID of the Food you want : "))
            for foods in self.food_list:
                if foods.food_id==food_id:
                    print(foods)
                    found=True
                    break
            if found==False:
                print("Food not in List")

        elif choice == 3:
            print("---------------Update Food------------------")
            food_id=int(input("Enter Book id: "))
            for foods in self.food_list:
                if foods.food_id==food_id:
                    foods.set_food_name(input("Enter Food Name: "))
                    foods.set_food_quantity(input("Enter Food Quantity: "))
                    foods.set_food_price=input("Enter Food Price: ")
                    foods.set_food_discount(float(input("Enter Food Discount: ")))

        elif choice == 4:
            print("---------------Delete Food------------------")
            found=False
            food_id = int(input("Enter the Food ID of the Food you want : "))
            for foods in self.food_list:
                if foods.food_id==food_id:
                    self.food_list.remove(foods)
                    found=True
                    break
            if found==False:
                print("Food not found")

        elif choice == 5:
            print("---------------Show Food list------------------")
            for i in range(len(self.food_list)):
                print(self.food_list[i])

        elif choice == 6:
                username = ""
                password = ""
                print("You have logged off")
                final_admin_page.askUser()

        else:
            print("Invalid Input")

while(True):
    print("Enter \n1.Add Food \n2.Search Food \n3.Update Food \n4.Delete Food \n5.Show Food list \n6.Log off")
    choice = int(input("Enter your choice : "))
    food_project_obj = food_project()
    food_project_obj.execute(choice)
