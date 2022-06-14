#[[1,2,3],
# [4,5,6],
# [5,6,7]]

def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"Enter 0[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

def sum(a,b):
    output=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[0])):
            row.append(a[i][j]+ b[i][j])
        output.append(row)
    return output

m=int(input("Enter the value of m\n"))
n=int(input("Enter the value of n\n"))

print("Enter matrix A")
a=matrix(m,n)
print(a)

print("Enter matrix B")
b=matrix(m,n)
print(b)

s=sum(a,b)
print(s)

'''
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)
'''
