def palindrome (x) : return (int (str(x)[::-1]))

def test_lychrel (x) :
    i = 0
    b = False
    x += palindrome (x)
    while i < 50 and not (b) :
        y = palindrome (x)
        b = (x==y)
        x += y
        i += 1
    if b : return (0)
    else : return (1)
        
def solve (n) :
    s = 0
    for i in range (n) :
        s += test_lychrel (i)
    return (s)
      
assert (solve (10000) == 249)