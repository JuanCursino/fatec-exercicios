num = int(input("\nEntre com um número com parte fracionária: "))
numi = int(num - 0.5)
numfrac = num - numi
numa = int(num + 0.00001)
print(f"\nParte inteira: ", numi)
print(f"\nParte fracionária: {(numfrac + 0.00001):.3f}")
print("\nParte arredondado: ", numa)
print("\n")
