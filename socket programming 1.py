'''
def userLogin(request):
    data={}
    if request.method=="POST": #whenever method is post we need to use "/" at the last of url
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect("http://localhost:8000/show-employee/")
        else:
            data['error']="username or password is incorrect"
            return render(request,'user_login.html',data)
    else:
        return render(request,'user_login.html',data)


def email(s):
    unique=set()
    for i in s:
        local,domain=i.split('@')
        local=local.split('+')[0]
        local=local.replace('.','')
        unique.add((local,domain))
    return len(unique)
print(email(["test.email+alex@abc.com","test.e.mail+bob.cathy@abc.com","testemail+david@ab.c.com"]))
'''
def findKthPositive(arr,k):
    l,r = 0,len(arr)-1
    while l <= r:
        m = l+(r-l)//2
        diff = arr[m]-m-1
        if diff >= k:
            r = m-1
        else:
            l = m+1
    print(l,r)
    return arr[r] + (k - (arr[r]-(r)-1))
print(findKthPositive([1,2,3,4],2))

