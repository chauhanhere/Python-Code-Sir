l=[eval(x) for x in input ("Enter list elements").split(',')]
element=eval(input("Enter element valuu"))
index=0
while index<len(l):
    if l[index]==element:
        print(index,end=' ')
    index+=1
