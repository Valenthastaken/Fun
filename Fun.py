#Import Package

import os, sys, time, random

#Warna
K = '\033[93m' #kuning
U = '\033[95m' #Ungu
C = '\033[94m' #biru tua
R = '\033[91m' #merah
H = '\033[92m' #hijau

#Pilihan Random
fun = random.choice(("Looking At","Love","Hate","Like","Lick","Say Love To","Pull","Bytes","Touching","Make Cry","Laughing Together With","Saying Hate To","Kick","Push","Hug","'s Head. Pat By","Feel Embrassing To","Receive Love From","Refusing Love From","Kiss","Punch","Slap","Approach","Stay Away From"))

#Argumen Ke 1
nama = sys.argv[1]
#Argumen Ke 2
dia = sys.argv[2]
#Alias
name =nama
 


#Untuk Slow Type Kata Yang Kita Print
def print_SlowType(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

#Hanya Pemanis
os.system('clear')
print (R+"                      Loading                 \n")
time.sleep(2)
z = input(H+"Press enter to start")
os.system('clear')
time.sleep(2)

#Hidangan Utama:v
print_SlowType(C+"%s "%(name))
print_SlowType(fun +" %s"%(dia))           
time.sleep(3)
print("\n\n\n\n")
#Biar Gampang
x = input(K+"Press enter to exit")
  
pass 