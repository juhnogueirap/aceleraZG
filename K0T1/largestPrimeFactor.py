def maior_fator_primo(n):
    fator = 2
    maior_fator = 0
    
    while n > 1:
        if n % fator == 0:
            maior_fator = fator
            while n % fator == 0:
                n = n // fator
        fator += 1
    
    return maior_fator

n = 600851475143
resultado = maior_fator_primo(n)
print(f"O maior fator primo de {n} é {resultado}")
