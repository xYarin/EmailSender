import smtplib, ssl
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfile, askopenfilename
happened = False
port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()
def center_window(root, w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y-50))

message = """\
Subject: Hi there

This message is sent from Yarin in Python the DEV."""

root = Tk()
center_window(root, 400, 250)

sender_email = Entry(root, width=25, borderwidth=5)
sender_email_label = Label(root, text="Email: ")
# make spcae labels
space = Label(root, text="     ").grid(row=0, column=1)
space1 = Label(root, text="     ").grid(row=2, column=2)
space2 = Label(root, text="     ").grid(row=4, column=4)
space3 = Label(root, text="     ").grid(row=6, column=5)

sender_email_label.grid(row=1, column=3)
sender_email.grid(row=1, column=4)

receiver_email = Entry(root, width=25, borderwidth=5)
receiver_email_label = Label(root, text="Receiver Email: ")
receiver_email.grid(row=5, column=4)
receiver_email_label.grid(row=5, column=3)

password = Entry(root, width=25, borderwidth=5, show="*")
password_label = Label(root, text="Password: ")
password.grid(row=3, column=4)
password_label.grid(row=3, column=3)

def clear():
    sender_email.delete(0, END)
    receiver_email.delete(0, END)
    password.delete(0, END)

def isFilled():
    if len(sender_email.get()) == 0 and len(password.get()) == 0 and len(receiver_email.get()) == 0:
        showerror(title="bruh..", message="Enter some stuff to start.....")
    elif len(sender_email.get()) == 0 or len(password.get()) == 0 or len(receiver_email.get()) == 0:
        showerror(title="Error!", message="You missed something, enter all of the info please")
    else:
        isVaild()
def getFilePath():
    file = askopenfilename(title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    print(file)
    return file


def isVaild():
    def open_file(r, title):
        path = getFilePath()
        with open(path, 'r') as f:
            read = f.read()
            msg = """\
Subject: {}

{}

This message was sent by xYarin program. """ .format(title, read)
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email.get(), password.get())
            server.sendmail(sender_email.get(), receiver_email.get(), msg)
            r.destroy()
            showinfo(title="Got it!", message=f"Your message has been successfully sent to '{receiver_email.get()}'")
            clear()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email.get(), password.get())
            
            
        except Exception as e:
            global happened
            happened = True
            showerror(title="Error!", message=f"Incorrect email or password\nError: {e}")
        
        if not happened:
            root2 = Tk()
            center_window(root2, 200, 200)
            subject = Entry(root2, width=20, borderwidth=5)
            subject.insert(0, "ENTER SUBJECT HERE")
            subject.pack()
            upload_message_button = Button(root2, text="Upload Text File Message", font = ("arial", 10, "bold"), command = lambda: open_file(root2, subject.get())).pack()
            root2.mainloop()

    
login_button = Button(root, text="Login", command=isFilled, width=25, height=3, font = ("arial", 10, "bold"))
login_button.grid(row=7, column=4)

#sender_email = "coding.guy.tests@gmail.com"
#receiver_email = "yarinm0206@gmail.com"


        

root.mainloop()