# this is to reach the end of list of size n using at max m steps at a time 
# this is a generalised menthod to find the min steps we can achive it . 

def steps(n,m) :

    if n < 0 :
        return 0 
    elif n < 2 :
        return 1
    
    count = 0 
    for i in range(1,m+1):
        count+= steps(n-i,m)
    
    return count

print(steps(4,3))