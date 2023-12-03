# version 1.0
# we need to move the -ve values to left 

def negative(a:list) -> list:

    l,r  = 0 , len(a)-1
    while l < r :

        if a[l] < 0 : 
            l += 1
        elif a[r] > 0 :
            r -= 1
        
        else:
            a[l],a[r] = a[r],a[l]
    return a

a = list(map(int,input(" Enter the values -\n").split()))
print(negative(a))
        
        
