# 3.	Write a Python program to count the number of even and odd numbers from a series of numbers.
# 	Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# 	Expected Output:
# 	Number of even numbers: 5
# 	Number of odd numbers: 4

#---------------------Using for loop---------------------------
# --------------------Using given list of numbers----------------------
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers)
oc = 0
ec = 0
for i in numbers:
     if(i % 2 == 0):
          ec +=1
     else:
    	     oc+=1
print("Number of even numbers :",ec)
print("Number of odd numbers :",oc)

#  -------------------Using Range----------------------------

a=int(input("enter start number : "))
b=int(input("enter end number : "))
print(tuple(range(a,b+1)))

oc = 0
ec = 0
for i in range(a,b+1):
     if(i % 2 == 0):
          ec +=1
     else:
    	     oc+=1
print("Number of even numbers :",ec)
print("Number of odd numbers :",oc)