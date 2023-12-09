# this is to create a code to share a list of prod from all the element in the list 
# note : this is without the no. itself. 


l = list(map(int, input("Enter the list of numbers followed by a space \n").split()))

def prod(l: list ) -> list:

    new_l = [1]*len(l)
    for i in range(1,len(l)) :        
        new_l[i] = l[i-1]*new_l[i-1]
    
    suf = 1 
    for i in range(len(l)-1,-1,-1):
        new_l[i] = new_l[i]* suf
        suf = l[i]*suf

    return new_l

print(prod(l))


