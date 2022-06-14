
def name(s):
    v=s.split(' ')
    print(len(v))
    new=""
    for i in range(len(v)-1):
        s=v[i]
        new+=(s[0].upper()+'.')
    new+=v[-1].title()
    return new
s=input("Enter the name")
print("name in abreviated form=",name(s))



