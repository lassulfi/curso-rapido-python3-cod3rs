def soma(a, b):
    return a + b

somar = soma
print(somar(3, 4))

def subtracao(a, b):
    return a - b

def operacao_binaria(fn, op1, op2):
    return fn(op1, op2)

resultado1 = operacao_binaria(soma, 13, 48)
print(resultado1)

resultado2 = operacao_binaria(subtracao, 13, 38)
print(resultado2)

# Avaliação tardia
def soma_parcial(a):
    # processamento pesado 1 - 10 s
    # processamento pesado 2 - 10 s
    # processamento pesado 3 - 40 s
    def concluir_soma(b):
        return a + b # 10 s
    return concluir_soma

# r1 = soma_total(1, 2) => 1m10s
# r2 = soma_total(1, 3) => 1m10s
# r3 = soma_total(1, 4) => 1m10s

# total: 3 min 30 s

soma_1 = soma_parcial(1) # 1m
r1 = soma_1(2) # 10 s
r2 = soma_1(3) # 10 s
r3 = soma_1(4) # 10 s

# total 1 min e 30 s

fn = soma_parcial(10)
resultado_final = fn(12)
print(resultado_final)

resultado_final = soma_parcial(12)(22)
print(resultado_final, r1, r2, r3)
