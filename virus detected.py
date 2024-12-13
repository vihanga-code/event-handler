from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x300")
root.title("virus!!")

def msg():
    messagebox.showwarning("ALERT","STOP VIRUS")
button=Button(root,text="scan for virus",command=msg)    
button.place(x=40,y=80)
root.mainloop()