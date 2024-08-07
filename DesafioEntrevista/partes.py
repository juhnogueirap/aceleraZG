import geral

def parte1() :
    parte1a = geral.erguei()
    for i in geral.animais:
        parte1a += geral.subiram(i)
    parte1a += geral.arca()
    for i in range (3):
        parte1a += geral.erguei()
    return f"{parte1a}"


def parte2():    
    primeiro = True
    parte2a = ""
    a = ""
    for i in geral.pch:
        a += i
        parte2a += geral.filhos(a, primeiro)
        primeiro = False
    return f"{parte2a}"