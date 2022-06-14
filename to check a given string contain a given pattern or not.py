'''
s=input("ENter a string")
x=input("Enter the part")
print(x in s)
'''
#counting sub string in a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count
    
