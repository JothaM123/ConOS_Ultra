import os,winsound,colorama,wikipedia,keyboard,time,ascii_magic

#=======init=============
colorama.init()

#=======functions========
def ring():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    print("\n")

def add(n1,n2):
    print(n1+n2)
    print("\n")

def subtract(n1,n2):
    print(n1-n2)
    print("\n")

def multiply(n1,n2):
    print(n1*n2)
    print("\n")

def divide(n1,n2):
    print(n1/n2)
    print("\n")

def tyme():
    t = time.localtime()
    ctime = time.strftime("%H:%M", t) 
    print(ctime) 

def wiki(term):
    wik = wikipedia.summary(term)
    print("\n"+wik+"\n")

def py():
    while 1:
        cmdrun=input("\nEnter Python Code\n>>>")
        exec(cmdrun)

def beep(num, dur):
    winsound.Beep(num, dur)

def img2ascii(img):
    image = ascii_magic.from_image_file(img)
    ascii_magic.to_terminal(image)
    print("\n")
  

#======fullscreen========

keyboard.press("F11")

#======flash-screen======

print("""
╭────────────────────────────────────╮
│                                    │
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐    ┌  ┐  │
│  │    │  │ │  │ │  │ │  │    │  │  │
│  │    │  │ │  │ │  │ └──┐    │  │  │
│  │    │  │ │  │ │  │    │    │  │  │
│  └──┘ └──┘ ┴  ┴ └──┘ └──┘    └──┘  │
│                                    │
╰────────────────────────────────────╯
Loading ConOS Ultra ...
""")
winsound.Beep(1000,500)
time.sleep(2)
os.system("cls")


#======header============
print(colorama.Fore.GREEN+"\n\nConOS v1.0")
print("="*os.get_terminal_size().columns)
print("""
╭─AVAILABLE COMMANDS─────────╮
│                            │
│ - add(n1,n2)               │
│ - beep(num, dur)           │
│ - divide(n1,n2)            │
│ - img2ascii(img)           │
│ - multiply(n1,n2)          │
│ - subtract(n1,n2)          │
│ - py()                     │
│ - ring()                   │
│ - tyme()                   │
│ - wiki()                   │
╰────────────────────────────╯
""")


#======evaluate commands======
while True:
    command = input("Enter command - ")
    print()
    try:
        exec(command)

        input("Press [Enter to continue]")
        os.system("cls")
        
        print("\n\nConOS Ultra")
        print("="*os.get_terminal_size().columns)
        print(+"""  
╭─AVAILABLE COMMANDS─────────╮
│                            │
│ - add(n1,n2)               │
│ - beep(num, dur)           │
│ - divide(n1,n2)            │
│ - img2ascii(img)           │
│ - multiply(n1,n2)          │
│ - subtract(n1,n2)          │
│ - py()                     │
│ - ring()                   │
│ - tyme()                   │
│ - wiki()                   │
╰────────────────────────────╯""")
    
    except:
        print(colorama.Fore.RED+"Error, try again!\n"+colorama.Fore.GREEN)
        input("Press [Enter] to continue ")
        os.system("cls")
        
        print("\n\nConOS v1.0")
        print("="*os.get_terminal_size().columns)
        print("""  
╭─AVAILABLE COMMANDS─────────╮
│                            │
│ - add(n1,n2)               │
│ - beep(num, dur)           │
│ - divide(n1,n2)            │
│ - img2ascii(img)           │
│ - multiply(n1,n2)          │
│ - subtract(n1,n2)          │
│ - py()                     │
│ - ring()                   │
│ - tyme()                   │
│ - wiki()                   │
╰────────────────────────────╯""")
        