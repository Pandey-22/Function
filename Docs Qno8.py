# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def alphabets(string):
    i=0
    upper_case=0
    lower_case=0
    while i<len(string):
        if string[i].isupper():
            upper_case+=1
        elif string[i].islower():
            lower_case+=1
        i=i+1
    print("uppercase =",upper_case)
    print("lower case =",lower_case)
alphabets("The quick Brow Fox")