from random import randint

#import getpass # not used
#import glob # not used
import os
import tkinter
import time
import turtle

# modules
import modules.sound as sound
import modules.graphics as graphics
import modules.functions as functions

# global variables
f = None
s = ''
bg = ''
text = ''
wav1 = ''
wav2 = ''
ver = ''
et = -1
math = -1
lock = -1
beep = -1
command = ''

drive = ''
home = ''
path = ''
predir = ''

def mussym(col1, col2):
    turtle.pu()
    turtle.goto(-100, 100)
    turtle.pencolor(col1)
    turtle.write("Wav", move="True", align="left", font=("Arial", 30, "bold"))
    turtle.pencolor(col2)
    turtle.write("Read", move="True", align="left", font=("Arial", 30, 'bold'))


def logo():
    graphics.pg("L", 1, 25, "bold")
    graphics.pg("L-", 1, 25, 'bold')
    graphics.pg("L-D", 1, 25, 'bold')
    graphics.pg('L-DO', 1, 25, 'bold')
    graphics.pg('L-DOS', 1, 25, 'bold')
    for i in range(10):
        graphics.pg('', 0.1, 25, 'bold')
        graphics.pg('L-DOS', 0.1, 25, 'bold')
    graphics.pg('', 0, 25, '')

def update():
    import tkinter.messagebox
    sound.PlayBeep(700, 1000)
    print("This software reqires a newer version of L-DOS.")
    graphics.pg("This software requires a newer version of L-DOS.", 5, 24, "bold")


def startup():
    filename = 'g_boot.wav'
    sound.PlaySound(filename)


def winerr():
    filename = 'g_error.wav'
    sound.PlaySound(filename)

def not_installed():
    sound.invalid_beep()
    print("This software is not installed. Install it through fshop.")
    graphics.pg("""This software is not installed. Install it through fshop.""", 5, 45, "bold")


def invalid():
    sound.invalid_beep()
    print("What you have inputted is invalid.")
    graphics.pg("""What you have inputted is invalid.""", 5, 45, "bold")


def boot():
    global f
    global s
    global bg
    global text
    global wav1
    global wav2
    global ver
    global et
    global math
    global lock
    global beep
    global command
    
    f = open("aero.ldos", 'r')
    s = f.read()
    bg='#' + s[0:6]
    text='#' + s[7:13]
    wav1='#' + s[14:20]
    wav2='#' + s[21:29]
    ver = "0.1.3"
    et = 0
    math = 0
    lock = 0
    beep = 0
    command = "N/A"
    
    # EDIT -- removed imports
    turtle.pencolor(text)
    turtle.bgcolor(bg)
    
    print("Booting L-DOS " + ver + "...")
    print("Finalizing...")
    print("L-DOS " + ver + " has booted. Loading command prompt...")

