# rite a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def case_count(st):
    d={"uc":0, "lc":0}
    for c in st:
        if c.isupper():
           d["uc"]+=1
        elif c.islower():
           d["lc"]+=1
        else: 
           pass
    print ("Original String : ", st)
    print ("No. of Upper case characters : ", d["uc"])
    print ("No. of Lower case Characters : ", d["lc"])

case_count('The quick Brown Fox')
case_count('The quick Brown@12 Fox23@12')