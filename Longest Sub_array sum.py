

def sub_array(a:list,k: int) -> list:

    max_sum = 0
    cur_sum = 0

    for i in range(len(a)):

        cur_sum+=a[i]

        if cur_sum == k:
            return ma   
        max_sum = max(max_sum,cur_sum)

