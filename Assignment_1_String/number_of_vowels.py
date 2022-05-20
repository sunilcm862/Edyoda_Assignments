# 2.	Python program to count the number of vowels in a given string.
# Sample Input :
# Python is a high level programming language
# Sample Output :
# Vowels :13


str_v= input("Enter string : ")
print(" Given String is : \n ",str_v)
#vowels={"a","e","i","o","u"}
vow_count=0
for i in str_v:
     if(i in {"a","e","i","o","u"} or i in {"A","E","I","O","U"}):
          vow_count +=1
print(" Vowels : ",vow_count)

# test input:
# Python is a hIigh lEvel prOgramming langUUage