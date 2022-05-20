# 3.	Program to check if a string contains any special character.
# Sample Input : 
# Python is a high level programming language
# Sample Output : 
# String is accepted

# 	Sample Input : 
# 	Python@is a&high level*programming language
# 	Sample Output : 
# 	String is not accepted

import re
string = input("Enter string: ")
spe_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if(spe_char.search(string) == None):
    print("String is accepted")
else:
    print("String is not accepted")



# test input: Assignment 01: String