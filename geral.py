pch = [" Braço direito, ", "braço esquerdo", "\n Perna direita,", "perna esquerda\n", "Balança a cabeça,", "dá uma voltinha\n", "Dá um pulinho", "e abraça o irmão"]

animais = ["O elefante \n E os passarinhos,", "A minhoquinha \n E os pinguins,", "O canguru \n E o sapinho,"]

def erguei():
    return(" Erguei as mãos e dai glória a Deus \n Erguei as mãos e dai glória a Deus \n Erguei as mãos \n E cantai como os filhos do Senhor\n")

def subiram(animal) :
    return f" Os animaizinhos subiram de dois em dois \n Os animaizinhos subiram de dois em dois\n {animal} como os filhos do Senhor\n"

def arca() :
    return(" Deus disse a Noé: constrói uma arca \n Deus disse a Noé: constrói uma arca \n Que seja feita \n De madeira para os filhos do Senhor\n")

def filhos(var, var2):    
    if(var2) == True:
        return f"O senhor tem muitos filhos \n Todos filhos ele tem \n Eu sou um deles, você também \n Louvemos ao senhor \n{var} \n"
    else:
        return f"O senhor tem muitos filhos \n Muitos filhos ele tem \n Eu sou um deles, você também \n Louvemos ao senhor \n{var} \n"
