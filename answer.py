import sys
import os
import  sqlite3
from tkinter import *
from tkinter import ttk

class Answer:
    def __init__(self,root):
        self.f=Frame(root,height=600, width=830)
        self.f.propagate(0)
        self.f.pack()

        self.l=Label(text="ANSWER QUERY",font='Helvetica 18 bold')
        self.l.place(x=320, y=10)
        
              
        self.l1=Label(text="Enter Query ID :")
        self.l1.place(x=50, y=100)
        self.t = Entry(self.f,width=25,fg='blue',bg='cyan')
        self.t.place(x=150,y=100)
    
        self.l=Label(text="Answer Query :")
        self.l.place(x=50, y=200)
        self.ans = Text(self.f, height=4, width=50, bg='cyan')
        self.ans.place(x=150,y=200)
        
        self.buttonCommit=Button(self.f, height=1, width=10, text="Submit", bd='3', command=self.buttonclick)
        self.buttonCommit.place(x=150,y=300)
        
        #Going back button
        self.btn = Button(root, text = 'Back', bd = '5', command = self.returntobvp)      
        self.btn.pack(side = 'top')
        
    def buttonclick(self):
        str1=self.inputValue=self.ans.get("1.0","end-1c")
        print(self.inputValue)
        
        str2=self.t.get()
        print(str2)
        
        conn  =  sqlite3 . connect ( 'database.db' )
        cursor  =  conn.cursor ()
        try:
            #cursor.execute("""ALTER TABLE Query ADD COLUMN Answer VARCHAR""")
            cursor.execute("""Update Query set Answer =:1 WHERE q_id= :2 """, (str1,str2))
            conn.commit()
            print ( 'Data entered successfully.' )

        except:
            #print("Database not found")
            cursor.execute("""ALTER TABLE Query ADD COLUMN Answer VARCHAR""")
            cursor.execute("""Update Query set Answer =:1 WHERE q_id= :2 """, (str1,str2))
            conn.commit ()
        
        
        cursor=conn.execute("SELECT * from Query")
        for row in cursor:
            print("Query", row)
        
    def returntobvp(self):
        root.destroy()
        os.system('python button_vala_page.py')
        

root=Tk()
root.title("ANSWER QUERY")

bt=Answer(root)

root.mainloop()
