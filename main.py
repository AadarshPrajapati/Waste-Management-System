from tkinter import *
from tkinter import ttk
import datetime
import addbankdetail
from tkinter import messagebox
date=datetime.datetime.today().date()
import sqlite3
cur=sqlite3.connect('waste.db')
con=cur.cursor()


class main(object):
    def __init__(self,master):
        self.master=master
        MainFrame=Frame(self.master)
        MainFrame.pack()

        ########################################### FRAMES ##########################################################
        self.top_frame=Frame(MainFrame,height=60,width=1150,bg='black',bd=3,relief=SUNKEN)
        self.top_frame.pack(fill=X,side=TOP)
        self.bottom_frame=Frame(MainFrame,height=550,width=1150,bd=3,bg='#afefe2',relief=RIDGE)
        self.bottom_frame.pack(fill=X,side=TOP)
        self.bottom_left=Frame(self.bottom_frame,width=766,height=550,bg='white',bd=2,relief=SUNKEN)
        self.bottom_left.pack(side=LEFT)
        self.bottom_right=Frame(self.bottom_frame,width=383,height=550,bg='white',bd=2,relief=SUNKEN)
        self.bottom_right.pack(side=RIGHT)

        self.extreme_bottom_frame=Frame(MainFrame,height=60,width=1150,bd=2,relief=SUNKEN,bg='black')
        self.extreme_bottom_frame.pack(fill=X,side=TOP)
        ######################################## SEARCH BOX #########################################################

        self.search_box=LabelFrame(self.bottom_right,text='Search Nearby Shop',width=383,height=70,font='times 10 bold',bg='#797979',fg='white',bd=1,relief=SUNKEN)
        self.search_box.place(x=0,y=0)
        self.ent_search=Entry(self.search_box,font='times ',width=25,bd=2,relief=RIDGE)
        self.ent_search.insert(5,'Enter_Shop_Name')
        self.ent_search.place(x=17,y=11)
        self.btn_search=Button(self.search_box,text='Search',font='times 12 bold',bg='white',width=11,height=1,bd=2,relief=RIDGE)
        self.btn_search.place(x=250,y=9)

        ###################################### WELCOME PORTAL ######################################################
        self.welcome_frame=Frame(self.bottom_right,height=480,width=383,bg='white')
        self.welcome_frame.place(x=0,y=71)
        self.lbl_welcome=Label(self.welcome_frame,text='WELCOME TO OUR PORTAL',font='copper 18 bold',bg='white',fg='#2d640b')
        self.lbl_welcome.grid(row=0,pady=5,padx=15)

        self.line=Label(self.welcome_frame,text="-----------------------------------------------------------",bg='white')
        self.line.grid(row=2)

        self.feedback=Text(self.welcome_frame,height=10,width=20,font='times 18 bold',wrap=WORD,bg='#afefe2')
        self.feedback.grid(row=3,pady=40)

        self.btn_feedback = Button(self.welcome_frame, text='Submit Feedback')
        self.btn_feedback.grid(row=4,column=0)




        ############### TABS ################################################################
        self.tab=ttk.Notebook(self.bottom_left)
        self.tab1=ttk.Frame(self.bottom_left)
        self.tab2=ttk.Frame(self.bottom_left)
        self.tab.add(self.tab1,text='Our Rate List')
        self.tab.add(self.tab2,text='Statistics')
        self.tab.place(x=0,y=0)

        self.list_rate=Listbox(self.tab1,height=52,width=60)
        self.list_rate.insert(0,"__________________________RATE__LIST________________________________________ ")
        self.list_rate.insert(1,"  1. Inert Waste            ----------- ₹22.1/kg")
        self.list_rate.insert(2,"  2. Biodegradable waste    -----------₹12.65/kg")
        self.list_rate.insert(3,"  3. White HDPE Plastic     -----------   ₹60/kg")
        self.list_rate.insert(4,"  4. PETscrap               -----------   ₹37/kg")
        self.list_rate.insert(5,"  5. Polycarbonate Bottle   -----------   ₹25/kg")
        self.list_rate.insert(6,"  6. Wine/Beer Bottle       -----------  ₹5/unit")
        self.list_rate.insert(7,"  7. Copper                 -----------   ₹45/kg")
        self.list_rate.insert(8,"  8. Newspaper              -----------   ₹19/kg")
        self.list_rate.insert(9,"  9. Plastic                -----------   ₹13/kg")
        self.list_rate.insert(10,"10.  Iron                  -----------   ₹20/kg")
        self.list_rate.grid(row=0,padx=(13,0))
        self.sb=Scrollbar(self.tab1,orient=VERTICAL,command=self.list_rate.yview)
        self.sb.grid(row=0,column=1,sticky=N+S)
        self.list_rate.config(yscrollcommand=self.sb.set)

        self.list_shop_info=Listbox(self.tab1,height=52,width=57)
        self.list_shop_info.grid(row=0,column=2,padx=3)
        self.list_shop_info.insert(0,'__________________________Shops_Near_To_You_________________________________')
        self.sb1 = Scrollbar(self.tab1, orient=VERTICAL, command=self.list_shop_info.yview)
        self.sb1.grid(row=0, column=3, sticky=N + S)
        self.list_shop_info.config(yscrollcommand=self.sb1.set)



        ############################################ BUTTONS ON TOP FRAME ####################################################
        self.btn_add_waste_detail=Button(self.top_frame,text='Add Waste Details')
        self.btn_add_waste_detail.grid(row=0,padx=4,pady=2)

        self.btn_request_for_waste = Button(self.top_frame, text='Add Request')
        self.btn_request_for_waste.grid(row=0,column=1, padx=4, pady=2)

        self.btn_add_picking_address = Button(self.top_frame, text='Add Address')
        self.btn_add_picking_address.grid(row=0,column=2, padx=4, pady=2)

        self.btn_add_bank_info = Button(self.top_frame, text='Add Bank Info',command=self.addbank)
        self.btn_add_bank_info.grid(row=0, column=3, padx=4, pady=2)

        self.btn_check_balance = Button(self.top_frame, text='Check Balance')
        self.btn_check_balance.grid(row=0, column=4, padx=4, pady=2)



        self.btn_change_password = Button(self.top_frame, text='Change Password')
        self.btn_change_password.place(x=1030,y=2)
        self.btn_calc_amount = Button(self.top_frame, text='Calc Amount')
        self.btn_calc_amount.grid(row=0,column=5,padx=4,pady=2)

        self.btn_redeem_money = Button(self.top_frame, text='Redeem Money')
        self.btn_redeem_money.grid(row=0,column=6,padx=4,pady=2)

        ################## BOTTOM FRAME BUTTON #################################################

        self.btn_logout=Button(self.extreme_bottom_frame,text='logout',bg='white',fg='black',height=1,width=8,font='times 12 bold')
        self.btn_logout.place(x=1050,y=13)

        self.user_id=Label(self.extreme_bottom_frame,text='User-Id : QSEZ 3265 985',font='times 12 bold',fg='white',bg='black')
        self.user_id.place(x=25,y=8)
        self.today = Label(self.extreme_bottom_frame, text=str(date),fg='red', bg='black')
        self.today.place(x=25,y=30)

    ############### FUNCTION ##############################

    def addbank(self):
        add=addbankdetail.AddBank()



def Application():
    root=Tk()
    root.title('Waste Management System')
    root.geometry('1150x650+160+30')

    main(root)
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    Application()