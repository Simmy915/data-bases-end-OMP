from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
import mysql.connector
import rsaidnumber


class AdminGUI:
    def __init__(self, master):
        #THIS IS THE WINDOW SET UP FOR THE APPLICATION
        self.master = master
        self.master.title("Admin Page")
        self.master.geometry('1010x620')
        self.master.config(bg="red")

        #THIS IS THE FRAME SET UP FOR THE OPTION MENU
        self.frame_options = Frame(self.master, bg='red', width=1010, height=620)
        self.frame_options.place(rely=0.5, relx=0.5, anchor=CENTER)

        #THIS IS THE OPTIONS BUTTON THAT USERS WILL  SEE
        self.btn_modify_screen = Button(self.frame_options, text="Modify / Add / Remove", bg="red", fg="white",
                                        border="0", relief="solid", activebackground="blue",
                                        activeforeground="white", width="30", command=self.modify_screen)
        self.btn_modify_screen.place(rely=0.45, relx=0.5, anchor=CENTER)

        self.btn_view_register = Button(self.frame_options, text="See register", bg="blue", fg="white", border="0",
                                        relief="solid", activebackground="#00547c", activeforeground="white",
                                        width="30", command=self.register_frame)

        self.btn_view_register.place(rely=0.5, relx=0.5, anchor=CENTER)

        self.btn_logout = Button(self.frame_options, text="Log out", bg="red", fg="blue", border="0",
                                 relief="solid", activebackground="#00547c", activeforeground="white", width="30",
                                 command=self.logout)
        self.btn_logout.place(rely=0.55, relx=0.5, anchor=CENTER)

        #THIS IS TO MODIFY THE WIDGETS
        self.frame_modify = Frame(self.master, width=1010, height=620, bg="green")

        #THIS IS THE SCROLL BAR
        self.tree_modify_frame = Frame(self.frame_modify)


        self.scroll_modify = Scrollbar(self.tree_modify_frame)
        self.scroll_modify.pack(side=RIGHT, fill=Y)

        #THIS IS THE TABLE THAT IS USED TO DISPALY USERS
        self.tree_modify = ttk.Treeview(self.tree_modify_frame, yscrollcommand=self.scroll_modify.set)
        self.scroll_modify.config(command=self.tree_modify.yview)
        self.tree_modify.pack()

        self.tree_modify['columns'] = ('ID No.', 'Name', 'Surname', 'Phone No.')

        self.tree_modify.column('ID No.')
        self.tree_modify.column('Name')
        self.tree_modify.column('Surname')
        self.tree_modify.column('Phone No.')

        self.tree_modify['show'] = 'headings'
        self.tree_modify.heading('ID No.', text='ID no.')
        self.tree_modify.heading('Name', text='Name')
        self.tree_modify.heading('Surname', text='Surname')
        self.tree_modify.heading('Phone No.', text='Phone no.')

        self.pop_treeview()  #THIS IS THE FUNCTION THAT WOULD BE USED TO POPULATE THE TABLE

        self.tree_modify_frame.place(rely=0, relx=0.5, anchor=N)

        """frame for entry fields (user name, surname, ID, phone no and admin privilege info. Next of kin name and phone 
        no)"""
        self.entry_frame = Frame(self.frame_modify, bg='white', width=814, height=350)
        self.entry_frame.place(rely=0.356, relx=0.098, anchor=NW)

        self.lbl_user_head = Label(self.entry_frame, text='User Details', font='sans-serif 14', bg='white')
        self.lbl_user_head.place(y=20, x=60)

        self.lbl_ID = Label(self.entry_frame, text="ID No.", bg='white')
        self.lbl_ID.place(x=60, y=70)

        self.entry_ID = Entry(self.entry_frame)
        self.entry_ID.place(x=200, y=69)

        self.lbl_name = Label(self.entry_frame, text="Name", bg='white')
        self.lbl_name.place(x=60, y=110)

        self.entry_name = Entry(self.entry_frame)
        self.entry_name.place(x=200, y=109)

        self.lbl_surname = Label(self.entry_frame, text="Surname", bg='green')
        self.lbl_surname.place(x=60, y=150)

        self.entry_surname = Entry(self.entry_frame)
        self.entry_surname.place(x=200, y=149)

        self.lbl_phone = Label(self.entry_frame, text="Phone No.", bg='orange')
        self.lbl_phone.place(x=60, y=190)

        self.entry_phone = Entry(self.entry_frame)
        self.entry_phone.place(x=200, y=189)

        self.lbl_admin_priv = Label(self.entry_frame, text="Admin privileges", bg="yellow")
        self.lbl_admin_priv.place(x=60, y=230)

        self.current_value = StringVar()
        self.combo_admin_priv = ttk.Combobox(self.entry_frame, textvariable=self.current_value, width=10,
                                             state='readonly')

        self.combo_admin_priv.bind('<<ComboboxSelected>>', self.password_normal)
        self.combo_admin_priv['values'] = ('Yes', 'No')
        self.combo_admin_priv.place(x=200, y=230)

        self.lbl_password = Label(self.entry_frame, text="Password", bg="white")
        self.lbl_password.place(x=60, y=270)

        self.entry_password = Entry(self.entry_frame, state='readonly')
        self.entry_password.place(x=200, y=269)

        self.lbl_kin = Label(self.entry_frame, text="Next of kin", font='sans-serif 14', bg='yellow')
        self.lbl_kin.place(x=440, y=20)

        self.lbl_kin_name = Label(self.entry_frame, text='Name', bg='yellow')
        self.lbl_kin_name.place(x=440, y=70)

        self.entry_kin_name = Entry(self.entry_frame)
        self.entry_kin_name.place(x=580, y=69)

        self.lbl_kin_phone = Label(self.entry_frame, text="Phone No.", bg='yellow')
        self.lbl_kin_phone.place(x=440, y=110)

        self.entry_kin_phone = Entry(self.entry_frame)
        self.entry_kin_phone.place(x=580, y=109)

        self.tree_modify.bind('<ButtonRelease-1>', self.send_data)


        self.btn_update = Button(self.entry_frame, text="Update user", bg="red", fg="white", border="0",
                                 relief="solid", activebackground="#00547c", activeforeground="white", width="15",
                                 command=self.update)
        self.btn_update.place(relx=0, rely=1, anchor=SW)

        self.btn_add = Button(self.entry_frame, text="Add user", bg="red", fg="white", border="0", relief="solid",
                              activebackground="blue", activeforeground="white", width="15", command=self.add)
        self.btn_add.place(rely=1, relx=0.36, anchor=S)

        self.btn_delete = Button(self.entry_frame, text="Delete user", bg="red", fg="white", border="0",
                                 relief="solid", activebackground="red", activeforeground="white", width="15",
                                 command=self.remove)
        self.btn_delete.place(rely=1, relx=0.64, anchor=S)

        self.btn_back_modify = Button(self.entry_frame, text="Back", bg="red", fg="white", border="0",
                                      relief="solid", activebackground="#00547c", activeforeground="white", width="15",
                                      command=self.back)
        self.btn_back_modify.place(rely=1, relx=1, anchor=SE)

        # THIS IS THE VARIABLE TAHT WILL KEEP TRACK OF THINGS SUCH AS ID OF USERS
        self.current_id = ''

        # THIS IS THE FRAME FOR SIGNING IN AND OUT!
        self.frame_register = Frame(self.master, width=1010, height=620, bg='blue')
        # self.frame_register.place(rely=0, relx=0, anchor=NW)

        self.tree_register_frame = Frame(self.frame_register)


        self.scroll_register = Scrollbar(self.tree_register_frame)
        self.scroll_register.pack(side=RIGHT, fill=Y)

        self.tree_register = ttk.Treeview(self.tree_register_frame, yscrollcommand=self.scroll_register.set)

        self.scroll_register.config(command=self.tree_register.yview)
        self.tree_register['columns'] = ('Date', 'ID No.', 'Name', 'Time in', 'Time out')

        self.tree_register.column('Date')
        self.tree_register.column('ID No.')
        self.tree_register.column('Name')
        self.tree_register.column('Time in')
        self.tree_register.column('Time out')

        self.tree_register['show'] = 'headings'
        self.tree_register.heading('Date', text='Date')
        self.tree_register.heading('ID No.', text='ID No.')
        self.tree_register.heading('Name', text='Name')
        self.tree_register.heading('Time in', text='Time in')
        self.tree_register.heading('Time out', text='Time out')


        self.btn_sign_out = Button(self.frame_register, text="Sign user out", bg="red", fg="white", border="0",
                                   relief="solid", activebackground="#00547c", activeforeground="white", width="28",
                                   command=self.sign_out_user)
        self.btn_sign_out.place(relx=0.5, y=300, anchor=CENTER)

        # THIS IS THE BACK BUTTON
        self.btn_back_register = Button(self.frame_register, text="Back", bg="blue", fg="white", border="0",
                                        relief="solid", activebackground="#00547c", activeforeground="white",
                                        width="28", command=self.back)
        self.btn_back_register.place(relx=0.5, y=350, anchor=CENTER)

        self.pop_tree_register()

        self.tree_register_frame.place(rely=0, relx=0.5, anchor=N)
        self.tree_register.pack()


    def modify_screen(self):
        self.frame_modify.place(rely=0.5, relx=0.5, anchor=CENTER)
        Misc.lift(self.frame_modify)


    def logout(self):
        self.master.destroy()
        import main


    def pop_treeview(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        query = "select * from Users"
        mycursor.execute(query)
        info = mycursor.fetchall()

        self.tree_modify.delete(*self.tree_modify.get_children())
        for user in info:
            self.tree_modify.insert(parent='', index='end', text='', values=user)


    def password_normal(self, event=None):
        if self.current_value.get() == 'Yes':
            self.entry_password.config(state='normal')

        else:
            self.entry_password.config(state='readonly')


    def send_data(self, event=None):
        current_item = self.tree_modify.focus()
        info = self.tree_modify.item(current_item)
        info = info['values']

        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        mycursor.execute("select * from Users where ID like '%{}'".format(info[0]))
        info1 = mycursor.fetchall()

        self.entry_ID.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_surname.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_kin_name.delete(0, END)
        self.entry_kin_phone.delete(0, END)
        self.entry_ID.insert(0, info1[0][0])
        self.current_id = info1[0][0]
        self.entry_phone.insert(0, info1[0][3])

        self.entry_name.insert(0, info[1])
        self.entry_surname.insert(0, info[2])


        mycursor.execute("select * from admin_users where ID='{}'".format(self.entry_ID.get()))
        info_admin = mycursor.fetchall()

        if info_admin:
            self.combo_admin_priv.current(0)
            self.entry_password.config(state='normal')
            self.entry_password.delete(0, END)
            self.entry_password.insert(0, info_admin[0][1])
        else:
            self.combo_admin_priv.current(1)
            self.entry_password.config(state='normal')
            self.entry_password.delete(0, END)
            self.entry_password.config(state='readonly')

        mycursor.execute("select * from next_of_kin where ID='{}'".format(self.entry_ID.get()))
        info_nex_of_kin = mycursor.fetchall()

        self.entry_kin_name.insert(0, info_nex_of_kin[0][1])
        self.entry_kin_phone.insert(0, info_nex_of_kin[0][2])


    def update(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        mycursor.execute("select * from admin_users where ID='{}'".format(self.current_id))
        admin_exist = mycursor.fetchall()


        if self.current_value.get() == 'Yes' and self.entry_password.get() == '':
            messagebox.showerror(message='Password entry field empty')

        elif self.current_id != self.entry_ID.get():
            messagebox.showerror(message='Cannot change ID')

        elif self.entry_ID.get() == '' or self.entry_name.get() == '' or self.entry_surname.get() == '' or \
                self.entry_surname == '' or self.entry_kin_name == '' or self.entry_kin_phone == '':
            messagebox.showerror(message='Check that all entry fields are not empty')


        elif self.current_value.get() == 'Yes' and admin_exist:
            query_admin = "update admin_users set password='{}' where ID='{}'".format(self.entry_password.get(),
                                                                                      self.current_id)
            mycursor.execute(query_admin)
            mydb.commit()
            query = "update Users set name='{}', surname='{}', phone='{}' " \
                    "where ID='{}'".format(self.entry_name.get(), self.entry_surname.get(),
                                           self.entry_phone.get(), self.current_id)
            mycursor.execute(query)
            mydb.commit()

            query_kin = "update next_of_kin set name='{}', phone='{}' where ID='{}'".format(self.current_id,
                                                                                            self.entry_kin_name,
                                                                                            self.entry_kin_phone)
            mycursor.execute(query_kin)
            mydb.commit()
            messagebox.showinfo(message='Update successful')


        elif self.current_value.get() == 'Yes' and not admin_exist:
            query_admin = "insert into admin_users (ID, password) values ('{}', '{}')".format(self.current_id,
                                                                                              self.entry_password.get()
                                                                                              )
            mycursor.execute(query_admin)
            mydb.commit()
            query = "update Users set name='{}', surname='{}', phone='{}' " \
                    "where ID='{}'".format(self.entry_name.get(), self.entry_surname.get(),
                                           self.entry_phone.get(), self.current_id)
            mycursor.execute(query)
            mydb.commit()

            query_kin = "update next_of_kin set name='{}', phone='{}' where ID='{}'".format(self.current_id,
                                                                                            self.entry_kin_name,
                                                                                            self.entry_kin_phone)
            mycursor.execute(query_kin)
            mydb.commit()
            messagebox.showinfo(message='Update successful')


        elif self.current_value.get() == 'No' and admin_exist:
            query_admin = "delete from admin_users where ID='{}'".format(self.current_id)
            mycursor.execute(query_admin)
            mydb.commit()
            self.entry_password.config(state='normal')
            self.entry_password.delete(0, END)
            self.entry_password.config(state='readonly')
            query = "update Users set name='{}', surname='{}', phone='{}' " \
                    "where ID='{}'".format(self.entry_name.get(), self.entry_surname.get(),
                                           self.entry_phone.get(), self.current_id)
            mycursor.execute(query)
            mydb.commit()

            query_kin = "update next_of_kin set name='{}', phone='{}' where ID='{}'".format(self.current_id,
                                                                                            self.entry_kin_name,
                                                                                            self.entry_kin_phone)
            mycursor.execute(query_kin)
            mydb.commit()
            messagebox.showinfo(message='Update successful')


        self.pop_treeview()


    def add(self):
        try:
            id_no = self.entry_ID.get()
            name = self.entry_name.get()
            surname = self.entry_surname.get()
            phone = self.entry_phone.get()

            name_kin = self.entry_kin_name.get()
            phone_kin = self.entry_kin_phone.get()


            rsaidnumber.parse(id_no)
            int(phone)
            int(phone_kin)

            if name == '' or surname == '' or phone == '' or name_kin == '' or phone_kin == '':
                messagebox.showerror(message='Empty entry fields not allowed')

            elif (len(phone) < 10 or len(phone) > 10) or (len(phone_kin) < 10 or len(phone_kin) > 10):
                messagebox.showerror(message='Phone numbers must be 10 digits')

            else:
                mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                               database='lifechoices_online', auth_plugin='mysql_native_password')

                mycursor = mydb.cursor()

                if self.current_value == 'Yes' or self.current_value == '':
                    if self.entry_password.get() == '':
                        messagebox.showerror(message="Admin Password cannot be empty. If you don't want admin "
                                                     "privileges, select 'No'")
                    else:
                        query_admin = "insert into admin_users (ID, password) values ('{}', '{}')".format(
                            self.current_id, self.entry_password.get())
                        mycursor.execute(query_admin)
                        mydb.commit()
                        query = "insert into Users (ID, name, surname, phone) values ('{}', '{}', '{}', '{}')".format(
                            id_no, name, surname, phone)
                        mycursor.execute(query)
                        mydb.commit()

                        query_kin = "insert into next_of_kin (ID, name, phone) values ('{}', '{}', '{}')".format(
                            id_no, name_kin, phone_kin)
                        mycursor.execute(query_kin)
                        mydb.commit()

                        self.pop_treeview()
                        messagebox.showinfo(message='Successfully added user')

                else:
                    query = "insert into Users (ID, name, surname, phone) values ('{}', '{}', '{}', '{}')".format(
                        id_no, name, surname, phone)
                    mycursor.execute(query)
                    mydb.commit()

                    query_kin = "insert into next_of_kin (ID, name, phone) values ('{}', '{}', '{}')".format(
                        id_no, name_kin, phone_kin)
                    mycursor.execute(query_kin)
                    mydb.commit()

                    self.pop_treeview()
                    messagebox.showinfo(message='user has been successfully added')

        except ValueError:
            messagebox.showerror(message="ID number or phone number(s) are invalid")

        except mysql.connector.errors.IntegrityError:
            messagebox.showerror(message='User with ID already exists')


    def remove(self):
        id_no = self.current_id
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        query_check = "select * from admin_users where ID='{}'".format(id_no)
        mycursor.execute(query_check)
        result = mycursor.fetchall()

        if not result:
            pass
        else:
            query_admin = "delete from admin_users where ID='{}'".format(id_no)
            mycursor.execute(query_admin)
            mydb.commit()

        query_kin = "delete from next_of_kin where ID='{}'".format(id_no)
        mycursor.execute(query_kin)
        mydb.commit()
        query = "delete from Users where ID='{}'".format(id_no)
        mycursor.execute(query)
        mydb.commit()


        self.pop_treeview()


    def register_frame(self):
        self.frame_register.place(rely=0, relx=0, anchor=NW)
        Misc.lift(self.frame_register)


    def pop_tree_register(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices2021', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        query = "select * from register"
        mycursor.execute(query)
        info = mycursor.fetchall()

        self.tree_register.delete(*self.tree_register.get_children())
        for user in info:
            self.tree_register.insert(parent='', index='end', text='', values=user)


    def sign_out_user(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        current_item = self.tree_register.focus()
        info = self.tree_register.item(current_item)
        info = info['values']
        print(info)


        if info[4] != '--:--':
            messagebox.showerror(message="User already signed out")

        else:
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute

            if hour <= 9:
                hour = '0' + str(hour)

            if minute <= 9:
                minute = '0' + str(minute)

            time = "{}:{}".format(hour, minute)
            query = "update register set time_out='{}' where ID like '%{}' and time_out='--:--'".format(time, info[1])
            mycursor.execute(query)
            mydb.commit()
            self.pop_tree_register()


    def back(self):
        self.frame_options.place(rely=0.5, relx=0.5, anchor=CENTER)
        Misc.lift(self.frame_options)



root = Tk()
app = AdminGUI(root)
root.mainloop()
