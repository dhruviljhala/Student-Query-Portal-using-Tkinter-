import sys
import os
import tkinter as tk
import  sqlite3
from tkinter import *
from tkinter import ttk
def returntobvp():
    root.destroy()
    os.system('python button_vala_page.py')
class login:
    def __init__(self,root):

        self.f=Frame(root,height=1000, width=500, background="light grey")
        self.f.propagate(0)
        #self.f.pack()
        
        self.f.grid(row=0, column=0)

        self.h1=Label(background='light grey',text="LOGIN",font='Helvetica 32 bold')
        self.h1.place(x=180, y=10)    
        self.l1=Label(background='light grey',text="Username :",font='Helvetica 10 bold')
        self.l2=Label(background='light grey',text="Password :",font='Helvetica 10 bold')
        self.b1=Button(self.f,text="Login",font='Helvetica 10 bold',width=15,height=2,bg="black",fg='light green',activebackground='cyan',activeforeground='blue',command=self.verify)

        self.e1=Entry(self.f,width=25,fg='blue',bg='white')
        self.e2=Entry(self.f,width=25,fg='blue',bg='white')

        self.l1.place(x=100, y=350)
        self.l2.place(x=100, y=375)
                      
        self.e1.place(x=200, y=350)
        self.e2.place(x=200, y=375)
                      
        self.b1.place(x=200, y=455)


        ###########################  REGISTER   ##################################
        self.f2=Frame(root,height=1000, width=500, background="cyan")
        self.f2.propagate(0)
        #self.f2.pack()
        
        self.f2.grid(row=0, column=1)

        self.h2=Label(background='cyan',text="REGISTRATION",font='Helvetica 32 bold')
        self.h2.place(x=595, y=10)
        self.l11=Label(background='cyan',text="Name :",font='Helvetica 10 bold')
        self.l22=Label(background='cyan',text="Username :",font='Helvetica 10 bold')
        self.l33=Label(background='cyan',text="Password :",font='Helvetica 10 bold')
        self.l44=Label(background='cyan',text="Year :",font='Helvetica 10 bold')
        self.l55=Label(background='cyan',text="Branch :",font='Helvetica 10 bold')

        self.year = tk.StringVar(root)
        self.year.set("I") # default value
        self.Y1 = ['I', 'II', 'III', 'IV']
        self.y = OptionMenu(root, self.year,*self.Y1)
        self.y.place(x=700, y=375)
        
        self.branch = tk.StringVar(root)
        self.branch.set("CS") # default value
        self.B1 = ["CS", "IT", "EXTC", "MECH", "MXTC", "CIVIL"]
        self.b = OptionMenu(root, self.branch,*self.B1)
        self.b.place(x=700, y=410)
        
        self.b11=Button(self.f2,text="Register",font='Helvetica 10 bold',width=15,height=2,bg="black",fg='light green',activebackground='light grey',activeforeground='blue',command=self.buttonClick)

        self.e11=Entry(self.f2,width=25,fg='blue',bg='white')
        self.e22=Entry(self.f2,width=25,fg='blue',bg='white')
        self.e33=Entry(self.f2,width=25,fg='blue',bg='white')

        self.l11.place(x=600, y=300)
        self.l22.place(x=600, y=325)
        self.l33.place(x=600, y=350)
        self.l44.place(x=600, y=375)
        self.l55.place(x=600, y=410)
        
        self.e11.place(x=200, y=300)
        self.e22.place(x=200, y=325)
        self.e33.place(x=200, y=350)
                      
        self.b11.place(x=200, y=475)

    

    def verify(self):
        str1=self.e1.get()
        str2=self.e2.get()
        conn  =  sqlite3 . connect ( 'database.db' )
        cursor  =  conn.cursor ()

        lst1=list(cursor.execute("""SELECT username FROM login"""))
        print(lst1)
        lst2=list(cursor.execute("""SELECT password FROM login"""))
        print(lst2)
        
        s=str(str1)
        for i in lst1:
            for j in i:
                if j==s:
                    returntobvp()
                else:
                    print('invalid')
                

        
    def buttonClick(self):
        str11=self.e11.get()
        str22=self.e22.get()
        str33=self.e33.get()
        str44=self.year.get()
        str55=self.branch.get()
        conn  =  sqlite3 . connect ( 'database.db' )
        cursor  =  conn.cursor ()

        try:
            cursor.execute("""INSERT INTO login(name,username,password,year,branch) VALUES (?,?,?,?,?)""", (str11,str22,str33,str44,str55))
            conn.commit ()
            
        except:
            cursor.execute("""CREATE TABLE IF NOT EXISTS login(name char(30), username varchar(30) PRIMARY KEY, password varchar(30), year char, branch char)""")
            cursor.execute("""INSERT INTO login(name,username,password,year,branch) VALUES (?,?,?,?,?)""", (str11,str22,str33,str44,str55))
            conn.commit ()
        print ( 'Data entered successfully.' )
        cursor=conn.execute("SELECT * from login")
        """
        for row in cursor:
            print("Name=", row[0])
            print("Username=", row[1])
            print("Password=", row[2])
            print("Year=", row[3])
            print("Branch=", row[4])
        """

        #query = cursor.execute("""SELECT *FROM EMPLOYEE WHERE emp_id LIKE (?)""", (str1))
        #for i in query:
        #    print("THIS Pass: ", i[1]);

    

root=Tk()
root.geometry("1000x1000")
root.title("login Page")
bt=login(root)
root.mainloop()
