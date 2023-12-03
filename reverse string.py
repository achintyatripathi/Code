# Reverse string
# version 1.0


def reverse(a : list ) -> list:

    l,r = 0,len(a)-1

    while l < r :

        a[l],a[r] = a[r],a[l]
        l+=1
        r-=1

    return a 

a = input("Enter a list of numbers to reverse the list , followed by a space !! ").split()
print(reverse(a))