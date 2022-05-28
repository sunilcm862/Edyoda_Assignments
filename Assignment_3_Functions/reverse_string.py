# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def string_function(st):
     print("Input string for function : ",st)
     rev = ""
     word_length=len(st)
     #print(word_length)
     while word_length>0:
          rev += st[word_length-1]
          word_length -= 1
     print("output string using function: ",rev)

string_function("1234abcd")