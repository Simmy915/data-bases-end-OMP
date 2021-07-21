import mysql.connector
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import rsaidnumber
import datetime


class HomeScreen:
    def __init__(self, master):

        self.master = master
        self.master.title("Lifechoices Online")
        self.master.geometry("800x650")
        self.id_no = ''


        self.background_img = PhotoImage(file='images/background-photos/Free-Abstract-Artistic-Grey-Background.png')
        self.background_img = self.background_img.subsample(5)
        self.img_logo = PhotoImage(file='images/lifechoices-logo-teal.png')
        self.img_logo = self.img_logo.subsample(7)


        image_bg = PhotoImage(file='images/background-photos/Free-Abstract-Artistic-Grey-Background.png')
        image_bg = image_bg.subsample(5)
        self.lbl_bg = Label(self.master, image=image_bg)
        self.lbl_bg.place(x=-10, y=-10)


        image_logo = PhotoImage(file='images/lifechoices-logo-teal.png')
        image_logo = image_logo.subsample(2)
        self.lbl_logo = Label(self.master, image=image_logo, bg="black", width="600", height="150")
        self.lbl_logo.place(x=98, y=50)


        self.frame_log = Frame(self.master, width="602", height="390", bg="white")
        self.frame_log.place(x=98, y=200)


        self.frame_left = Frame(self.frame_log, width="300", height="390", bg="blue")
        self.frame_left.place(x=0, y=0)
        image_welcome = PhotoImage(file="images//welcome-png-hd-17.png")
        image_welcome = image_welcome.subsample(2)
        self.lbl_welcome = Label(self.frame_left, image=image_welcome, bg="blue")
        self.lbl_welcome.place(x=30, y=50)


        self.btn_sign_in = Button(self.frame_log, text="Sign in", bg="red", fg="white", border="0", relief="solid",
                                  activebackground="blue", activeforeground="white", width="30",
                                  command=self.sign_in_frame)
        self.btn_sign_in.place(x=317, y=100)
        self.lbl_or = Label(self.frame_log, text="-or-", bg="white")
        self.lbl_or.place(x=440, y=155)
        self.btn_reg = Button(self.frame_log, text="Register", bg="blue", fg="white", border="0", relief="solid",
                              activebackground="green", activeforeground="white", width="30",
                              command=self.register_frame)
        self.btn_reg.place(x=317, y=200)


        self.frame_sign = Frame(self.frame_log, bg="red", width="302", height="390")


        self.frame_id = Frame(self.frame_sign)
        self.lbl_id = Label(self.frame_id, text="ID No.", bg="grey", width="8")
        self.entry_id = Entry(self.frame_id)


        self.btn_sign_in2 = Button(self.frame_sign, text="Sign in", bg="red", fg="white", border="0",
                                   relief="solid", activebackground="#00547c", activeforeground="white", width="26",
                                   command=self.sign_in)


        self.lbl_not_reg = Label(self.frame_sign, text="Not registered? Click", font="sans-serif 9", bg="blue")
        self.btn_not_reg = Button(self.frame_sign, text="here", bg="red", fg="white", borderwidth=0,
                                  highlightbackground="white", activebackground="white", activeforeground="#00547c",
                                  font="sans-serif 9", underline=True, pady=0, padx=0,
                                  command=lambda: [self.register_frame()])

        self.frame_id.place(x=35, y=130)
        self.lbl_id.grid(row=1, column=1)
        self.entry_id.grid(row=1, column=2)
        self.btn_sign_in2.place(x=34, y=180)
        self.lbl_not_reg.place(x=35, y=215)
        self.btn_not_reg.place(x=163, y=215)


        self.frame_register = Frame(self.frame_log, bg="white", width="302", height="390")

        self.lbl_your_details_head = Label(self.frame_register, text="Your Details", font="sans-serif 14", bg="white")
        self.lbl_your_details_head.place(x=95, y=10)

        self.frame_name = Frame(self.frame_register)
        self.lbl_name = Label(self.frame_name, text="Name", bg="blue", width=10)
        self.entry_name = Entry(self.frame_name)
        self.frame_name.place(x=28, y=50)
        self.lbl_name.grid(row=1, column=1)
        self.entry_name.grid(row=1, column=2)

        self.frame_surname = Frame(self.frame_register)
        self.lbl_surname = Label(self.frame_surname, text="Surname", bg="blue", width=10)
        self.entry_surname = Entry(self.frame_surname)
        self.frame_surname.place(x=28, y=80)
        self.lbl_surname.grid(row=1, column=1)
        self.entry_surname.grid(row=1, column=2)

        self.frame_register_id = Frame(self.frame_register)
        self.lbl_register_id = Label(self.frame_register_id, text="ID", bg="blue", width=10)
        self.entry_register_id = Entry(self.frame_register_id)
        self.frame_register_id.place(x=28, y=110)
        self.lbl_register_id.grid(row=1, column=1)
        self.entry_register_id.grid(row=1, column=2)

        self.frame_phone = Frame(self.frame_register)
        self.lbl_phone = Label(self.frame_phone, text="Phone No.", bg="blue", width=10)
        self.entry_phone = Entry(self.frame_phone)
        self.frame_phone.place(x=28, y=140)
        self.lbl_phone.grid(row=1, column=1)
        self.entry_phone.grid(row=1, column=2)

        #THIS IS THE NEXT OF KIN
        self.lbl_next_of_kin_head = Label(self.frame_register, text="Next of Kin Details", bg="red",
                                          font="sans-serif 14")
        self.lbl_next_of_kin_head.place(x=65, y=190)

        self.frame_kin_name = Frame(self.frame_register)
        self.lbl_kin_name = Label(self.frame_kin_name, text="Name", bg="red", width=10)
        self.entry_kin_name = Entry(self.frame_kin_name)
        self.frame_kin_name.place(x=28, y=230)
        self.lbl_kin_name.grid(row=1, column=1)
        self.entry_kin_name.grid(row=1, column=2)

        self.frame_kin_phone = Frame(self.frame_register)
        self.lbl_kin_phone = Label(self.frame_kin_phone, text="Phone No.", bg="red", width=10)
        self.entry_kin_phone = Entry(self.frame_kin_phone)
        self.frame_kin_phone.place(x=28, y=260)
        self.lbl_kin_phone.grid(row=1, column=1)
        self.entry_kin_phone.grid(row=1, column=2)

        self.btn_reg_page = Button(self.frame_register, text="Register", bg="blue", fg="white", border="0",
                                   relief="solid", activebackground="#00547c", activeforeground="white", width="28",
                                   command=self.register)
        self.btn_reg_page.place(x=28, y=310)


        self.lbl_already_reg = Label(self.frame_register, text="Already registered? Click", bg="blue",
                                     font="sans-serif 9")
        self.lbl_already_reg.place(x=28, y=345)
        self.btn_already_reg = Button(self.frame_register, text="here", bg="blue", fg="#00769e", borderwidth=0,
                                      highlightbackground="white", activebackground="red", activeforeground="#00547c",
                                      font="sans-serif 9", underline=True, pady=0, padx=0,
                                      command=lambda: [self.sign_in_frame()])
        self.btn_already_reg.place(x=180, y=345)


        self.frame_admin = Frame(self.frame_log, bg="red", width=300, height=390)

        self.lbl_admin_head = Label(self.frame_admin, text="Admin Login", font="sans-serif 14", bg="white")
        self.lbl_admin_head.place(x=95, y=100)

        self.frame_admin_id = Frame(self.frame_admin)
        self.lbl_admin_id = Label(self.frame_admin_id, text="ID No.", bg="blue", width=10)
        self.entry_admin_id = Entry(self.frame_admin_id)
        self.frame_admin_id.place(x=28, y=150)
        self.lbl_admin_id.grid(row=1, column=1)
        self.entry_admin_id.grid(row=1, column=2)

        self.frame_admin_pass = Frame(self.frame_admin)
        self.lbl_admin_pass = Label(self.frame_admin_pass, text="Password", bg="blue", width=10)
        self.entry_admin_pass = Entry(self.frame_admin_pass)
        self.frame_admin_pass.place(x=28, y=180)
        self.lbl_admin_pass.grid(row=1, column=1)
        self.entry_admin_pass.grid(row=1, column=2)

        self.btn_admin_sign = Button(self.frame_admin, text="Sign in", bg="blue", fg="white", border="0",
                                     relief="solid", activebackground="#00547c", activeforeground="white", width="28",
                                     command=self.admin)

        self.btn_admin_sign.place(x=27, y=215)


        self.admin_key_pressed = False


        self.master.bind('<Control-Alt-a>', self.admin_frame)

        self.master.mainloop()


    def sign_in_frame(self):
        self.frame_sign.place(x=300, y=0)
        Misc.lift(self.frame_sign)


    def register_frame(self):
        self.frame_register.place(x=300, y=0)
        Misc.lift(self.frame_register)


    def admin_frame(self, event=None):
        if not self.admin_key_pressed:
            self.frame_admin.place(x=300, y=0)
            Misc.lift(self.frame_admin)
            self.admin_key_pressed = True

        else:
            self.frame_sign.place(x=300, y=0)
            Misc.lift(self.frame_sign)
            self.admin_key_pressed = False


    def sign_in(self):
        try:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                                database='lifechoices_online', auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            id_no = self.entry_id.get()
            self.id_no = self.entry_id.get()
            rsaidnumber.parse(id_no)
            query = "select * from Users where ID='{}'".format(id_no)
            mycursor.execute(query)
            info = mycursor.fetchall()
            if not info:
                messagebox.showerror(message="User does not exist")
            else:
                query_check_sign = "select * from register where ID='{}' and time_out='--:--'".format(id_no)
                mycursor.execute(query_check_sign)
                result = mycursor.fetchall()
                if not result:
                    now = datetime.datetime.now()
                    date = "{}".format(now.date())
                    minute = now.minute
                    hour = now.hour
                    if minute <= 9:
                        minute = '0' + str(minute)
                    if hour <= 9:
                        hour = '0' + str(hour)
                    time = "{}:{}".format(hour, minute)
                    query1 = "insert into register (Date, ID, name, time_in) values (" \
                             "'{}', '{}', '{}', '{}')".format(date, id_no, info[0][1], time)
                    mycursor.execute(query1)
                    mydb.commit()
                    self.master.withdraw()
                    self.signedin_window()

                else:
                    self.master.withdraw()
                    self.signedin_window()

        except ValueError:
            messagebox.showwarning(message="Invalid ID number format")


    def register(self):
        try:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                           database='lifechoices_online', auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            id_no = self.entry_register_id.get()
            name = self.entry_name.get()
            surname = self.entry_surname.get()
            phone = self.entry_phone.get()
            name_kin = self.entry_kin_name.get()
            phone_kin = self.entry_kin_phone.get()

            #
            rsaidnumber.parse(id_no)
            int(self.entry_phone.get())
            int(self.entry_kin_phone.get())

            query = "select * from Users where ID='{}'".format(id_no)
            mycursor.execute(query)
            result = mycursor.fetchall()


            if result:
                messagebox.showerror(message="User already exists, try signing in")

            elif name == '' or surname == '' or phone == '' or name_kin == '' or phone_kin == '':
                messagebox.showerror(message='Make sure all entry fields are filled')

            elif len(phone) != 10:
                messagebox.showwarning(message="Phone number be a ten digit integer")

            elif len(phone_kin) != 10:
                messagebox.showwarning(message="Next of kin phone number must be a ten digit integer")

            else:
                query1 = "insert into Users (ID, name, surname, phone) values ('{}', '{}', '{}', '{}')".format(id_no,
                                                                                                               name,
                                                                                                               surname,
                                                                                                               phone)
                mycursor.execute(query1)
                mydb.commit()

                query2 = "insert into next_of_kin (ID, name, phone) values ('{}', '{}', '{}')".format(id_no, name_kin,
                                                                                                      phone_kin)
                mycursor.execute(query2)
                mydb.commit()
                messagebox.showinfo(message="Registration complete. Proceed to sign-in")
                self.sign_in_frame()

        except ValueError:
            messagebox.showwarning(message="Make sure all entries are correctly filled")


    def admin(self):
        try:
            mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                           database='lifechoices_online', auth_plugin='mysql_native_password')

            mycursor = mydb.cursor()

            id_no = self.entry_admin_id.get()
            password = self.entry_admin_pass.get()


            rsaidnumber.parse(id_no)

            query = "select * from admin_users where ID='{}'".format(id_no)
            mycursor.execute(query)

            result = mycursor.fetchall()

            if not result:
                messagebox.showerror(message="Admin user does not exist")

            else:
                if result[0][1] == password:
                    messagebox.showinfo(message="success")
                    self.master.destroy()
                    import admin_window

                else:
                    messagebox.showerror(message="incorrect password")

        except ValueError:
            messagebox.showerror(message="Incorrect ID format")

    def signedin_window(self):

        window = Toplevel()
        window.geometry('600x400')


        lbl_img = Label(window, image=self.background_img)
        lbl_img.place(relx=0, rely=0, anchor=NW)


        lbl_logo = Label(window, width=600, height=50, bg='black', image=self.img_logo)
        lbl_logo.place(relx=0, rely=0, anchor=NW)


        frame_sign_out = Frame(window, width=300, height=100, bg='white')
        frame_sign_out.place(relx=0.5, rely=0.5, anchor=CENTER)


        lbl_signed_in_head = Label(frame_sign_out, text="Signed in", font="sans-serif 15", bg='white')
        lbl_signed_in_head.place(rely=0.1, relx=0.5, anchor=N)




        def sign_out():
            try:
                mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                               database='lifechoices_online', auth_plugin='mysql_native_password')
                mycursor = mydb.cursor()


                now = datetime.datetime.now()
                minute = now.minute
                hour = now.hour
                if minute <= 9:
                    minute = '0' + str(minute)
                if hour <= 9:
                    hour = '0' + str(hour)
                time = "{}:{}".format(hour, minute)
                query = "update register set time_out='{}' where ID='{}' and time_out='--:--'".format(time, self.id_no)
                mycursor.execute(query)
                mydb.commit()
                messagebox.showinfo(message='Logged out. Peace out')


                root.deiconify()
                window.destroy()

            except ValueError:
                messagebox.showerror(message='Invalid ID')


        btn_sign_out = Button(frame_sign_out, text="Sign out", bg="#00769e", fg="white", border="0",
                              relief="solid", activebackground="#00547c", activeforeground="white", width="40",
                              command=sign_out)
        btn_sign_out.place(rely=1, relx=0.5, anchor=S)



root = Tk()
app = HomeScreen(root)
