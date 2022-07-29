from curses import window
from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("Nbyula Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()


    if username in r.keys() and password == r[username]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="Black")
        
        Label(screen,text="Hello Terraformers!!! \n Wait I'm learning the Meeting Scheduling part",fg="green", bg='Black', font=('Calibri(Body)',35,'bold')).pack(expand=True)
        
        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'invalid username or password')


###########

def signup_command():
    window=Toplevel(root)
    root.title("Nbyula SignUp")
    root.geometry("925x500+300+200")
    root.configure(bg="#fff")
    root.resizable(False, False)


    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()

        if password==confirm_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully signed up')
                window.destroy()

            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
                messagebox.showerror('Invalid', "Both Password should match!!!")
            
    def sign():
        window.destroy()

    img = PhotoImage(file="image.png")
    Label(root, image=img,border=0,bg="white").place(x=50,y=90)

    frame = Frame(root,width = 350, height=390, bg="#fff")
    frame.place(x=380, y=50)


    heading = Label(frame, text = "Nbyula SignUp", fg ="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, 'bold'))
    heading.place(x=25, y=5)

#Username

    def on_enter(e):
        user.delete(0, "end")
    def on_leave(e):
        if user.get()=='':
            user.insert(0, "Username")

    user = Entry(frame,width=35,fg='black', border=0,bg='white',font=("Microsoft Yahei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#password

    def on_enter(e):
        code.delete(0, "end")
    def on_leave(e):
        if code.get()=='':
            code.insert(0, "Password")

    code = Entry(frame, width=35, fg="black", border=0, bg ='white', font=("Microsoft Yahei UI Light", 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


#confirm_password

    def on_enter(e):
        confirm_code.delete(0, 'end')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'Confirm Password')

    confirm_code = Entry(frame, width=35, fg="black", border=0, bg ='white', font=("Microsoft YaHei UI Light", 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    checkbtn = Checkbutton(frame,text = "Remember me?").place(x=35,y=265)

    Button(frame, width=39,pady=7, text = "Sign Up", bg="#57a1f8", fg="white",border=0, command=signup).place(x=35,y=300)

    label = Label(frame, text =' I have an account !!!', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=345)

    signin=Button(frame, width = 6, text ='Sign In', border=0, bg='white', cursor ='hand2', fg='#57a1f8', command=sign)
    signin.place(x=220,y=340)



    root.mainloop()

###########


img = PhotoImage(file="image.png")
Label(root, image=img,border=0,bg="white").place(x=50,y=90)

frame = Frame(root,width = 350, height=390, bg="#fff")
frame.place(x=380, y=50)


heading = Label(frame, text = "Nbyula Login", fg ="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, 'bold'))
heading.place(x=25, y=5)

#Username

def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    if user.get()=='':
        user.insert(0, "Username")

user = Entry(frame,width=35,fg='black', border=0,bg='white',font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#password

def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    if code.get()=='':
        code.insert(0, "Password")

code = Entry(frame, width=35, fg="black", border=0, bg ='white', font=("Microsoft Yahei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

###

checkbtn = Checkbutton(frame,text = "Remember me?").place(x=35,y=200)

Button(frame, width=39,pady=7, text = "Log In", bg="#57a1f8", fg="white",border=0, command=signin).place(x=35,y=240)
label = Label(frame, text =" Don't have an account !!!", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=70, y=285)

sign_up=Button(frame, width = 6, text ='Sign Up', border=0, bg='white', cursor ='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=220,y=280)



root.mainloop()
