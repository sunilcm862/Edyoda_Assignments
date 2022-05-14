# 1.	Write a Python program to get the Fibonacci series between 0 to 50
# 	Note: The Fibonacci Sequence is the series of numbers:
# 	0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# 	Every next number is found by adding up the two numbers before it.
# 	Expected Output: 1 1 2 3 5 8 13 21 34


#---------------------Using while loop---------------------------
# n_1=int(input("Enter Fibonacci series between start number:"))
n_2=int(input("Enter Fibonacci series between 0 to "))

a=0
b=1
print("Fibonacci series between 0 to",n_2,"are : ")
if(n_2<0):
     print("Negative number")
else:
     while b<n_2:
          print(b)
          c = a + b
          a = b
          b = c