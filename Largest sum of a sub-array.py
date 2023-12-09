# to find the largest sum of a sum-array in a the array 
# here we can use the same pattern to find the largest sub-set in an array. 

l = list(map(int,input("Enter an arrayy of numbers to be used followed by spaces \n").split()))

def largest(l: int ) -> int:

    sum_l = 0 
    max_l = 0
    for i in l :

        sum_l +=i
        max_l = max(sum_l,max_l)

        if sum_l < 0 :
            sum_l = 0
    
    return max_l



print(largest(l))