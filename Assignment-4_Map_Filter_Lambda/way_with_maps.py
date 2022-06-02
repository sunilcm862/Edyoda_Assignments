# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list:  [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

#input list from user
input_list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
     ele = int(input("Enter elements for list : "))
     input_list.append(ele) # adding the element
print(" ")
print("Original list : ",input_list)
print("Result list(triple) : ",list(map(lambda n: 3 * n, input_list)))
print(" ")

#given list
print(" ")
s_list=[1, 2, 3, 4, 5, 6, 7]
print("sample Original list : ",s_list)
print("Trippled result of given sample list : ",list(map(lambda n: 3 * n, s_list)))
print(" ")