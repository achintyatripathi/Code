# version 1.1
# this is a version of dutch flag problem 
# it will have a list on 0,1,2 no. throughout the list , we need to sort them and 
# arrange the same in a manner where all 0 ,1, 2 are linked one after other.


def dutch(a : list) -> list :
    
    left , mid = 0,0
    right = len(a) -1

    # we can follow the binary search method here . 
    # find mid here. 
    # 
    # mid == 0  then  l,mid = mid,l   l+=1 , mim+=1 
    # mid == 1 then l=mid +=1 
    # mid == 2  then ,mid = mid,r 

    while mid <= right:

        if a[mid] == 0 :
            a[left],a[mid] = a[mid], a[left]
            left +=1
            mid+=1
        elif a[mid] == 1:
            mid+=1 
        elif a[mid] == 2 :
            a[right],a[mid] = a[mid], a[right]
            right -=1
    return a 

a = list(map(int,input("Enter the list of only 0 ,1 ,2 followed by spaces !! \n").split()))
print(dutch(a))
