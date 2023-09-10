import math as m

xnuml = int(input("\nEntrar com 1 valor: "))
xnum2 = int(input( "\nEntrar com 2 valor: "))
xnum3 = int(input( "\nEntrar com 3 valor: "))
x = xnuml + xnum2 / (xnum3 + xnuml) + 2 *(xnuml - xnum2) + m.log(64.) / m.log(2.)
print ("\nX = ", x)
print ("\n")