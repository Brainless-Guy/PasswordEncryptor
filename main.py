import tkinter as tk
import requests,os
import logging,threading
from PIL import Image,ImageTk
import tkinter.messagebox as msg
from assets.psscode import run
from assets.hasher import check
import book


# API USAGE : basically forms a code in localhost:5000/generate 

def flask_run(stop :bool):
    logging.basicConfig(level=logging.ERROR)
    
    run()
        
# Makes the Code Run without Logs of Flash In console enabling the tkinter GUI to run Properly!
def api():
    thread = False
    flask_thread = threading.Thread(target=flask_run,args=(lambda : thread,))
    flask_thread.daemon = True
    flask_thread.start()
    

    
# Didn't Find a Good Word but It does the thing, Checks If We are logging by Hashing Method or the "API" method  
def HallCode(e = None):
    if strhash.get() == 1:
        code = requests.get(url="http://127.0.0.1:5000/generate").json()
        if entry.get() == code['code']:
            msg.showinfo("Logged IN",'You Are Logged IN')
            root.destroy(            )
            
            book.passbook()
        else:
            msg.showwarning(msg.WARNING,"Wrong")
            root.destroy()
            
    elif strhash.get() == 2:
        
        if check(entry.get()) == True:
            msg.showinfo("Logged IN",'You Are Logged IN')
            root.destroy()
            book.passbook()
        else:
            msg.showwarning(msg.WARNING,"Wrong")
            root.destroy()
# Animation For The Lock           
def unlock_anim(e = None):
    global unlock
    entryButton.config(image=unlock,background="#95D2B3",border=0,highlightthickness=0,activebackground="#D8EFD3",command=HallCode)
resetbutton = lambda x : entryButton.config(image=image,background="#95D2B3",border=0,activebackground="#D8EFD3",command=HallCode)
def coloranim(e =None):
    entry.config(textvariable=passcode,background='#55AD9B',width=44,font=("System",15))  
    (entryButton.config(image=image,background="#55AD9B",border=0,activebackground="#D8EFD3",command=HallCode)) 
def resetanim(e=None):
    entry.config(textvariable=passcode,background='#95D2B3',width=44,font=("System",15))  
    (entryButton.config(image=image,background="#95D2B3",border=0,activebackground="#D8EFD3",command=HallCode))
root = tk.Tk()
Width = 569
Height = 423

root.geometry("569x423")
root.maxsize(Width,Height-150)

root.bell()

root.title('PASSBOOK')
root.iconbitmap("assets/key.ico")
# Passcode


root.config(background="#D8EFD3")

password = tk.Label(root,text="PASSWORD :",background ='#D8EFD3',foreground='#55AD9B',font=("fixedsys",29,))
password.place(x=190,y=32)

passcode = tk.StringVar()


entry = tk.Entry(textvariable=passcode,background='#95D2B3',width=44,font=("System",15),show='*')
entry.place(height=40,x=110,y=120)

entry.bind('<Enter>',coloranim)
entry.bind('<Leave>',resetanim)
image = ImageTk.PhotoImage(image=Image.open("assets/lock.png"))
entryButton = tk.Button(image=image,background="#95D2B3",border=0,activebackground="#D8EFD3",command=HallCode)
entryButton.place(x=470,y=122.8)
unlock = ImageTk.PhotoImage(image=Image.open("assets/unlock.png"))


strhash = tk.IntVar()
strhash.set(2)
# Used Alot of Icons , HOOF~!
ico1 = ImageTk.PhotoImage(image=Image.open("assets/radiobutton.png").resize(size=(50,40)))
ico2 = ImageTk.PhotoImage(image=Image.open("assets/checked.png").resize(size=(52,40)))
radio_api = tk.Radiobutton(root,font=("System",10),variable=strhash,value=1,border=0,indicatoron=False,image=ico1,bg='#D8EFD3',highlightbackground='#D8EFD3',activebackground='#D8EFD3',selectimage=ico2,selectcolor='#D8EFD3',command=api)
radio_hash= tk.Radiobutton(root,variable=strhash,value=2,font=("System",10),text="Hash",border=0,indicatoron=False,image=ico1,bg='#D8EFD3',highlightbackground='#D8EFD3',activebackground='#D8EFD3',selectimage=ico2,selectcolor='#D8EFD3')
radio_api.place(x=150,y=200)
radio_hash.place(x=350,y=200)
label1 = tk.Label(text="API",font=('fixedsys',19),background='#D8EFD3',fg='#55AD9B').place(x=200,y=200)
label2 = tk.Label(text="HASH",font=('fixedsys',19),background='#D8EFD3',foreground='#55AD9B').place(x=400,y=200)




entryButton.bind("<Enter>",unlock_anim)
entryButton.bind("<Leave>",resetbutton)

root.mainloop()

