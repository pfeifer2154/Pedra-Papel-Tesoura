import random
num=int(input("Escreva 1 para papel, 2 para tesoura, 3 para pedra: "))
com=random.randint(1,3)
print("Computador: ",com)
if num==com:
   print("Empate")
elif num==1 and com==2:
   print("Vc perdeu") 
elif num==2 and com==3:
   print("Vc perdeu")   
elif num==1 and com==3:
   print("Vc ganhou")
elif num==3 and com==2:
   print("Vc ganhou")
elif num==2 and com==1:
   print("Vc ganhou")
elif num==3 and com==1:
   print("Vc perdeu")   