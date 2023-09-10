sm = int(input("\nentre com o salário mínimo: "))
qtdade = int(input("\nentre com a quantidade em quilowatt: "))
preco = sm /700
vp = preco * qtdade
vd = vp * 0.9
print("\npreço do quilowatt: ", preco, "\nvalor a ser pago: ", vp,"\nvalor com desconto: ", vd)
