def solve () :
    f = open ("names.txt", "r")
    for ligne in f :
        chaine = ligne
    f.close ()
    chaine = sorted ((chaine.replace ('"', '')).split (','), key=str.lower)
    s = 0   # somme finale
    i = 1   # rang du mot
    for mot in chaine :
        t = 0   # somme du mot
        for lettre in mot :
            t += ord (lettre) - 64  # rang de la lettre dans l'alphabet
        s += t*i
        i += 1
    return (s)

assert (solve () == 871198282)