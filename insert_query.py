import sys
import os
import  sqlite3
from tkinter import *
from tkinter import ttk

class Insert:
    def __init__(self,root):
        self.f=Frame(root,height=600, width=830)
        self.f.propagate(0)
        self.f.pack()

        self.l=Label(text="INSERT QUERY",font='Helvetica 18 bold')
        self.l.place(x=350, y=10)
        
        
        self.l1=Label(text="Enter Query :")
        self.l1.place(x=50, y=100)
        self.t = Text(self.f, height=4, width=50, bg='cyan')
        self.t.place(x=150,y=100)
    
                
        self.buttonCommit=Button(self.f, height=1, width=10, text="Submit", bd='3', command=self.retrieve_input)
        self.buttonCommit.place(x=150,y=200)

        #Going back button
        self.btn = Button(root, text = 'Back', bd = '5', command = self.returntobvp)      
        self.btn.pack(side = 'top')
        
    def retrieve_input(self):
        str1=self.inputValue=self.t.get("1.0","end-1c")
        print(self.inputValue)
        #str1=self.e1.get()
        #str2=self.e2.get()
        conn  =  sqlite3 . connect ( 'database.db' )
        cursor  =  conn.cursor ()
        try:
            cursor.execute("""INSERT INTO Query(query) VALUES (?)""", (str1,))
            conn.commit ()

        except:
            cursor.execute('''CREATE TABLE Query(q_id INTEGER PRIMARY KEY,query char(30))''')
            cursor.execute("""INSERT INTO Query(query) VALUES (?)""", (str1,))
            conn.commit ()
        print ( 'Data entered successfully.' )
        cursor=conn.execute("SELECT * from Query")
        for row in cursor:
            print("Query", row)

    def returntobvp(self):
        root.destroy()
        os.system('python button_vala_page.py')
        

root=Tk()
root.title("ASK A QUERY")

bt=Insert(root)

root.mainloop()





















