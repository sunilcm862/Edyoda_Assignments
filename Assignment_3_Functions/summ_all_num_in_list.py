# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
 
 #using function
def sum(n):
     print("Input list : ",n)
     total = 0
     for x in n:
        total += x
     print("Sum of all numbers in list : ", total)
sum((8, 2, 3, 0, 7))
#sum((8, 2, 3, 0, 7,6,9))

#----------------------------------

# #without functions
# a=(8,2,3,0,7)
# print(a)
# sum=0
# for i in a:
#      sum+=i
# print(sum)