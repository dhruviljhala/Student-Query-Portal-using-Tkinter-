#BUTTON VALA PAGE
import os
from subprocess import call
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

#file linking part 
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def ask_query():
    call(["python", "insert_query.py"]) #Button 1 (Ask query)
def answer_query():
    call(["python", "answer.py"])  #Buttton 2 (Answer Query)
def view_browse():
    call(["python","Display_with_back.py"]) #Button 3 (Surf/Browse)


class MULTIPURPOSE_SIP:
    def __init__(self):
        root = Tk()
       
        _bgcolor = '#000000'  
        _fgcolor = '#000000'  
        _compcolor = '#ffffff' 
        _ana1color = '#ffffff' 
        _ana2color = '#ffffff' 
        font14 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("963x749+540+110")
        root.title("MULTIPURPOSE STUDENT INTERACTION PLATFORM")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="black")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        #frame color
        self.Frame1.configure(background="yellow")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        #How may we help you message part.
        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        #Message Background Color
        self.Message6.configure(background="yellow")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''How may we help you?''')
        self.Message6.configure(width=791)

        #Ask a query button
        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.15, rely=0.20, height=150, width=400)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000000")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Ask a query''')
        self.Button2.configure(command=ask_query) #python link file line

        #Answer a query button
        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.57, rely=0.30, height=150, width=400)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#000000")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="white")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Answer query''')
        self.Button3.configure(command=answer_query)   #python link file line


        #Browsing button
        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.15, rely=0.61, height=150, width=400)
        self.Button5.configure(activebackground="#000000")
        self.Button5.configure(activeforeground="white")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''View/Browse''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=view_browse) #python link file line

        #Exit button
        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.57, rely=0.71, height=150, width=400)
        self.Button5.configure(activebackground="#000000")
        self.Button5.configure(activeforeground="white")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Leave''')
        self.Button6.configure(command=quit)
        root.mainloop()


GUEST=MULTIPURPOSE_SIP()