def shell():
    global f
    global s
    global bg
    global text
    global wav1
    global wav2
    global ver
    global et
    global math
    global lock
    global beep
    global command
    
    global drive
    global home
    global path
    global predir
    
    drive = "C:/"
    home = os.getcwd()
    path = home
    predir = home
    
    logo()
    startup()
    graphics.ttext()
    
    print("A second window has been opened for graphical capability.")
    print("If a program requires graphics, open the secondary window.")
    print("Make sure L-DOS Folder is on the desktop.")
    print("L-DOS requires a version of Microsoft Windows.")
    
    sound.PlayBeep(1000, 1000)
    
    while 1 == 1:
        turtle.bgcolor(bg)
        turtle.pencolor(text)
        
        lCom = command
        
        turtle.pu()
        turtle.goto(0, 0)
        turtle.pd()
        turtle.clear()
        
        graphics.ttext()
        
        turtle.write("Last Command: " + lCom, align = "center", font = ("Arial", 10, "normal"))
        
        command = input(drive)
        sound.confirm_beep()
        
        if command == "break":
            break
        if drive == "C:/":
            if command == "print":
                toPrint = input("")
                print(toPrint)
            if command == "help":
                print("""
                L-DOS HELP
                ----------
                Welcome to L-DOS, an OS programmed in Python!
                Python has basic input and output commands, which
                is perfect for a DOS-based operating system.
                ----------
                COMMANDS
                ----------
                break: returns you to python prompt
                print: echoes what you say
                update: updates L-DOS
                version: shows version
                fshop: function shop
                fshop /nw: function shop without delays
                pgui: prints to the gui
                graphic: GUI
                graphic /nw: GUI without delays
                file: text editor and reader
                wavread: plays a wav file
                dir: shows directory
                cd: change directory
                pd: previous directory
                nd: new directory
                dirs: searches for anything
                ----------
                FSHOP HELP
                ----------
                NOTE: FSHOP DOES NOT CONNECT TO THE INTERNET. ALL DOWNLOADS
                ARE FAKE AND CAN BE SKIPPED BY USING THE /nw TAG.
                ----------
                fshop: opens function shop
                example interface:
                1. option 1
                2. option 2
                3. option 3
                ect.
                choice: []
                select whatever you want
                1. math.exe
                2. lock.exe
                3. etest.exe
                choice: 3
                install etest? y/n
                []
                type y to install
                install etest? y/n
                y
                installing etest...
                installed successfully.
                launch program:
                C:/etest
                [program]
                ----------
                Thank you for downloading L-DOS.
                ----------
                NOTE: Scroll up to view all of help.""")
                sound.error_beep()
            if command == "p-lang" or command == "plang":
                update()
            if command == "doc" or command == "docedit":
                update()
            if command == "A:/" or "A:" or "A":
                drive = "A:/"
            if command == "B:/" or "B:" or "B":
                drive = "B:/"
            if command == "C:/" or "C:" or "C":
                drive = "C:/"
            if command == "update":
                print("Loading L-DOS Setup...")
                print("""
                L-DOS is loading...
                L-DOS is now rebooting...""")
                
                time.sleep(1)
                
                print("L-DOS Update is not available. Rebooting...")
                
                time.sleep(0.1)
                
                print("Reboot initalized...")
                print("Reboot cancelled.")
                sound.error_beep()
            if command == "version":
                print("You are running L-DOS version " + ver + ".")
            if command == "etest":
                if et == 1:
                    retval = functions.etest()
                    
                    if retval == "update":
                        print("Please update to a newer version of L-DOS!")
                    elif retval == "not_installed":
                        not_installed()
                    elif retval == "invalid":
                        invalid()
                    else:
                        invalid()
                else:
                    not_installed()
            if command == "beep":
                if beep == 1:
                    bp = int(input("Beep Pitch: "))
                    bl = int(input("Beep Length: "))
                    
                    sound.PlayBeep(bp, bl)
                else:
                    not_installed()
            if command == "fshop /nw":
                print("Loading Function Shop...")
                print("""
                Function Shop
                -----------
                1. math.exe
                2. lock.exe
                3. etest.exe
                4. beep.exe
                5. bonusGui.exe
                -----------""")
                
                choice1 = input("Insert choice: ")
                
                sound.confirm_beep()
                
                if choice1 == "1":
                    print("Install math?")
                    if input() == "y" or "Y":
                        sound.confirm_beep()
                        print("Installing math function...")
                        print("Math has been installed successfully.")
                        math = 1
                elif choice1 == "2":
                    print ("Install lock?")
                    if input() == "y" or "Y":
                        sound.confirm_beep()
                        print("Installing lock...")
                        print("Lock has been installed successfully.")
                        lock = 1
                elif choice1 == "3":
                    print("Install error tester?")
                    if input() == "y" or "Y":
                        sound.confirm_beep()
                        print("Installing error test...")
                        print("Error tester has been installed successfully.")
                        et = 1
                elif choice1 == "4":
                    print("Install beep?")
                    if input() == "y" or "Y":
                        sound.confirm_beep()
                        print("Installing beep...")
                        beep = 1
                        print("Beep has been installed successfully.")
                elif choice1 == "5":
                    print("Install Bonus GUI?")
                    if input() == "y" or "Y":
                        sound.confirm_beep()
                        print("Installing bonus GUI...")
                        sound.error_beep()
                        print("First attempt failed.")
                        sound.error_beep()
                        print("Second attempt failed. Trying final time...")
                        sound.error_beep()
                        print("Third attempt failed. Cannot download bonusGui.exe.")
                else:
                    invalid()
                    sound.confirm_beep()
            if command == "pgui":
                graphics.pgui(input("What to print to GUI: "), "Arial")
            if command == "graphic":
                print("Direct your attention to the Graphical Interface.")
                startup()
                graphics.pg("Welcome to L-DOS Graphic!", 2, 25, 'bold')
                graphics.pg('''L-DOS Graphic is not fully complete yet. Please consider this when using L-DOS Graphic.''', 5, 25, 'bold')
            if command == "file":
                choice = input("""
                What do you want to do with file manager?
                1. Open file
                2. Create file
                3. Edit existing file
                """)
                if choice == "1":
                    file = input("Please input filename: ")
                    f = open(file, "r")
                    con = f.read()
                    print(con)
                    graphics.pg(con, 5, 10, 'bold')
                elif choice == "2":
                    file = input("What to name this file? ")
                    f = open(file, 'w+')
                elif choice == "3":
                    file = input("What file to edit? ")
                    edit = input("What to add? ")
                    f = open(file, 'a+')
                    f.write(edit)
            if command == "sound":
                snd = input("Input integer ID: ")
                if snd == "1":
                    print("GUI Logon Noise")
                    startup()
                elif snd == "2":
                    print("Error Sound")
                    winerr()
            if command == "guiprint":
                tp = input("What to print on-screen? ")
                fnt = input("What font to use? ")
                graphics.pgui(tp, fnt)
            if 'wavread' in command:
                filename = command[8:len(command)]
                if not '.wav' in command:
                    filename = filename + ".wav"
                print("Playing " + filename)
                graphics.pg(filename, 0, 30, "bold")
                mussym(wav1, wav2)
                sound.PlaySound(filename)
            if command == "dir":
                for x in os.listdir('.'):
                    print(x)
            if "cd" in command:
                predir = os.getcwd()
                os.chdir(command[3:len(command)])
            if command == "pd":
                os.chdir(predir)
            if command == "nd":
                dirname = input("What to name directory?")
                os.makedirs(dirname)
            if command == "":
                invalid()
            if command == "credits":
                print("Lim Industries L-DOS")
                graphics.pg("Lim Industries L-DOS", 1, 12, "bold")
                sound.confirm_beep()
                print("Created by Lim95")
                graphics.pg("Created by Lim95", 1, 12, "bold")
                sound.confirm_beep()
                print("Programmed in Python 3.0")
                graphics.pg("Programmed in Python 3.0", 1, 12, "bold")
                sound.confirm_beep()
                print("Music from Friday Night Funkin'")
                graphics.pg("Music from Friday Night Funkin'", 1, 12, "bold")
                sound.confirm_beep()
                print("GUI Boot Sound from Windows 95")
                graphics.pg("GUI Boot Sound from Windows 95", 1, 12, "bold")
                sound.confirm_beep()
                print("Thanks for using L-DOS!")
                graphics.pg("Thanks for using L-DOS!", 5, 12, "bold")
                sound.error_beep()
            if command == "lib":
                print("""
                L-DOS v0.1.0 uses the following Pythin libraries:
                Turtle [GUI]
                Time [DELAY]
                Random [LOCK]
                Winsound [BEEP]
                OS [FILES]
                Getpass [USER DIRECTORY]
                Glob [SEARCH]""")
                theme = "L"
            if command == "math":
                if math == 1:
                    functions.math()
                else:
                    not_installed()
            if command == "lock":
                if lock == 1:
                    functions.lock()
                else:
                    not_installed()
            if 'dirs' in command:
                for x in os.listdir('.'):
                    if command[5:len(command)] in x:
                        print(x)
            if 'open' in command:
                if '.wav' in command[5:len(command)]:
                    print("Use wavread to open this file.")
                else:
                    file = command[5:len(command)]
                    f = open(file, "r")
                    con = f.read()
                    print(con)
                    graphics.pg(con, 5, 10, 'bold')
            if command == 'theme':
                print("Welcome to Theme Manager!")
                
                cmd = input("""What do you want to do here?
                1. Change theme
                2. Restore default theme
                3. Restore Backed Up Theme
                Input choice here: """)
                
                if cmd == "1":
                    f = open("tbackup.ldos", "w")
                    f.write(str(bg + '/' + text + '/' + wav1 + '/' + wav2))
                    bg = '#' + input("Background? Use a hex value (xxxxxx). ")
                    text = '#' + input("Text color? Use a hex value (xxxxxx). ")
                    wav1 = '#' + input("Wav? Use a hex value (xxxxxx). ")
                    wav2 = '#' + input("Read? Use a hex value (xxxxxx). ")
                    f = open("theme.ldos", 'w')
                    f.write(str(bg + '/' + text + '/' + wav1 + '/' + wav2))
                elif cmd == "2":
                    bg = "#FFFFFF"
                    text= "#000000"
                    wav1 = "#0062ff"
                    wav2 = "#d4ff00"
                elif cmd == '3':
                    f = open("tbackup.ldos", 'r')
                    s = f.read()
                    bg='#' + s[0:6]
                    text='#' + s[7:13]
                    wav1='#' + s[14:20]
                    wav2='#' + s[21:29]       
                else:
                    invalid()
            if command == "story":
                print("Welcome! This is basically Mad Libs.")
                name = input("Name: ")
                noun1 = input("Noun: ")
                noun2 = input("Noun: ")
                noun3 = input("Noun: ")
                verb = input("Verb ending in -ing: ")
                adj = input("Adjective: ")
                print("Ok! Compiling story...")
                time.sleep(0.5)
                input("Story compiled! Press enter to read it.")
                print("Once, a person named " + name + " went to the gym.")
                print("Once " + name + " got on the " + noun1 + ", they started to exercise.")
                print("After they were done with the " + noun1 + ", they started to use a " + noun2 + ".")
                print("For the other people, this was a sight to behold. " + name + " using a " + noun2 + "?!")
                print("Then " + name + " finished with the " + noun2 + ". " + name + " got on a " + noun3 + " and started " + verb + "!")
                print("Someone asked, '" + name + ", is that how you're supposed to use a " + noun3 + "?'")
                print(name + " replied, 'Of course! This is the secret use of any " + noun3 + "!'")
                print("This day became imfamous as 'The Day that " + name + " used a " + noun3 + " wrong.'")
                print("The end!")
            if command == "guitest":
                t = input("Input integer key... ")
                if t == "1":
                    logo()
                    startup()
                elif t == "2":
                    mussym(wav1, wav2)
                elif t == "3":
                    not_installed()
                elif t == '4':
                    invalid()
                elif t == "5":
                    graphics.pg("hdntstmsg", 1, 25, 'bold')
                elif t == '6':
                    graphics.pgui('hdntstmsg', 'Comic Sans MS')
                else:
                    invalid()
            if command == "whatsnew" or command == "patchnotes":
                print("""
                L-DOS v0.1.3 Patch Notes
                -----
                Fixed Bugs
                Added a New Game
                Added some More Themes""")
            if command == 'settle':
                itm1 = input("What do you think is good? ")
                itm2 = input("What does your friend think is good? ")
                
                cho = randint(1, 2)
                
                if cho == 1:
                    print("Oh yeah, " + itm1 + " is WAAAAAAY better than " + itm2 + ".")
                else:
                    print("Definitley, " + itm2 + " is the best.")
            if command == "colors":
                print(bg)
                print(text)
                print(wav1)
                print(wav2)
            if command == "copy":
                f1 = open(input("What file to copy from? "), 'r')
                f2 = input("What file to copy to? ")
                f = open(f2, "w")
                f.write(f1.read())
            if "getcol" in command:
                col = command[7:len(command)]
                if col == "red" or col == "Red":
                    print("ff0000")
                elif col == "orange" or col == "Orange":
                    print("ff8400")
                elif col == "yellow" or col == "Yellow":
                    print("eeff00")
                elif col == "green" or col == "Green":
                    print("00ff08")
                elif col == "blue" or col == "Blue":
                    print("008cff")
                elif col == "purple" or col == "Purple":
                    print("9d00ff")
                elif col == "pink" or col == "Pink":
                    print("ff00e1")
                elif col == "black" or col == "Black":
                    print("000000")
                elif col == "white" or col == "White":
                    print("FFFFFF")
                else:
                    print("Visit this link: https://www.google.com/search?client=firefox-b-1-d&q=hex+color+picker")


def main():
    boot()
    shell()


main()