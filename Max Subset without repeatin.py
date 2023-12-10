# here we are going to find the max lenth of a subset without repeating the string . 
# we are going to use the same concept of sub-array concept .
# this is based on two pointer theorm 


l = list(map(str,input("Enter a string of letters \n")))

def subset(l:list) -> list:

    visited = [False] * 256
    max_l = 0
    i,j = 0,0 

    while i < len(l) and j<len(l) :

        if not visited[ord(l[j])] :
            visited[ord(l[j])] = True
            j+=1
            max_l = max(max_l, j-i)
            
        
        else:
            visited[ord(l[j])] = False
            i+=1
    return max_l 

print(subset(l))