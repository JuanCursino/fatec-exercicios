import math as m

base = int(input("\ndigite base: "))
altura = int(input("\ndigite altura: "))
perimetro = 2*(base + altura)
area = base * altura
diagonal = m.sqrt(base**2 + altura**2)
print ("\nperimetro = " ,perimetro)
print ("\narea = ", area ) 
print ("\ndiagonal = ", diagonal)
print ("\n")
