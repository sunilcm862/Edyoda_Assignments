# 2.	Write a Python program that accepts a word from the user and reverse it.
# 	Sample Test Case
# 	Input: Edyoda
# 	Output: adoydE

#---------------------Using while loop---------------------------
word = input("Enter string to reverse :")
print("")
print ("Original word/string  is : ",word)
reverse = ""
word_length = len(word)
while word_length > 0:   
    reverse += word[ word_length - 1 ]
    #print(reverse)
    word_length = word_length - 1
print ("Reversed word/string is : ",reverse)