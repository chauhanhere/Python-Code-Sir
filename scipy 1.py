from scipy.integrate import quad
'''
def integratefunction(x):
    return x
d=quad(integratefunction,0,1)# 0 is the lower limits and 1 is the upper limit
print(d)


def integratefn(x,a,b):
    print(x,a,b)
    return x*a+b
a,b=3,2
d=quad(integratefn,0,1,args=(a,b))
print(d)

#optimization example
import numpy as np
from scipy.optimize import root
def rootfu(x):
    return x+3.5*np.cos(x)
d=root(rootfu,0.3)
print(d)

#inverse of matrix
import numpy as np
from scipy import linalg
c=np.array([[10,6],[2,7]])
print(type(c))
print(c)
print(linalg.inv(c))

#first find the determinant the interchange the position
#of matrix diagonally and divide each element of matrix with the determinant

#finding determinants
import numpy as np
from scipy import linalg
c=np.array([[10,6],[2,7]])
print(type(c))
print(c)
print(linalg.det(c))

#solving linear equation
import numpy as np
from scipy import linalg
a=np.array([[2,3,1],[-1,5,4],[3,2,9]])
b=np.array([21,9,6])
print(linalg.solve(a,b))


#calculating eigen values and eigen vactors
import numpy as np
from scipy import linalg
a=np.array([[5,8],[7,9]])
eigenvalues,eigenvector=linalg.eig(a)
d,e=eigenvalues
print(d,e)
print(eigenvector[:,0])
print(eigenvector[:,1])
'''

#scipy subpackage:-Statistics
from scipy.stats import norm
print(norm.rvs(loc=0,scale=1,size=10))
print(norm.cdf(5,loc=1,scale=2))
print(norm.pdf(9,loc=0,scale=1))














