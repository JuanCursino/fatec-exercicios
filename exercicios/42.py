import math as m

angulo = int(input("\ndigite um angulo em graus: "))

rang = angulo*m.pi /180
print ( "\nseno: ", m.sin(rang))
print ("\nco-seno: ", m.cos(rang))
print ("\ntangente: ", m.tan(rang))
print ("\nco-secante: ",1/ m.sin(rang))
print ("\nsecante: ", 1/m.cos(rang))
print ("\ncotangente: ", 1/ m.tan(rang)) 
