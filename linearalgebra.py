import numpy as np

def ex1():
    mx1= np.array([[1, 0],
                   [0, 1]])
    mx2 = np.array([[1, 2],
                    [3, 4]])

    mx1x2=np.matmul(mx1, mx2)

    print(mx1x2)


def ex2():
    try:
        n = int(input("What is the length of your array?"))
        base = np.array([1, 2, 3])
        out = np.resize(base, n *3)
        print(out)
    except:
        print("Your input should be a whole number")


def ex3():
    a= np.zeros((10,10))
    #print("10x10 0 matrix: ")
    #print(a)
    b = np.pad(a, pad_width=1, mode='constant',
                   constant_values=1)
    print("12x12 0 matrix with 1 borders: ")
    print(b)


def ex4():
    a= np.random.rand(3, 5)
    print(a)
    allsum=a.sum()
    print("Sum of all numbers:")
    print(allsum)
    rowsum=a.sum(axis=1)
    print("Sum of rows:")
    print(rowsum)
    colsum=a.sum(axis=0)
    print("Sum of columns:")
    print(colsum)


def ex5():
    a = np.array(([1, 1, 0, 0]), dtype=bool)
    b = np.array(([1, 0, 1, 0]), dtype=bool)

    for i in a,b:
        for j in range(np.shape(i)[0]):
            for k in range(np.shape(i)[0]):
                if k>j:
                    print(i)
                    print(j,k)
                    print(np.logical_and(i[j], i[k]))
                    print(np.logical_or(i[j], i[k]))


def ex6():
    a=np.array([1, 2, 0, 0, 4, 0])
    b=list()

    for i in range(np.shape(a)[0]):
        if a[i] !=0:
            print(a[i])
            b.append(i)
    print(b)


def ex7():
    a= np.random.rand(8, 8)
    print(np.max(a))
    print(np.min(a))


def ex8():
    a=np.eye(8)
    b=np.random.randint(1, 100, (8,8), dtype=int)
    c=a*b
    print(c)


def ex9():
    try:
        n=int(input("What size is your matrix?"))
        a=np.empty((n,n))
        for i in range(n):
            for j in range(n):
                a[i,j]=i+j

        print(a)
    except:
        print("Your input should be a whole number")


def ex10():
    try:
        n=int(input("What size is your matrix?"))
        a=np.empty((n,n))
        for i in range(n):
            for j in range(n):
                if i==0:
                    a[i,j]=j
                else:
                    a[i,j]=a[0,j]*(1+i)

        print(a)
    except:
        print("Your input should be a whole number")

#ex1()
#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
#ex9()
#ex10()



