import numpy as np
A=np.array([1,2,3,4,5])
print(A)
print(type(A))

A1=np.array([[1,2,3],[4,5,6]])
print(A1)
print(type(A1))

A2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,12,13]]],ndmin=5)
print(A2)
print(A2.ndim)

A1=np.array([1,2,3,4,5,6,7,8,9,10])
print(A1[::-1])
print(A1[-1:-10:-3])
print(A1[1::2])
print(A1[-3:-10:-3])

A2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A2[1,1])
print(A2[-2,-2])
print(A2[0::,0:2])
print(A2[-1:-3:-1,-1:-3:-1])

A3=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(A3[0::,0:2])

D=np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]] ])
print('-----mokshang------')
print(D.shape)
print('-----gajera-----------')
print(D[0::,0::,1::])
print("------jesus--------")
print(D[-1:-3:-1,-1:-3:-1,-2::-1])
print('----christ-------')
print(D[0::2,0:1,0:2])

print("-------Kiran-------")
D=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
f1=D.reshape(2,6)
print(f1)
f2=D.reshape(6,2)
print(f2)

print("_---------")
D=np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]] ])
f1=D.reshape(6,3)
f2=D.reshape(3,6)
f3=D.reshape(3,6,1)
f4=D.reshape(6,3,1)
f5=D.reshape(9,2,-1)
f6=D.reshape(9,2,1)
print(f1)
print(f2)
print('-------------------')
print(f3)
print('-------------')
print(f4)
print('--------------')
print(f5)
print('----------------')
print(f6)
print(D.shape)

f=D.reshape(-1)
print(f)

a=np.array([1,2,3,45])
for i in a:
    print(i)

a=np.array([[1,2,3],[4,5,6]])
for i in a:
    for j in i:
        print(j)

a=np.array([[[1,2,3],[4,5,6]]])
for i in a:
    for j in i:
        for k in j:
            print(k)
print("----Jesus is my lord----------")


x = np.random.randint(1, 10)  # random integer from 1 to 9
print(x)


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1.shape)
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

