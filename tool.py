import os

os.system("clear")
from pyfiglet import figlet_format
from colorama import Fore
import random
print (Fore.CYAN + figlet_format("dragon fire"))


print ("creado por the dark society [ver 1.1]")


from colorama import Fore, Style, init


init( )
print (Fore.LIGHTGREEN_EX +"        (__)")
print (Fore.LIGHTGREEN_EX +"        (oo)")
print (Fore.LIGHTGREEN_EX +"         \/ ")
print (Fore.LIGHTGREEN_EX +"        /  |")
print (Fore.LIGHTGREEN_EX +"   *---/    |---*")
print (Fore.LIGHTGREEN_EX +"       |   /")
print (Fore.LIGHTGREEN_EX +"       | /")
print (Fore.LIGHTGREEN_EX +"       |/")
print (Fore.LIGHTGREEN_EX +"       |")
print (Fore.LIGHTGREEN_EX +"       |")
print (Fore.LIGHTGREEN_EX +"      /")
print (Fore.LIGHTGREEN_EX +"     /")
print (Fore.LIGHTGREEN_EX +"    *")



mesclas = ["KNsql45@8", "yt192AR!#", "haEL23", "JcL12#$", "Sq2!@#a", "haha19", "HA29na", "ZA×ñl", "ZZesol+!", "ALql29"]
opcion1 = ["cT9!rL2$zV61+A", "Y7^kP4@wM1!xD8#q", "jL5$zQ2!vN9@tR8#", "D8@rM3!wX7#pK1^s", "fQ4#nT9&yV2!kL6@", "Z5!mB8^qR1@xP7$a", "K9*vT2#sL7!cN4@h", "uR3@xJ8$wM6!pQ1%", "P7^nW4#zA9!yD2&k", "mT8#qL2!vX9@rK5$", "bK2!zW8^pD5@nT7$", "X9@vM4$qL6!tR1#y", "T5#kP7!wA2@zN8^r", "A8!nZ5^tK2@wR7$m", "cP4#xL9!vT1@qY8^", "J6@mW2$zN7!rK4#p", "hR8^qD3@xV1!mL9$", "uQ9$gM3!rX7@pV2#", "N4^yT8@wL1#zD6!k", "R7#vK2!mX9@qP4$s"]

print ("1:generar contraseñas seguras")

print ("2:salir") 





opcion = input("> ")


if opcion == "1":
  print (random.choice(opcion1))
  print ("copia y une los dos textos para reforzamiento")
  print (random.choice(mesclas))
elif opcion == "2":
  print ("vuelve pronto :)")
else:
  print ("opcion no valida") 
