import tkinter as tk
from PIL import ImageTk,Image
import tkinter.messagebox as msg
import  tkinter.filedialog as fd
from assets.hasher import cipher,decipher,hasher
import os

# A function that would be called in main.py
def passbook():
    # Animations
    anim_ = lambda e :   password1.config(width=50,textvariable=password,foreground='#222831',background='#36C2CE',font=('Modern',14,'bold'))
    anim2_ = lambda e : email1.config(width=50,textvariable=email,foreground='#222831',background='#36C2CE',font=('Modern',14,'bold'))
    __anim = lambda e: password1.config(width=50,textvariable=password,foreground='#222831',background='#478CCF',font=('Modern',14,'bold'))
    __anim2 = lambda e: email1.config(width=50,textvariable=email,foreground='#222831',background='#478CCF',font=('Modern',14,'bold'))
    ___anim =  lambda e: Label.config(text="PASSWORD SAVER",font=('fixedsys',23),bg='#222831',compound="top",fg="#478CCF",highlightcolor='#222831',activebackground='#478CCF')
    l___anim = lambda e : Label.config(text="PASSWORD SAVER",font=('fixedsys',23),fg='#00ADB5',compound="top",bg="#222831")
    __defaultpath__ = "encrypted_file.txt"
    __defaulthashpath_ = "hash.txt"
    
    # to change pass hash
   
    def changepass():
        def hashpath(): # dropped this idea
            if os.path.exists("hash_path.txt"):
                
                with open("hash_path.txt", "r") as file:
                    
                    if (file.read().strip()) == '':
                        s = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],title="choose your hash file location:")
                        with open("hash_path.txt", "w") as file:
                            file.write(cipher(s))
                        return s
                    else:
                        with open("hash_path.txt", "r") as file:
                            return decipher(file.read().strip(""))        
            else:
                        s = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],title="choose your hash file location:")
                        with open("hash_path.txt", "w") as file:
                            file.write(cipher(s))
                        return s
        l__1anim = lambda e: passchange.config(text="Change >",font=("fixedsys",14),fg='#00ADB5',compound="top",bg="#222831")
        __1anim = lambda e: passchange.config(text="Change >",font=('fixedsys',23),bg='#222831',compound="top",fg="#478CCF",highlightcolor='#222831',activebackground='#478CCF')
        
        # def load2():
        #     with open("hash_path.txt","w") as dir:
        #         s = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],title="choose a text file to Store HASH!")
        #         dir.write(cipher(s))
        

        
        def changepasscode(e):
            
            with open('hash.txt',"w") as hash:
                hash.write(cipher(hasher(Pass1.get().strip())))
                window2.destroy()
            
        
        window2 = tk.Tk()
        window2.config(bg ="#222831")
        window2.iconbitmap('assets/key.ico')
        window2.title('Change Password')
        window2.geometry('300x100')
        Pass1 = tk.StringVar(window2)
        passchange = tk.Label(window2,text="Change >",font=("fixedsys",14),fg='#00ADB5',compound="top",bg="#222831")
        passchange.place(x=10,y=10)
        PassEntry=tk.Entry(window2,width=30,textvariable=Pass1,foreground='#222831',background='#478CCF',font=('Modern',14,'bold'))
        PassEntry.place(x=10,y=50)
        passchange.bind('<Enter>',__1anim)
        passchange.bind("<Leave>",l__1anim)
        passchange.bind("<Button-1>",changepasscode)
        # button2 = tk.Button(window2,text="path",command=load2)
        # button2.place(x=250,y=10)
        window2.mainloop()

    # to Get the text file
    def pathapp():
        if os.path.exists("file_path.txt"):
            
            with open("file_path.txt", "r") as file:
                
                if (file.read().strip()) == '':
                    s = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                    with open("file_path.txt", "w") as file:
                        file.write(s)
                    return s
                else:
                    with open("file_path.txt", "r") as file:
                        return file.read().strip("")        
        else:
                    s = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                    with open("file_path.txt", "w") as file:
                        file.write(s)
                    return s
    # Text File Load Button Function
    def load():
        with open("file_path.txt","w") as dir:
            s = fd.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],title="choose a text file!")
            dir.write((s))
    # Passwords:
    def decryption(e = None):
        def edit(e=None):
            text.config(font=("fixedsys",15),state="normal")
        # Save Button In Menubar
        def save(e =  None):
            key ={}
            s_ = text.get(index1=1.0,index2=tk.END)
            text.config(font=("fixedsys",15),state="disabled")
            
            if s_.strip() != '':
                s_ = s_.strip().split('\n')
                for i in range(0,len(s_)):
            
                    key1,key2 = s_[i].strip().split(':')

                    key[cipher(key1)]=cipher(key2)
                
                file_cleared = False
                for code1,code2 in key.items():    
                        
                        with open(pathapp(),'a') as save:
                                if not file_cleared:
                                    open(pathapp(), 'w').close()
                                    file_cleared = True
                                s__ = f'\n{code1}:{code2}'
                                save.write(s__)
            else:
                 with open(pathapp(),'w') as save:
                      pass
        # GUI to show ciphered codes in deciphered form in text widget
        window = tk.Tk()
        window.title("Passwords")
        window.iconbitmap('assets/key.ico')
        window.geometry('500x500')

        def enwrite(str):
            text.config(state="normal")
            text.insert(tk.END,f'{str}\n')
            text.config(state='disabled')

        codes = {}
        scrollbar = tk.Scrollbar(window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text = tk.Text(window,autoseparators=True,font=("fixedsys",15),state="disabled" ,wrap=tk.WORD,yscrollcommand=scrollbar.set)
        text.pack(fill='both',expand=True)
        scrollbar.config(command=text.yview) # Scroll Bar
        ls = pathapp()
        if ls != '':
            with open(pathapp(),'r') as f:
                k1=f.read().split('\n')
                
                for i in range(1,len(k1)):
                    if k1[i].strip() != ':':
                        key,passe = k1[i].strip().split(':',1)
                        codes[decipher(key)]=decipher(passe)
                        for name,code in codes.items():
                            passcode = f"{name}:{code}"
                        enwrite(passcode)
                    else:
                        continue
        
        else:
            if os.path.exists(__defaultpath__):
                with open(f'{__defaultpath__}','r') as f:
                    k1=f.read().split('\n')
                    
                    for i in range(1,len(k1)):
                        if k1[i].strip() != ':':
                            key,passe = k1[i].strip().split(':',1)
                            codes[decipher(key)]=decipher(passe)
                            for name,code in codes.items():
                                passcode = f"{name}:{code}"
                            enwrite(passcode)
                        else:
                            continue
            else:
                msg.showerror(msg.ERROR,"Choose a hash file~!")
        menu1 = tk.Menu(window,tearoff=0)
        menu1.add_command(label='Edit',command=edit)
        menu1.add_command(label='Save',command=save)
        window.config(menu=menu1)
        
        window.mainloop()
    # Ciphers Code and Writes in the selected file.
    def write():
        k = msg.askyesno("Submit","Do you want to submit this ?")
        if k == True: 
            txt = __defaultpath__
            ls = pathapp()
            if ls != '':
                with open(pathapp(),'+a') as file:
                    file.write('\n')
                    file.write(f'{cipher(email.get())}:{cipher(password.get())}')
                    password1.delete(0,tk.END)
                    email1.delete(0,tk.END)
                    
            else: # You can repair this: ( this thing won't  make a budge in code)
                with open(f'{__defaultpath__}','+a') as file:
                    file.write('\n')
                    file.write(('%s:%s') % (cipher(email.get()),cipher(password.get())))
                    with open("file_path.txt","w") as s:
                              s.write(__defaultpath__)
    # GUI           
    window =  tk.Tk()
    window.geometry("500x400")
    window.iconbitmap('assets/key.ico')
    window.config(bg='#222831')
    window.title("Password encryptor")

    Label = tk.Label(text="PASSWORD SAVER",font=('fixedsys',23),fg='#00ADB5',compound="top",bg="#222831")
    Label.place(x=150,y=50)
    Label.bind('<Enter>',___anim)
    Label.bind("<Leave>",l___anim)  # BINDINGS
    Label.bind('<Button-1>',decryption)           # secret binding
    
    email_label =  tk.Label(window,text='EMAIL/NAME : ' ,font=('System',16,'bold'),fg='#36C2CE',bg='#222831')
    email_label.place(x=30,y=90)


    email = tk.StringVar()

    email1 =  tk.Entry(width=50,textvariable=email,foreground='#222831',background='#478CCF',font=('Modern',14,'bold'))
    email1.place(x=30,y=130,height=40)
    email1.bind('<Enter>',anim2_)
    email1.bind('<Leave>',__anim2)
    password = tk.StringVar()

    Pass_label =  tk.Label(window,text='PASSWORD : ' ,font=('System',16,'bold'),fg='#36C2CE',bg='#222831')
    Pass_label.place(x=30,y=200)
    
    password1 =  tk.Entry(width=50,textvariable=password,foreground='#222831',background='#478CCF',font=('Modern',14,'bold'))
    password1.place(x=30,y=240,height=40)
    password1.bind('<Enter>',anim_)
    password1.bind('<Leave>',__anim)
    button =  ImageTk.PhotoImage(Image.open('assets/button.png'))

    submit = tk.Button(image=button,background="#222831",fg='#77E4C8',width=70,border=0,command=write)
    submit.place(x=30,y=320,height=40)

    load_ico = ImageTk.PhotoImage(Image.open("assets/save.png"))

    load_button  = tk.Button(image=load_ico,background='#222831',command=load )
    load_button.place(x=330,y=320)
    change_ico = ImageTk.PhotoImage(Image.open("assets/edit.png").resize(size=(32,32)))
    change = tk.Button(image=change_ico,bd=0,border=0,borderwidth=0,bg='#77E4C8',command=changepass)
    change.place(x=20,y=10)
    window.mainloop()

if __name__ == '__main__':
    passbook()
