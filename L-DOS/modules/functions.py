import time

# modules
import modules.sound as sound

def math():
    a = input("Number A? ")
    b = input("Number 2? ")
    op = input("""
    Input Option:
    A: Add
    S: Subtract
    M: Multiply
    D: Divide
    """)

    if op == "a" or "A":
        print(int(a) + int(b))
    elif op == "s" or "S":
        print(int(a) - int(b))
    elif op == "m" or "M":
        print(int(a) * int(b))
    elif op == "d" or "D":
        print(int(a) / int(b))


def etest():
    print("Loading etest tool...")
    time.sleep(0.5)
    print("etest tool loaded.")
    
    ets = int(input("What error key to test? Use integer key. "))
    
    sound.confirm_beep()
    
    if ets == 1:
        print("ekey 1 - requires newer version")
        #update()
        return "update"
    elif ets == 2:
        print("ekey 2 - program not currently installed.")
        #not_installed()
        return "not installed"
    elif ets == 3:
        print("ekey 3 - invalid operation")
        #invalid()
        return "invalid"
    else:
        #invalid()
        return "invalid"


def lock():
    file = input("What file to lock? ")
    password = input("What password to lock it with? ")
    
    file = open(file + ".pass", "a+")
    file = open(file + ".pass", "w")
    file.write(password)
    
    file.close()
    
    print(file + ".pass has been locked.")