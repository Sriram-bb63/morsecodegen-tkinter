#Importing required modules
from tkinter import Tk, Label, Button, Text, END
from winsound import Beep
from time import sleep

#Morse translator function
def morsetranslate():
    msg=box.get('1.0', END)

    #Defining freq and duration
    f=2250      #Frequncy
    d1=250      #Short beep
    d2=650      #Long beep
    d3=0        #End gap bw letters

    #Converting to lower case
    msg=msg.lower()

    #Assigning values in dictionary
    dic={
        "a":[d3,d1,d2],
        "b":[d3,d2,d1,d1,d1],
        "c":[d3,d2,d1,d2,d1],
        "d":[d3,d2,d1,d1],
        "e":[d3,d1],
        "f":[d3,d1,d1,d2,d1],
        "g":[d3,d2,d2,d1],
        "h":[d3,d1,d1,d1,d1],
        "i":[d3,d1,d1],
        "j":[d3,d1,d2,d2,d2],
        "k":[d3,d2,d1,d2],
        "l":[d3,d1,d2,d1,d1],
        "m":[d3,d2,d2],
        "n":[d3,d2,d1],
        "o":[d3,d2,d2,d2],
        "p":[d3,d1,d2,d2,d1],
        "q":[d3,d2,d2,d1,d2],
        "r":[d3,d1,d2,d1],
        "s":[d3,d1,d1,d1],
        "t":[d3,d2],
        "u":[d3,d1,d1,d2],
        "v":[d3,d1,d1,d1,d2],
        "w":[d3,d1,d2,d2],
        "x":[d3,d2,d1,d1,d2],
        "y":[d3,d2,d1,d2,d2],
        "z":[d3,d2,d2,d1,d1],
        "1":[d3,d1,d2,d2,d2,d2],
        "2":[d3,d1,d1,d2,d2,d2],
        "3":[d3,d1,d1,d1,d2,d2],
        "4":[d3,d1,d1,d1,d1,d2],
        "5":[d3,d1,d1,d1,d1,d1],
        "6":[d3,d2,d1,d1,d1,d1],
        "7":[d3,d2,d2,d1,d1,d1],
        "8":[d3,d2,d2,d2,d1,d1],
        "9":[d3,d2,d2,d2,d2,d1],
        "0":[d3,d2,d2,d2,d2,d2],
        ".":[d3,d1,d2,d1,d2,d1,d2],
        ",":[d3,d2,d2,d1,d1,d2,d2],
        "?":[d3,d1,d1,d2,d2,d1,d1],
        "'":[d3,d1,d2,d2,d2,d2,d1],
        "!":[d3,d2,d1,d2,d1,d2,d2],
        "/":[d3,d2,d1,d1,d2,d1],
        "(":[d3,d2,d1,d2,d2,d1],
        ")":[d3,d2,d1,d2,d2,d1,d2],
        "&":[d3,d1,d2,d1,d1,d1],
        ":":[d3,d2,d2,d2,d1,d1,d1],
        ";":[d3,d2,d1,d2,d1,d2,d1],
        "=":[d3,d2,d1,d1,d1,d2],
        "+":[d3,d1,d2,d1,d2,d1],
        "-":[d3,d2,d1,d1,d1,d1,d2],
        "_":[d3,d1,d1,d2,d2,d1,d2],
        "\"":[d3,d1,d2,d1,d1,d2,d1],
        "@":[d3,d1,d2,d2,d1,d2,d1]}

    for i in range(len(msg)):
        print(msg[i])
        if msg[i]==" ":
            sleep(5)
        elif msg[i] in dic:
            lst=dic[msg[i]]
            for j in range(len(lst)):
                if lst[j]!=0:
                    Beep(f,lst[j])
                else:
                    sleep(3)
        elif msg[i]=="\n":
            pass
        else:
            pass

#Creating window
root=Tk()
root.geometry("265x150")

#Title
root.title("Morse generator")

#Setting the bg color to grey
root['bg']='#3b3b3b'

#Heading
head=Label(root, text="Morse code generator", bg='#3b3b3b', fg='white')
head.grid(row=0, column=0)

#Entry prompter
entrytext=Label(root, text="Enter your message:", bg='#3b3b3b', fg='white')
entrytext.grid(row=1, column=0)

#Entry
box=Text(root, width=30, height=3, bg='#bfbfbf', fg='black')
box.grid(row=2, column=0, padx=10)

#Go button
convert=Button(root, text="Translate", command=morsetranslate)
convert.grid(row=4, column=0, pady=15)

#mainlooping window
root.mainloop()
