soma = 0
fibo = [1, 1]
i = 2

while True:
    next_fibo = fibo[i-1] + fibo[i-2]
    if next_fibo >= 4000000:
        break
    fibo.append(next_fibo)
    if next_fibo % 2 == 0:
        soma += next_fibo
    i += 1

print("\nA soma dos números pares da seq. de Fibonacci é igual a:", soma, "\n")

