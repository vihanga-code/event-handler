from tkinter import *
window=Tk()
window.title("event handler")
window.geometry("250x300")
def keypress(event):
 print(event.char)
window.bind("<Key>",keypress)
def handler_for_button(event):
    print("button is click")
button=Button(text="click me")
button.pack()
button.bind("<Button-1>",handler_for_button)
window.mainloop()



