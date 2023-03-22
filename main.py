import tkinter 
from tkinter import *

root = Tk()
root.title("Exercice 1")
root.geometry("400x650+400+100") 

root.resizable(False,False)

list_tach = []

def Ajout_Tach():
    tach = tach_input.get()
    tach_input.delete(0, END)

    if tach:
        with open("tachlist.txt","a") as f_tach:
            f_tach.write(f"\n{tach}")
        list_tach.append(tach)
        listbox.insert(END, tach)


def supprimer():
    global list_tach
    tach = str(listbox.get(ANCHOR))
    if tach in list_tach:
        list_tach.remove(tach)

        with open("tachlist.txt","w") as f_tach:
            for tach in list_tach:
                f_tach.write(tach+"\n")
            
        listbox.delete(ANCHOR)


def open_tach():
    try:
        global list_tach
        with open("tachlist.txt","r") as f_tach:
            taches = f_tach.readlines() 

            for tach in taches:
                if tach != '\n':
                    list_tach.append(tach.strip())
                    listbox.insert(END , tach.strip())
    except:
        file=open("tachlist.txt","w")
        file.close()
        
#icons 
Image_icon=PhotoImage(file="task.png")
root.iconphoto(False,Image_icon)

#bar 
TopImage = PhotoImage(file="topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

noteImage=PhotoImage(file="task.png")
Label(root,image=noteImage,bg="#32405b").place(x=30,y=25)

heading =Label(root,text="TOUTES LES TÂCHES",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=85,y=20)

#main frame 
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

tach_input = Entry(frame,width=18,font="arial 20",bd=0)
tach_input.place(x=10,y=10)
tach_input.focus()

button = Button(frame,text="Ajouter",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=Ajout_Tach)
button.place(x=270,y=6)

#listbox 
frame1= Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")

listbox.pack(side=LEFT, fill =BOTH,padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT , fill = BOTH)

listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)

#delete 
Delete_icon = PhotoImage(file="delete.png")
Button(root,image=Delete_icon,bd=0,command=supprimer).pack(side=BOTTOM,pady=13)

open_tach()

root.mainloop()
