l=[9,5,4,55,43,432,44,5,32,34,2,0,8,7,72,5,4,42]
print(sorted(l))
odd=sum(n for n in l if n%2==1)
even=sum(n for n in l if n%2==0)
print("sum of odd elemets=",odd)
print("sum of even elemets=",even)
