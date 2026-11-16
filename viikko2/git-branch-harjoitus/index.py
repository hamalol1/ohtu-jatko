from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}")
print(f"{x} - {y} = {erotus(x, y)}")
print(f"{x} * {y} = {tulo(x, y)}")

<<<<<<< HEAD
logger("lopetetaan ohjelma")
print("goodbye!") # lisäys bugikorjaus-branchissa

#hei hei
=======
logger("lopetetaan")
print("goodbye!")

#Moi moi
>>>>>>> 51191c34e7869a3212872dc23cde2b89fc0c758c
