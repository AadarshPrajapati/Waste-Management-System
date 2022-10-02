from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('waste.db')
cur=con.cursor()

class AddBank(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('550x650+100+30')
        self.title('Add Bank Detail')
        self.resizable(False,False)


        #######################FRAMES###################################
        self.topFrame=Frame(self,height=150,bg='white')
        self.topFrame.pack(fill=X)
        self.bottomFrame=Frame(self,height=500,bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        #########################HEADING IMAGE##########################
        self.icons=PhotoImage(file='icon.png')
        self.top_image_lbl=Label(self.topFrame,image=self.icons,compound=LEFT,text=' Add Bank Detail',fg='#003f8a',bg='white',font='arial 22 bold')
        self.top_image_lbl.place(x=120,y=10)


        ##########################ENTRIES AND LABEL#####################

        Label(self.bottomFrame,text='Account_Type            :   ',bg='#fcc324',font='times 12 bold').place(x=130,y=10)
        self.account_type=StringVar()
        Radiobutton(self.bottomFrame,text='Savings',var=self.account_type,value='Savings',bg='#fcc324').place(x=300,y=12)
        Radiobutton(self.bottomFrame,text='Current',var=self.account_type,value='Current',bg='#fcc324').place(x=360,y=12)

        Label(self.bottomFrame, text='CIF Number               :   ', bg='#fcc324', font='times 12 bold').place(x=130, y=40)
        self.ent_cif=Entry(self.bottomFrame,width=30)
        self.ent_cif.place(x=300,y=45)

        Label(self.bottomFrame, text='Accn. Number            :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=70)
        self.ent_account =Entry(self.bottomFrame, width=30)
        self.ent_account.place(x=300, y=75)

        Label(self.bottomFrame, text='User Name                 :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=100)
        self.ent_name = Entry(self.bottomFrame, width=30)
        self.ent_name.place(x=300, y=105)

        Label(self.bottomFrame, text='Phone Number           :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=130)
        self.ent_phone = Entry(self.bottomFrame, width=30)
        self.ent_phone.place(x=300, y=135)

        Label(self.bottomFrame, text='IFSC Code                 :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=160)
        self.ent_ifsc = Entry(self.bottomFrame, width=30)
        self.ent_ifsc.place(x=300, y=165)

        Label(self.bottomFrame, text='MICR Code              :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=190)
        self.ent_micr = Entry(self.bottomFrame, width=30)
        self.ent_micr.place(x=300, y=195)

        Label(self.bottomFrame, text='Bank Name               :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=220)
        self.ent_bank = Entry(self.bottomFrame, width=30)
        self.ent_bank.place(x=300, y=225)

        Label(self.bottomFrame, text='Branch Name            :   ', bg='#fcc324', font='times 12 bold').place(x=130,y=250)
        self.ent_branch =Entry(self.bottomFrame, width=30)
        self.ent_branch.place(x=300, y=255)

        Button(self.bottomFrame,text='Submit',width=20,command=self.adddetail).place(x=220,y=330)






    def adddetail(self):
        bank_type=self.account_type.get()
        cif=self.ent_cif.get()
        account=self.ent_account.get()
        user=self.ent_name.get()
        phone=self.ent_phone.get()
        ifsc=self.ent_ifsc.get()
        micr=self.ent_micr.get()
        bank=self.ent_bank.get()
        branch=self.ent_branch.get()

        if(bank_type and cif and account and user and phone and ifsc and micr and bank and branch!=""):
            try:
                query="INSERT INTO 'bank'(user_bank_type,user_cif_no,user_account_no,user_name,user_phone,user_ifsc,user_micr,user_bank_name,user_branch_name) VALUES(?,?,?,?,?,?,?,?,?)"
                cur.execute(query,(bank_type,cif,account,user,phone,ifsc,micr,bank,branch))
                con.commit()
                messagebox.showinfo("Successful","Details added to database")
            except:
                messagebox.showinfo("Unsuccessful","Details can't be added to data base")
        else:
            messagebox.showerror("Error","Can't have empty field")






