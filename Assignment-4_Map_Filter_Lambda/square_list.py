# Write a Python program to square the elements of a list using map() function.
# Sample List:  [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

input_list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
     ele = int(input("Enter elements for list : "))
     input_list.append(ele) # adding the element
print(" ")
print("Original list : ",input_list)
print("Result list(Square) using * : ",list(map(lambda n: n*n, input_list)))
print(" ")
print("Result list(Square) using ** : ",list(map(lambda n: n**2, input_list)))
print("----------------- ")

#given list
print(" ")
s_list=[4, 5, 2, 9]
print("sample Original list : ",s_list)
print("Squared result of given sample list : ",list(map(lambda n: n ** 2, s_list)))
print("---------------- ")