def expo_rapide (x, n) :
    """
    Calcule x**n selon la méthode de l'exponentiation rapide
    """
    if n==0 :
        return (1)
    elif n==1 :
        return (x)
    elif n%2==0 :
        return (expo_rapide (x*x, int (n/2)))
    else :
        return (x*expo_rapide (x*x, int (n/2)))

def solve (n) :
    a = expo_rapide (2, n)
    s = 0
    while a>0 :
        x = a//10
        y = a%10
        s += y
        a = x
    return (s)

assert (solve (1000) == 1366)
