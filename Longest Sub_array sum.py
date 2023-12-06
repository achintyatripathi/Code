
l = list(map(int,input("Enter list of numbers \n").split()))
k = int(input("Enter  numbers \n"))
def sub_array(a:list,k: int) -> list:

    maxL = 0
    cur_sum = 0
    d = {}
    for i in range(len(a)):

        cur_sum+=a[i]

        if cur_sum == k:
            maxL = i+1  
        elif (cur_sum - k) in d :
            maxL = max(maxL,i - d[cur_sum-k])
        
        if cur_sum not in d:
            d[cur_sum] = i 
    
    return maxL

print(sub_array(l,k))

