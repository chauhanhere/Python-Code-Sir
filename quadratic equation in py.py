a=int(input("Enter the a of quadratic equation"))
b=int(input("Enter the b of quadratic equation"))
c=int(input("Enter the c of quadratic equation"))
d=b*b-(4*a*c)
if (d>0):
    print("roots are real and distinct")
    x=(-b+d*d)/2*a
    y=(-b-d*d)/2*a
    print('x=',x)
    print('y=',y)
elif(d<0):
    print("imaginary roots")
else:
    print("Equal roots")
    x=(-b+d*d)/2*a
    print('x=',x)
    
'''equation 1 =a=1,b=-7,c=12'''
''' equation 2 =a=1,b=-6,c=9 '''
