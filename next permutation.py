# here in this code we are trying to achieve a new list where the next number in the list will be comming . 
# EG. -- > [1,2,3] ==> [1,3,2]  
# the reason for this one it after 123 the next no. will be 132 , 
# similarly for 321 it will be going back to the original no. that is 123 as there will be no number greater than that 

def per(l):

    n = len(l)
    for i in range(n-1,-1,-1) :

        if l[i-1] < l[i] :
            l[i:] = sorted(l[i:])
            # find the number where the no. will become increase again 
            j = i-1

            # find the least largert number from the sorted list to be replaced with the current number to get the next no. and not the highest number 
            for k in range(j,n): 
                
                if l[j] < l[k] :
                    l[j],l[k] = l[k],l[j]
                
                    return l
    return reversed(l)

print(per([1,2,3]))

