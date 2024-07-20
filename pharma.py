from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import  mysql.connector
from tkinter import messagebox





class PharmacyManagementSystem:
     def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        self.addmed_var=StringVar()
        self.refMed_var=StringVar()



        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                       bg='white',fg="dark cyan",font=("times new romman",50,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"C:\Users\HP\Desktop\pharma_project\first_logo.jpg")
        img1=img1.resize((100,90))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=60,y=20)
        # ------------------ dataframes------------------
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                 fg="dark cyan",font=("arial",16,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="dark cyan",font=("arial",16,"bold"))
        DataFrameRight.place(x=910,y=5,width=560,height=350)
        # ------------------buttons frame ----------------
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=535,width=1530,height=65)

        #=============main button==============
        btnAddData=Button(ButtonFrame,text ="Medicine Add",font=("arial",16,"bold"),bg="dark cyan",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(ButtonFrame,text ="UPDATE",font=("arial",16,"bold"),width=10,bg="dark cyan",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(ButtonFrame,text ="DELETE",font=("arial",16,"bold"),width=10,bg="red",fg="white")
        btnAddData.grid(row=0,column=2)


        btnAddData=Button(ButtonFrame,text ="RESET",font=("arial",16,"bold"),width=10,bg="dark cyan",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(ButtonFrame,text ="EXIT",font=("arial",16,"bold"),width=10,bg="dark cyan",fg="white")
        btnAddData.grid(row=0,column=4)

        #============search by ==========================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,width=10,font=("arial",16,"bold"),state="readonly")
        search_combo["values"]=("Ref","MedName","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame,bd= 3,width=12,font=("arial",17,"bold"))    
        txtSearch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,text ="SEARCH",font=("arial",16,"bold"),width=10,bg="dark cyan",fg="white")
        searchBtn.grid(row=0,column=8)

        showALL=Button(ButtonFrame,text ="SHOW  ",font=("arial",16,"bold"),width=10,bg="dark cyan",fg="white")
        showALL.grid(row=0,column=9)


        #=======================label and entry===============
        lblSearch=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:-",padx=2)
        lblSearch.grid(row=0,column=0,sticky=W)

        

        ref_combo=ttk.Combobox(DataFrameLeft,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=("Ref","MedName","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)


        lBLcompanyName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:-",padx=2,pady=6)
        lBLcompanyName.grid(row=1,column=0,sticky=W)

        txtcompanyno=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtcompanyno.grid(row=1,column=1)
        

        lBLtypeofmed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine:-",padx=2,pady=6)
        lBLtypeofmed.grid(row=2,column=0,sticky=W)

        comtypeofmed=ttk.Combobox(DataFrameLeft,width=27,font=("arial",13,"bold"),state="readonly")
        comtypeofmed["values"]=('Tablet','Liquid','Capsules','Topical Medicines','Drops','Inhales','Injection')
        comtypeofmed.current(0)    
        comtypeofmed.grid(row=2,column=1)
        



        #============ADD MEDICINE==============
        lBLmedicinename=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name:-",padx=2,pady=6)
        lBLmedicinename.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,width=27,font=("arial",13,"bold"),state="readonly")
        comMedicineName["values"]=('Nice','Novel')
        comMedicineName.current(0)    
        comMedicineName.grid(row=3,column=1)
        

        lbllotno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:-",padx=2,pady=6)
        lbllotno.grid(row=4,column=0,sticky=W)
        txtlotno=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtlotno.grid(row=4,column=1)


        lblissuedate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:-",padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtissuedate.grid(row=5,column=1)


        
        lblexpdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:-",padx=2,pady=6)
        lblexpdate.grid(row=6,column=0,sticky=W)
        txtexpdate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtexpdate.grid(row=6,column=1)


        lbluses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:-",padx=2,pady=4)
        lbluses.grid(row=7,column=0,sticky=W)
        txtuses=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtuses.grid(row=7,column=1)


        lblsf=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:-",padx=2,pady=6)
        lblsf.grid(row=8,column=0,sticky=W)
        txtsf=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtsf.grid(row=8,column=1)

        lblprecwar=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:-",padx=15)
        lblprecwar.grid(row=0,column=2,sticky=W)
        txtprecwar=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtprecwar.grid(row=0,column=3)


        lbldosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:-",padx=15,pady=6)
        lbldosage.grid(row=1,column=2,sticky=W)
        txtdosage=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtdosage.grid(row=1,column=3)


        lblprice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price:-",padx=15)
        lblprice.grid(row=2,column=2,sticky=W)
        txtprice=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtprice.grid(row=2,column=3)


        lblquantity=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Product Quantity:-",padx=15)
        lblquantity.grid(row=3,column=2,sticky=W)
        txtquantity=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtquantity.grid(row=3,column=3)

        #====================IAMGES============

        lblhome=Label(DataFrameLeft,font=("arial",16,"bold"),text=" Stay Home Stay Safe",padx=15,fg="green",width=37)
        lblhome.place(x=410,y=140)


        img2=Image.open(r"C:\Users\HP\Desktop\pharma_project\second_logo.jpg")
        img2=img2.resize((140,135))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=500,y=340)

        img3=Image.open(r"C:\Users\HP\Desktop\pharma_project\third_logo.jpg")
        img3=img3.resize((150,135))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=780,y=340)


        img4=Image.open(r"C:\Users\HP\Desktop\pharma_project\fourth_logo.jpg")
        img4=img4.resize((130,135))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=645,y=340)


#=================================data frame right



        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
                                 fg="dark cyan",font=("arial",16,"bold"))
        DataFrameRight.place(x=910,y=5,width=560,height=350)

        img5=Image.open(r"C:\Users\HP\Desktop\pharma_project\fifth_logo.jpg")
        img5=img5.resize((130,135))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1335,y=165)




        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text=" Reference No.:-",padx=15,pady=6)
        lblrefno.place(x=-20,y=8)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",12,"bold"),bg="white",bd=2, relief=RIDGE,width=20)
        txtrefno.place(x=135,y=10)


        
        lblmedn=Label(DataFrameRight,font=("arial",12,"bold"),text=" Medicine Name:-",padx=15,pady=6)
        lblmedn.place(x=-20,y=40)
        txtmedn=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2, relief=RIDGE,width=20)
        txtmedn.place(x=135,y=40)


        #=========side frame===============
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=5,y=90,width=320,height=210)


        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("Ref","MedName"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("Ref",text="Ref")
        self.medicine_table.heading("MedName",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("Ref",width=100)
        self.medicine_table.column("MedName",width=100)

        #=================medicine add buttons==============
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        down_frame.place(x=360,y=150,width=126,height=160)

        btnaddmed=Button(down_frame,text ="ADD",font=("arial",12,"bold"),width=11,bg="sky blue",fg="white",pady=4)
        btnaddmed.grid(row=0,column=0)

        btnupdmed=Button(down_frame,text ="UPDATE",font=("arial",12,"bold"),width=11,bg="sky blue",fg="white",pady=4)
        btnupdmed.grid(row=1,column=0)

        btndeltmed=Button(down_frame,text ="DELETE",font=("arial",12,"bold"),width=11,bg="sky blue",fg="white",pady=4)
        btndeltmed.grid(row=2,column=0)

        btnclrmed=Button(down_frame,text ="CLEAR",font=("arial",12,"bold"),width=11,bg="sky blue",fg="white",pady=4)
        btnclrmed.grid(row=3,column=0)

#=======================frame details======================

        framedetails=Frame(self.root,bd=10,relief=RIDGE,bg="white")
        framedetails.place(x=0,y=600,width=1530,height=185)




        #==============main table and scrollbar============

        table_frame=Frame(self.root,bd=12,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=600,width=1530,height=160)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.pharmacy_table=ttk.Treeview(table_frame,columns=("reg","companyname","type","tabletname","lotno","issuedate","expdate"
                                                              ,"uses","sideeffects","warning","dosage","price","productqt"),
                                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No.")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No.")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffects",text="Side Effects")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qty")
        
        


        #=====================sql=====================
     def Addmed(self):
            conn=mysql.connector.connect(host='LAPTOP-SAKSOV5R ',user='root@localhost',password='devansh@sql',database='placement')
            my_cursor=conn.cursor()
            my_cursor.execute("insert into god(Ref,MedName) values(%s,%s)",(

                                                                self.refMed_var.get(),
                                                                self.addmed_var.get(),

                                                                            ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Medicine Added") 
           
    

     
            

if  __name__ == "__main__":
     root=Tk()
     obj=PharmacyManagementSystem(root)
     root.mainloop()