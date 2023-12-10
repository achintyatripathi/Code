'''
Given the heights of N towers and a value of K, Either increase or decrease the height of every tower by K (only once) where K > 0. 
After modifications, the task is to minimize the difference between the heights of the longest and the shortest tower and output its difference.


Input: arr[] = {1, 15, 10}, k = 6
Output:  Maximum difference is 5.
Explanation: Change 1 to 7, 15 to 9 and 10 to 4. Maximum difference is 5 (between 4 and 9). We can't get a lower difference.

Explanation - If we increase the min. height of a towel and decrease the height of tower then we can decrease the dif. between them. 

'''

def tower(l,k) -> int:

    mid = (max(l) - min(l)) // 2
    new_l = []
    if mid < k :
        return mid
    
    for i in l :

        if i >= mid :
            new_l.append(i-k)
        else:
            new_l.append(i+k)
    
    return max(new_l)-min(new_l)

l = list(map(int,input("Enter a string of letters \n").split()))
k = int(input("Enter the value to be inc. of decreased the size -  "))

print(tower(l,k))


