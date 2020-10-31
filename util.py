from random import randint

def findPrimRoot(p):
    if (p == 2):
        return 1
    
    p1 = 2
    p2 = (p-1) // p1

    while(1):
        g = randint(2, p-1)
        if not (pow(g, (p-1)//p1, p) == 1) and not (pow(g, (p-1)//p2, p) == 1):
            return g