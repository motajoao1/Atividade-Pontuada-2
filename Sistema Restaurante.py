import os
os.system ("cls || clear")

soma = 0
pr = 0
escolhidos = ""

while True:
    print( """
          Código \t Prato \t\t Valor
          1 \t Picanha \t\t R$25,00
          2 \t Lasanha \t\t R$20,00
          3 \t Strogonoff \t\t R$18,00
          4 \t Bife Acebolado \t R$15,00
          5 \t Pão com ovo \t\t R$5,00
          6 \t Misto \t\t\t R$7,00              
          7 \t Milkshake \t\t R$20,00     
""")
    opcao = int (input("Digite o numero da opção desejada: "))
    
    match opcao:
        case 1:
            prato = "1. Picanha "
            preco = 25 
            pr += 1
            escolhidos += prato
        case 2:
            prato = "2. Lasanha "
            preco = 20
            pr += 1
            escolhidos += prato
        case 3:
            prato = "3. Strogonoff "
            preco = 18
            pr += 1
            escolhidos += prato
        case 4:
            prato = "4. Bife Acebolado "
            preco = 15
            pr += 1
            escolhidos += prato
        case 5:
            prato = "5. Pão com ovo "
            preco = 5
            pr += 1
            escolhidos += prato
        case 6:
            prato = "6. Misto " 
            preco = 7
            pr += 1
            escolhidos += prato
        case 7:
            prato = "7 . Milkshake " 
            preco = 20
            pr += 1
            escolhidos += prato
        case 0:
            break
        case _:
            print("Opção Inválida! Por favor, escolha outro prato.")
        
            
    soma += preco
    continuar = input("Deseja escolher outro prato? \nDigite 'S' ou 'N': ").lower()
    if continuar == "n":
        break

print(f"\nTotal de pedidos: {pr}")
print (f"Pratos selecionados: {escolhidos}")
print(f"Total a pagar: R$ {soma}")
forma_de_pagamento = int(input("""
Digite a forma de pagamento:                               
1 - A vista
2 - Crédito                             
"""))

match forma_de_pagamento:
    case 1:
        valort = soma * 0.9
        print("Desconto de 10%.")
        print(f"Total a pagar: R${valort}")
    case 2:
        valort = soma * 1.1
        print(f"Acréscimo de 10%.")
        print(f"Total a pagar: R${valort}")