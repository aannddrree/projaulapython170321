n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

if n1 == 1:
    print("Opa o valor é 1")
elif n1 == 2 or n2 == 3:
    print("opa n1 é 2 ou n2 = 3")
elif n1 >= 1000 or n2 <= -1000:
    print("opa nem sei o que falar rs")
else:
    print("e galera não entrou em nenhum condição")
