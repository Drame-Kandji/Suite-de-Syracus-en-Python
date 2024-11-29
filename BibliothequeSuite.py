
def collatz(x):
    #la règle de Collatz à un entier x.
    return x // 2 if x % 2 == 0 else 3 * x + 1

def syracuse(x, direct=True):
    if x==1:
        print(1)
    else:
        if(direct):
            print(x)
        
        syracuse(collatz(x), direct)
        
        if(not direct):
            print(x)

    
def temps_parcouru(x):
    #le nombre d'itérations pour atteindre 1.
    if x == 1:
        return 0
    else:
        colat= collatz(x)
        return 1 + temps_parcouru(colat)

def altitude(x, maxVal=None):
    #la valeur maximale atteinte dans la suite de Syracuse.
    if maxVal is None:
        maxVal = x

    if x==1:
        return maxVal
    else:

        y=collatz(x)
        return altitude(y,max(y,maxVal))



