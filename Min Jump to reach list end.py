
def jump(l:list) :

    e = 0
    s = 0
    count = 0
    for i in range(len(l)) :

        s = max(s,i+l[i])
        if i == e :
            count +=1
            e = s
            if e >= len(l)-1 :
                return count 
    
    return -1

l = list(map(int,input("Enter a list of numbers \n").split()))
print(jump(l))
