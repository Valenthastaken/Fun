#Buat Have Fun Aja
#OrionX


import os, sys, time, random


K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'


fun = random.choice(("Menyatakan Cinta Kepada","Menarik","Menggigit","Mencium","Memukul","Menampar","Menjauhi","Mendekati"))

nama = sys.argv[1]
dia = sys.argv[2]
password = sys.argv[3]
if password == "Orion":
    print(H+"Password Antum Benar!!")
    time.sleep(2)
else :
    print(R+"Antum Salah Memasukkan Password, Nunggunya Lama Loh")
    time.sleep(100000)
name =nama

def print_Slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def print_SlowType(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.2)


os.system('clear')

print_SlowType(R+"Wait.....\n")
print(U+"[                    ] 0%\n ")
time.sleep(1)
print_Slow(U+"[=====               ] 25%\n")
time.sleep(1)
print_Slow(U+"[==========          ] 50%\n")
time.sleep(1)
print_Slow(U+"[===============     ] 75%\n")
time.sleep(1)
print_Slow(U+"[====================] 100%\n")
time.sleep(3)

os.system('clear')
print_SlowType(H+"Welcome, Are You Ready?")
time.sleep(3)
os.system('clear')

print_SlowType(C+"\n%s "%(name))
print_SlowType(fun +" %s"%(dia))           

time.sleep(8)
print("\n\n\n\n")
print(H+"\nBye!")
pass
#Made By Orion
