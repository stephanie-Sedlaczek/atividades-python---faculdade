valor_saque = int(input("informe valor do saque: "))

print(f"{valor_saque // 100} cédulas de 100.")   
valor_saque = valor_saque % 100

print(f"{valor_saque // 50} cédulas de 50.")   
valor_saque = valor_saque % 50