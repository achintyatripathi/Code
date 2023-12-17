
def merge(a,b):

    n = len(a)
    m = len(b)
    tmp = 0
    for i in range(n) : 
        if a[i] > b[0]:
            a[i],b[0] = b[0],a[i]

            tmp = b[0]
            k = 1 
            while k < m and b[k] < tmp :
                b[k-1] = b[k]
                k+=1
            b[k-1] = tmp 

    return a+b

a = list(map(int,input("Enter a list of numbers \n").split()))
b = list(map(int,input("Enter a list of numbers \n").split()))

print(merge(a,b))