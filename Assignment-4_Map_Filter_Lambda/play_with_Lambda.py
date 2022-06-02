# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35

a=int(input("Enter number to add with 25 : "))
x = lambda a : a + 25
print(x(a))