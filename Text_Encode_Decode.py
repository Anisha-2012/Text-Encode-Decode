#importing modules
from tkinter import *
import base64
 
#initializing the display window
root = Tk()
root.geometry('700x400')
root.resizable(0,0)
root.configure(bg = 'cyan')

#title of the window
root.title("MessageMagic - Message Encode and Decode")

#label
Label(root, text ='Encode & Deco1de',bg='cyan',fg = '#660029', font = 'arial 20 bold').pack(side='top')
Label(root, text ='MessageMagic',bg='cyan',fg='teal', font = 'arial 17 bold').pack(side =BOTTOM)

#define variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# Defining the needed functions
#Function to encode
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#Function to decode
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#Function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode!')

#Function to exit window
def Exit():
    root.destroy()

#Function to reset window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# Designing the labels and buttons
#Message
Label(root, font= 'arial 15 bold', text='Message',bg = 'cyan',fg='blue').place(x= 70,y=60)
Entry(root, font = 'arial 13', textvariable = Text, bg = 'steelblue', fg = 'white',width=25).place(x=360, y = 60)

#key
Label(root, font = 'arial 15 bold', text ='Key',bg = 'cyan',fg='blue').place(x=70, y = 100)
Entry(root, font = 'arial 13', textvariable = private_key , bg ='steelblue',fg='white',width=25).place(x=360, y = 100)

#mode
Label(root, font = 'arial 15 bold', text ='Mode (e-encode, d-decode)',bg = 'cyan',fg='blue').place(x=70, y = 140)
Entry(root, font = 'arial 13', textvariable = mode , bg ='steelblue',fg='white',width=25).place(x=360, y = 140)

#result
Entry(root, font = 'arial 13 bold', textvariable = Result, bg ='steelblue',fg='white',width=25).place(x=360, y = 180)

#result button
Button(root, font = 'arial 12 bold', text = 'RESULT' ,width = 10 ,padx = 2,pady = 2,bg ='LimeGreen',fg="black" ,command = Mode).place(x=70, y = 180)

#reset button
Button(root, font = 'arial 12 bold' ,text ='RESET' ,width =10, command = Reset,bg = '#cc00ff',fg = 'black', padx=2,pady=2).place(x=200, y = 250)

#exit button
Button(root, font = 'arial 12 bold',text= 'EXIT' , width = 10 ,command = Exit,bg = 'OrangeRed',fg = 'black', padx=2, pady=2).place(x=340, y = 250)
root.mainloop()















