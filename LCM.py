
l = list(map(int,input("Enter list of numbers \n").split()))
def GCD(x,y) :

    while y :
        x,y = y , x%y
    return x

lcm = 1 
for i in l :
    lcm = (lcm*i) // GCD(lcm,i)

print(lcm)