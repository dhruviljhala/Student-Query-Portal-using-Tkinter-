import sys
import os
import  sqlite3
from tkinter import *
from tkinter import ttk

    
class show:
    def __init__(self,root):
        self.f=Frame(root,height=600, width=830)
        self.f.propagate(0)
        self.f.pack()

        self.l=Label(text="ALL QUERIES",font='Helvetica 18 bold')
        self.l.place(x=340, y=10)
        
        #Going back button
        self.btn = Button(root, text = 'Back', bd = '5', command = self.returntobvp)      
        self.btn.pack(side = 'top')
                
        conn  =  sqlite3 . connect ( 'database.db' )
        cursor  =  conn.cursor ()

        
        cursor=conn.execute("SELECT q_id, query, Answer from Query")
        
        self.tree = ttk.Treeview(self.f, columns = (1,2,3), height = 20, selectmode="extended", show = "headings")
        self.tree.place(x=30,y=80)

        self.tree.heading(1, text="Query ID")
        self.tree.heading(2, text="Query")
        self.tree.heading(3, text="Answer")

        self.tree.column(1, width = 55)
        self.tree.column(2, width = 350)
        self.tree.column(3, width = 350)

        scroll = ttk.Scrollbar(self.f, orient="vertical", command=self.tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        self.tree.configure(yscrollcommand=scroll.set)

        for val in cursor:
            self.tree.insert('', 'end', values = (val[0],val[1], val[2]) )
    def returntobvp(self):
        root.destroy()
        os.system('python button_vala_page.py')

root=Tk()
root.title("VIEW/BROWSE")

bt=show(root)

root.mainloop()
