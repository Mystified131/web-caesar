
def Seizapp(rstr, rot):

    abet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "X", "y", "z"]

    rot = 14

    wdlst = []

    nlst = []

    for ele in rstr:
        wdlst.append(ele.lower())

    for elem in wdlst:
        if elem in abet:
            lval = abet.index(elem)
            nval = lval + rot
            
            try:
                nchr = abet[nval]

            except:
                nchr = abet[nval - 26]

            nlst.append(nchr)
    
        if elem not in abet:
            nlst.append(elem)

    nwd = ""

    for elem in nlst:

        nwd += elem

    return nwd



