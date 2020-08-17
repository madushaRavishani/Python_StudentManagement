from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
      

        #ALL IMAGES
        self.bg_icon=ImageTk.PhotoImage(file="images/lg.png")
        self.logo_icon=ImageTk.PhotoImage( file="images/client1.png")
    
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack()

       # title=Label(self.root,text="Login System", font=("times new roman",40,"bold"),bg="blue",fg="black",bd=10,relief=GROOVE)
        #title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=460,y=200)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

       
        lbluser=Label(Login_Frame,text="Username",font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.uname,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="Password",font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,cursor="hand2",text="Login",width=15,font=("times new roman",20,"bold"),bg="gray",fg="black",command=self.loginfunction).grid(row=3,column=1,pady=10)

    def loginfunction(self):
        #print(self.uname.get(),self.pass_.get())
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required")           
        elif self.uname.get()=="madusha" and self.pass_.get()=="123456":
            #messagebox.showinfo("successfully login",f"welcome {self.uname.get()}")
            self.root.destroy()
            import Student
            #Student.File_App()
        else:
            messagebox.showerror("Error","Invalid usename & password")

root=Tk()  
obj=Login(root)
root.mainloop()
