num = int(input( "\nentre com um número de 3 dígitos: "))
c = num / 100
d = num % 100 / 10
u = num %10
numl = u*100 + d*10 + c
print ("\nnúmero: ", num)
print ("\ninvertido: ", numl)
