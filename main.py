##import mysql.connector
from tkinter import*
#from PIL import ImageTk
from tkinter import messagebox



class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        #self.root.resizable(False,False)
        #====BG IMage=====
        #self.bg=ImageTk.PhotoImage(files="C:\\Users\\Tohy Ny Aina\\PycharmProjects\\pythonProject3\\images\\hack.png")
        #self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #====Login Frame=====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=130,y=130,height=340,width=500)


        title=Label(Frame_login,text="Bienvenue sur POTEHO",font=("Impact",25,"bold"),fg="black",bg="white").place(x=70,y=30)
        desc=Label(Frame_login,text="Veuillez vous connecter",font=("Ubuntu",15,"bold"),fg="black",bg="white").place(x=70,y=100)
        foot=Label(text="(c)Mlay</>. Tous droits réservés.",font=("Ubuntu",12,"bold"),fg="black",bg="white").place(x=560, y=680)

        lbl_user=Label(Frame_login,text="Admin",font=("Ubuntu",10,"bold"),fg="black",bg="white").place(x=70,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=70,y=170,width=350,height=35)


        lbl_user=Label(Frame_login,text="Mot de passe",font=("Ubuntu",10,"bold"),fg="black",bg="white").place(x=70,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_pass.place(x=70,y=240,width=350,height=35)

        #forget=Button(Frame_login,text="Mot de passe oublier?",bg="white",fg="black",bd=0,font=("times new roman",12)).place(x=90,y=280)

        Create_btn=Button(Frame_login,cursor="hand2",text="Vous n'avez pas un compte?",bg="white",fg="black",bd=0,font=("times new roman",12)).place(x=70,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Entrer",fg="white",bg="black",bd=0,font=("Ubuntu",18)).place(x=280,y=470,width=180,height=40)




    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Erreur","Veuillez completer les information",parent=self.root)

        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Tohy":
            messagebox.showerror("Erreur","Le nom de l'utilisateur/mot de passe est incorrect",parent=self.root)
        else:
            messagebox.showinfo("Bienvenue","Bienvenue {self.txt_user.get()}\n Your Password: {self.txt_pass.get()}",parent=self.root)


    #def Ok():
        #mysqldb=mysql.connector.connect(host="localhost",user="root",pasword="",database="mlay")
        #mycursor=mysqldb.cursor()
        #uname=self.txt_user.get()
        #password=self.txt_pass.get()

        #sql="select * from login where uname= %s and password= %s"
        #mycursor.execute(sql, [(uname), (password)])
        #results = mycursor.fetchall()
        #if results:
         #   messagebox.showinfo("","Connecter avec succes")
         #   root.destroy()
         #   call(["python","main.py"])
         #   return True
        #else:
         #   messagebox.showinfo("","Mot de passe incorrecte")
         #   return False


root=Tk()
root.minsize(1349,710)
root.geometry("1199x600+100+50")
c=Canvas(root,bg="white",height=300,width=300)
filename = PhotoImage(file="C:\\Users\\Tohy Ny Aina\\PycharmProjects\\pythonProject3\\images\\hack.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

c.pack()
obj=Login(root)
root.mainloop()