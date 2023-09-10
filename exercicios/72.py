deposito = int(input("\nEntre com deposito: "))
taxa = int(input("\nEntre com a taxa de juros: "))
valor = deposito * taxa / 100
total = deposito + valor
print("\nRendimentos: ", valor, "\nTotal: ", total)
print("\n")
