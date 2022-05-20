#                               Morse Encoder And Decoder
# Morse Code is made by Samual Morse To communicate with someone else.
#Morse Code Is made by just Two Charectors:  Dots and Dashes   ( . _ )

import subprocess
from time import sleep
import os
import random
from gpiozero import LED

morse = { 
        'A':'._', 
        'B':'_...',
		'C':'_._.', 
        'D':'_..', 
        'E':'.',
		'F':'.._.', 
        'G':'_.', 
        'H':'....',
		'I':'..', 
        'J':'._', 
        'K':'_._',
        'L':'._..', 
        'M':'__',
        'N':'_.',
	    'O':'_', 
        'P':'._.', 
        'Q':'_._',	
        'R':'._.', 
        'S':'...', 
        'T':'_',
        'U':'.._', 
        'V':'..._', 
        'W':'._',
		'X':'_.._', 
        'Y':'_._', 
        'Z':'_..',
		'1':'._', 
        '2':'.._', 
        '3':'..._',
		'4':'...._', 
        '5':'.....', 
        '6':'_....',
		'7':'_...', 
        '8':'_..', 
        '9':'_.',
		'0':'_', 
        ',':'_.._', 
        '.':'._._._',
		'?':'.._..', 
        '/':'_.._.', 
        '-':'_...._',
		'(':'_._.',
        ')':'_._._',
        ' ':' ',
        '\n':'    ',
        '!':'-.-.--'
    }



def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += morse[letter] + " "
		else:
			cipher += morse[letter] + "  "

	return cipher


def play(message):
    buz = LED(25)
    for letter in message:
        if letter == " ":
            sleep(1)
            print(letter)
        if letter == "  ":
            sleep(1)
            print(letter)
        if letter == ".":
            buz.on()
            sleep(0.2)
            buz.off()
            print(letter)
        if letter == "_":
            buz.on()
            sleep(0.4)
            buz.off()
            print(letter)



def main():
    subprocess.run("clear", shell=True)
    print("\n\n****************** Morse Code Decoder And Encoder ******************\n")
    ask1 = input("\nDo you want to Encode Or Decode or other options[E / D / O]: ")
    if ask1 == "E":
        if os.path.exists("txt1"):
            os.remove("txt1")
        print("\nEnter The text You want in the editor. \nAnd press [ ctrl + s ] to save it and close the editor.\nThen press enter key here.")
        sleep(1)
        f1 = open("txt1", "x")   #This will create a file and open it for editing in a graphical text editor.
        subprocess.run("/usr/bin/mousepad ./txt1 &> /dev/null &", shell=True)
        sleep(2)
        subprocess.run("clear", shell=True)
        ask2 = input("\nIf you have finished Typing You text press Enter Here: ")
        if ask2 == "":
            f2 = open("txt1", "r")
            txt = f2.read()
            print(" \nThis is the text You wrote:\n\n", txt, "\n\n")
            print("Your text in Morse Code: \n\n")
            E = encrypt(txt.upper())
            print(E)
            play(E)
            x = list(random.sample(range(1, 100), 1))
            m = str(x[0])
            n = str("./saved/txt" + m)
            print("\n\nYour Text is saved as " + n + " in this folder.\n\nThank You\n")
            f3 = open(n , "w")
            f3.write(E)
            f3.close()
            f2.close()
            sleep(10)
            subprocess.run("clear", shell=True)
            main()
    if ask1 == "D":
        print("pending")



main()



