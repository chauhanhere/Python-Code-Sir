
def checkpermutation(x,y):
    l=len(x)
    v=len(y)
    if l!=v:
        return False
    sort_1=sorted(x)
    sort_2=sorted(y)#sorted function returns list 
    for i in range(l):
        if sort_1[i]!=sort_2[i]:
            return False
    return True

print(checkpermutation('bacb h','b abc'))

