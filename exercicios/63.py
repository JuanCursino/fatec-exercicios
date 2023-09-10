na = int(input("\nhoras trabalhadas: "))
vha = int(input("\nvaior da hora-aula: "))
pd = int(input("\npercentuai de desconto: "))
sb = na * vha
td = ( pd / 100) * sb
sl = sb - td 
print ("\nsalario liquido: ",sl)
print ("\n")
