# 1.	Python program to capitalize the first and last character of each word in a string (input string should be a statement)
# Sample Input : 
# Python is a high level programming language
# Sample Output : 
# PythoN IS A HigH LeveL ProgramminG LanguagE


string= input("Enter string to capitalize First and Last letter : ")
listc = list(string);
# print(listc)
# print(" ") 
i = 0 ;
while i < len(listc):
    # print(len(listc))
    k = i;
    while (i < len(listc) and listc[i] != ' ') :
        i += 1;
    if (ord(listc[k]) >= 97 and ord(listc[k]) <= 122 ):
        listc[k] = chr(ord(listc[k]) - 32);
    else :
        listc[k] = listc[k]
             
    if (ord(listc[i - 1]) >= 97 and ord(listc[i - 1]) <= 122 ):
        listc[i - 1] = chr(ord(listc[i - 1]) - 32);
    else :
        listc[i - 1] = listc[i - 1]

    i += 1
# print(listc)
str2=str(listc)
# print(str2)
sentence="".join(listc)
print(sentence)