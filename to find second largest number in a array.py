l=[1,2,4,6,6,8]
m=max(l)
s=min(l)
for i in l:
    if i>=s and i<m:
        s=i
print(s)
