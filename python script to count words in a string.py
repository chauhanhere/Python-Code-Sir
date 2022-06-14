'''
n=input("Enter the string ")
res=n.split(' ')
count=len(res)
print(count)

#LEE
def mostWordsFound( sentences: list[str]) -> int:
    return max(print(len(i.split(' ')))for i in sentences)
print(mostWordsFound(["please wait","continue to fight","continue to win"]))

def checkValid(matrix: list[list[int]]) -> bool:
    n=len(matrix)
    print(n)
    for row,col in zip(matrix ,zip(*matrix)):
        print(row,col)
        if len(set(row))!=n or len(set(col))!=n:
            return False
    return True
print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))
            
print(True > False)
print(True < False)
print("I'm \n"," ""learning"" \n "," "" Python \n")


'''

s="Prashanta"
n=3
c=0
l=len(s)
if l%n==0:
    part=l/n
    for i in s:
        print("c=",c)
        if c%part==0:
            print()
        print(i,end='')
        c+=1
        








