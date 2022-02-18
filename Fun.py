#Import Package

import os, sys, time, random

#Color
K = '\033[93m' #Yellow
U = '\033[95m' #Purple
C = '\033[94m' #biru tua
R = '\033[91m' #Red
H = '\033[92m' #Green

#Random Choice
fun = random.choice(("Looking At","Love","Hate","Like","Lick","Say Love To","Pull","Bytes","Touching","Make Cry","Laughing Together With","Saying Hate To","Kick","Push","Hug","'s Head. Pat By","Feel Embrassing To","Receive Love From","Refusing Love From","Kiss","Punch","Slap","Approach","Stay Away From"))

#First Args
nama = sys.argv[1]
#Second Args
dia = sys.argv[2]
#Alias
name =nama
 


#Slowtype Word
def print_SlowType(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

#Addon
os.system('clear')
print (R+"                      Loading                 \n")
time.sleep(2)
z = input(H+"Press enter to start")
os.system('clear')
time.sleep(2)

#Main course
print_SlowType(C+"%s "%(name))
print_SlowType(fun +" %s"%(dia))           
time.sleep(3)
print("\n\n\n\n")
#Easy
x = input(K+"Press enter to exit")
  
pass 
