import numpy as np
"""#to create an array
a=np.array([10,20,30,40],dtype='int16')
print(a)

#to create a 2d array
b=np.array([[1,2,3,4,],[5,6,7,8]])
print(b)

print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.nbytes)
print(a.itemsize)

#array index slicing
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

print(a[0,4])
print(a[1])
print(a[:,5])
a[1,4]=24
print(a[1,0:6:2])
b=np.array([[[1,2,],[3,4]],[[5,6],[7,8]]])
print(b[1,1,1])
print(b[0,:,1])
b[:,1,:]=[9,9],[8,8]
print(b)


#initializing different types of arrays

#all 0s matrix(work outside in)
a=np.zeros((3,3,3))
print(a)


#all 1s matrix
b=np.ones((3,3,3))
print(b)
a.six
#any other no
c=np.full((2,2),11)
print(c)
print(c[1])

#any other no(full_like)
d=np.full_like(b,7)
print(d)

#random decimal nos
e=np.random.rand(3,2)
print(e)

#random integer nnos
f=np.random.randint(-8,8,size=(3,2))
print(f)

#identity matrix
g=np.identity(8)
print(g)

#to repeat an array
arr=np.array([[1,2,3]])
rl=np.repeat(arr,3,axis=0)
print(rl)

#mini question
z=np.ones((5,5))
print(z)

y=np.zeros((3,3))
y[1,1]=9
print(y)

z[0:3,0:3]=y
print(z)

#copying arrays
n=np.array([1,2,3])
m=n
m[1]=200
print(m)


#basic mathematics using arrays
a=np.array([1,2,3,4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

#sum of 2 arrays
b=np.array([1,2,3,4])
print(a+b)
#trigonometric values(sin,cos,tan)
s=np.sin(a)
print(s)

#linear algebra
a=np.ones((2,3))
b=np.full((3,2),3)
c=np.matmul(a,b)
print(c)

#find the determinant
d=np.random.randint(12,size=(2,2))
print(d)
e=np.linalg.det(d)
print(e)

#statistics
stats=np.array([[1,2,3],[4,5,6]])
print(stats)
a=np.min(stats,axis=0)
print(a)

b=np.max(stats,axis=1)
print(b)

c=np.sum(stats)
print(c)

#reorganizing arrays
bef=np.array([[1,2,3,4],[5,6,7,8]])
print(bef)

#reshape(as long as it has the same number )
aft=bef.reshape((2,2,2))
print(aft)

#vertically stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v=np.vstack([v1,v2,v1,v2,v1,v2])
print(v)

#horizontally stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v3=np.hstack([v1,v2])
print(v3)"""












