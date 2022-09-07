from pandastable import Table, TableModel


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_absolute_error

from sklearn import datasets

from sklearn.model_selection import train_test_split

from sklearn import tree

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

#import imutils
import pytesseract
import sqlite3



 
def raise_frame(f):
    f.tkraise()
 
def finish():
    root.destroy()
def fr1():
    raise_frame(Fr1)
def fr2():
    raise_frame(Fr2) 
def fr3():
    raise_frame(Fr3)
def fr4():
    raise_frame(Fr4)
def fr5():
    raise_frame(Fr5)
def fr6():
    raise_frame(Fr6)

def fr7():
    raise_frame(Fr7)
def fr8():
    raise_frame(Fr8)
def fr9():
    raise_frame(Fr9)
def fr10():
    raise_frame(Fr10)
def fr11():
    raise_frame(Fr11)



def OpenData():
    global tail
    global D1
    global D2
    global data
    
    file=askopenfile(mode='r',filetypes=[('All files','*.csv')])
    #if file is not None:
    #    D1=file.read()
    #    D2=file.read()

    head, tail = os.path.split(str(file))
    tail=str(tail)
    tail=tail[:-29]
    messagebox.showinfo('MessageBox','File Selected successfully')
    data = pd.read_csv(tail)
    
    #print(data)
    #x1.set(data)
    data1=''
    for  i in range(len(data)):
        for j in range(len(data.columns)):
            data1+=str(data.iloc[i,j])+'\t'
        data1+='\n'
    print(data1)
    x1.set(data1)
    

    lab01 = Label(Fr3, fg="black",bg="black",width=43, height=29,
                  font = "Latin 10 bold").place(x = 1500,y=20)
    lab02 = Label(Fr3, fg="black",bg="pink",width=40, height=28,
                  font = "Latin 10 bold").place(x = 1511,y=32)
    

    lab03 = Label(Fr3, justify="left",text="Column Names",
                 fg="black",bg="white", font = "Latin 10 bold").place(x = 1550,y=35)

    lab04 = Label(Fr3, justify="left",text="Operations",
                 fg="black",bg="white", font = "Latin 10 bold").place(x = 1730,y=35)

    lab05 = Label(Fr3, justify="left",text="Select Column Names for Graph",
                 fg="black",bg="white", font = "Latin 8 bold").place(x = 1550,y=252)

    
    dd=[]
    for i in data.columns:
        dd.append(i)
    
    drop1 = OptionMenu(Fr3,clicked,*dd,command=display_selected)
    drop1.place(x = 1550, y = 60)

    dd1=['Sum','Mean','Max','Min']
    drop2 = OptionMenu(Fr3,clicked1,*dd1,command=display_selected1)
    drop2.place(x = 1730, y = 60)


    listbox = Listbox(Fr3, width=30, height=10, selectmode=MULTIPLE)

    for i in range(0,len(dd)):
        listbox.insert(i+1,dd[i])

    

    

    def graph1():
        global data
        cl=[]
        
        for i in listbox.curselection():
            print(listbox.get(i))
            cl.append(listbox.get(i))
            
        df = data
        monthList  = df [cl[0]].tolist()
        profitList = df [cl[1]].tolist()
        
        plt.plot(monthList, profitList, label = '')
        plt.xlabel(cl[0])
        plt.ylabel(cl[1])
        plt.xticks(monthList)
        #plt.title('Company profit per month')
        plt.yticks([100000, 200000, 300000, 400000, 500000])
        plt.show()

    def graph2():
        global data
        cl=[]
        
        for i in listbox.curselection():
            print(listbox.get(i))
            cl.append(listbox.get(i))
            
        df = data
        monthList  = df [cl[0]].tolist()
        faceCremSalesData   = df [cl[1]].tolist()
        faceWashSalesData   = df [cl[2]].tolist()

        plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = cl[1], align='edge')
        plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = cl[2], align='edge')
        plt.xlabel(cl[0])
        plt.ylabel('units in number')
        plt.legend(loc='upper left')
        #plt.title('Sales data')

        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        #plt.title('Facewash and facecream sales data')
        plt.show()
    
    btn1 = Button(Fr3, text='Display Graph1', command=graph1)
    btn2 = Button(Fr3, text='Display Graph2', command=graph2)

    btn1.place(x = 1750, y = 250)
    btn2.place(x = 1750, y = 450)
    listbox.place(x = 1550, y = 270)

choice=''
choice1=''
def display_selected(Z):
    global choice
    choice = clicked.get()
    print(choice)
def display_selected1(Z):
    global choice1,choice,data
    choice1 = clicked1.get()
    print(choice1+' '+choice)

    if(choice1=='Sum'):
        print(data[choice].sum())
        messagebox.showinfo('MessageBox','Sum is '+str(data[choice].sum()))
    if(choice1=='Mean'):
        print(data[choice].mean())
        messagebox.showinfo('MessageBox','Mean is '+str(data[choice].mean()))
    if(choice1=='Max'):
        print(data[choice].max())
        messagebox.showinfo('MessageBox','Max is '+str(data[choice].max()))
    if(choice1=='Min'):
        print(data[choice].min())
        messagebox.showinfo('MessageBox','Min is '+str(data[choice].min()))



    
def fun1():
    
    x1.set('')
    x3.set('')
    x4.set('')
    x5.set('')
    
    x2.set('')
    global tail
    global D1
    data = pd.read_csv(tail)
    print(data)
    
    D1=D1.replace(',','\t')
    x2.set(D1)

def fun2():

    x1.set('')
    x2.set('')
    x4.set('')
    x5.set('')
    
    x3.set('')
    global tail
    global D2
    
    data = pd.read_csv(tail)
    print(data.describe())
    D2=data.describe()
    x3.set(D2)

def fun3():
    
    x1.set('')
    x2.set('')
    x3.set('')
    x5.set('')
    global tail
    
    data = pd.read_csv(tail)
    
    grouped_df = data.groupby('Type of property')['Price in lakhs']


    mean_df = grouped_df.mean()
    print('group by mean')
    print(mean_df)
    
    x4.set('group by mean\n\n'+str(mean_df))
    
def fun4():
       
    x1.set('')
    x2.set('')
    x3.set('')
    x4.set('')
    global tail
    
    data = pd.read_csv(tail)
    
    grouped_df = data.groupby('Type of property')['Price in lakhs']
    s = grouped_df.std()

    print('group by std')
    print(s)
    
    x5.set('group by std\n\n'+str(s))
    
def fun5():

    x1.set('')
    x2.set('')
    x3.set('')
    x4.set('')
    x5.set('')
    global tail
    
    data = pd.read_csv(tail)
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    clf = DecisionTreeClassifier(random_state=1234)
    model = clf.fit(X, y)

    text_representation = tree.export_text(clf)
    print(text_representation)

    with open("decistion_tree.log", "w") as fout:
        fout.write(text_representation)

    fig = plt.figure(figsize=(25,20))
    _ = tree.plot_tree(clf,feature_names=iris.feature_names,class_names=iris.target_names,filled=True)

    fig.savefig("decistion_tree.png")
    x6.set(str(text_representation))
    
def fun6():
    
    x1.set('')
    x2.set('')
    x3.set('')
    x4.set('')
    x5.set('')
    global tail
    
    data = pd.read_csv(tail)
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    clf = DecisionTreeClassifier(random_state=1234)
    model = clf.fit(X, y)

    text_representation = tree.export_text(clf)
    print(text_representation)

    with open("decistion_tree.log", "w") as fout:
        fout.write(text_representation)

    fig = plt.figure(figsize=(25,20))
    _ = tree.plot_tree(clf,feature_names=iris.feature_names,class_names=iris.target_names,filled=True)

    fig.savefig("decistion_tree.png")
    x6.set(str(text_representation))
    messagebox.showinfo('MessageBox','Tree is created please check in folder')
    
def Save():
    global asky1
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    f.write(asky1)
    f.close()
def SaveKey():
    key=str(e2.get()) 
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    f.write(key)
    f.close()
def fun7():
    x2.set('')
def fun8():
    x2.set('')
def OpenKey():
    global D
    file=askopenfile(mode='r',filetypes=[('All files','*.txt')])
    if file is not None:
        D=file.read()
        x10.set(D)
    
def fun9():
    x2.set('')
def fun10():
    x2.set('')
    
def fun11():
    x2.set('')
    
def fun12():
    try:
        conn = sqlite3.connect('test1.db')
    
        #conn.execute('''CREATE TABLE COMPANY
        #     (Username TEXT PRIMARY KEY     NOT NULL,
        #     Password           TEXT    NOT NULL,
        #     Contactno       TEXT);''')
    
        un=txt1.get()
        pw=txt2.get()
        cont=txt3.get()
        
        q="INSERT INTO COMPANY (Username,Password,Contactno) VALUES(?,?,? )"
        v=(un,pw,cont)
        
        conn.execute(q,v)
        conn.commit()
        
        messagebox.showinfo('MessageBox','Registration successfully completed')
        x7.set('')
        x8.set('')
        x9.set('')
        
    except:
        messagebox.showinfo('MessageBox','IError pleae try again')
    
def fun13():
    try:
        conn = sqlite3.connect('test1.db')
        no=txt1.get()
        name=txt2.get()
        address=txt3.get()
        
        q="update COMPANY  set NAME=?,ADDRESS=? where No=?"
        v=(name,address,no)
        conn.execute(q,v)
        conn.commit()
        messagebox.showinfo('MessageBox','One record is updated successfully ')
        x7.set('')
        x8.set('')
        x9.set('')
    except:
        messagebox.showinfo('MessageBox','Error pleae try again')

def fun14():
    try:
        conn = sqlite3.connect('test1.db')
        no=txt1.get()
        
        q="delete from COMPANY where No=?"
        v=(no,)
        conn.execute(q,v)
        conn.commit()
        messagebox.showinfo('MessageBox','One record is deleted successfully ')
        x7.set('')
        x8.set('')
        x9.set('')
    except:
        messagebox.showinfo('MessageBox','Error pleae try again')
def fun15():
    try:
        yy=''
        conn = sqlite3.connect('test1.db')
        cursor = conn.execute("SELECT No, name, address from COMPANY")
        
        for row in cursor:
            yy+=str(row[0])+'\t'+row[1]+'\t'+row[2]+'\n'
        ll2.configure(text=yy)
    except:
        messagebox.showinfo('MessageBox','Error pleae try again')
    
def fun16():
    try:
        conn = sqlite3.connect('test1.db')
        username=txt4.get()
        password=txt5.get()
        cursor = conn.execute("SELECT username, password, contactno from COMPANY where username=? and password=?",(username,password))
        for row in cursor:
            x11.set(row[0])
            x12.set(row[1])
            x13.set(row[2])
        un=x11.get()
        pw=x12.get()
        if(un==username and pw==password):
            raise_frame(Fr6)
        else:
            messagebox.showinfo('MessageBox','sorry pleae try again')
    except:
        messagebox.showinfo('MessageBox','Error pleae try again')

def loginfun():
    raise_frame(Fr1)
def regfun():
    raise_frame(Fr2)
def homefun():
    raise_frame(Fr4)
def Helpfun():
    raise_frame(Fr5)
    
root = Tk()
menubar=Menu(root)
menubar.add_command(label="Home",command=homefun)
menubar.add_command(label="Login",command=loginfun)
menubar.add_command(label="Regi",command=regfun)
menubar.add_command(label="Help",command=Helpfun)
root.config(menu=menubar)


Fr0 = Frame(root)
Fr1 = Frame(root)
Fr2 = Frame(root)
Fr3 = Frame(root)
Fr4 = Frame(root)
Fr5 = Frame(root)
Fr6 = Frame(root)
Fr7 = Frame(root)
Fr8 = Frame(root)
Fr9 = Frame(root)
Fr10 = Frame(root)
Fr11 = Frame(root)


Fr0.place(x = 0,y = 0,height=400, width=1100)
Fr1.place(x = 0,y = 80,height=700, width=1100)
Fr2.place(x = 0,y = 80,height=700, width=1100)
Fr3.place(x = 0,y = 80,height=1500, width=1900)
Fr4.place(x = 0,y = 80,height=700, width=1100)

Fr5.place(x = 0,y = 80,height=700, width=1100)
Fr6.place(x = 0,y = 80,height=700, width=1100)


Fr0.config(bg='white')
Fr1.config(bg='white')
Fr2.config(bg='white')
Fr3.config(bg='white')
Fr4.config(bg='white')
Fr5.config(bg='white')
Fr6.config(bg='white')


x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()
x7=StringVar()
x8=StringVar()
x9=StringVar()
x10=StringVar()
x11=StringVar()
x12=StringVar()
x13=StringVar()
x14=StringVar()
x15=StringVar()
x16=StringVar()

clicked = StringVar()
clicked1 = StringVar()
clicked.set("Select")
clicked1.set("Select")
#HeadingPage




ph91=ImageTk.PhotoImage(Image.open("01.jpg"))
lab1 = Label(Fr0,bg='white',image=ph91).place(x = 80, y = 5)


#lab2 = Label(Fr0, justify="left",text = "Data Mining Techniques  in Machine Learning",
#                 fg="white",bg="black", font = "Latin 20 bold",height=1).place(x = 180,y=100)


#f = Frame(r)
    
#Fr6.pack(fill=BOTH,expand=1)
df = TableModel.getSampleData()
table = pt = Table(Fr6, dataframe=df,showtoolbar=True, showstatusbar=True)
pt.show()

#------------------------Login Page-----Fr-1--------------------


l5= Label(Fr1,text="Login Form", justify="left",fg="black",bg="white", font = "Helvetica 18 bold").place(x = 450, y =120)

lab2 = Label(Fr1, justify="left",text ='Username',fg="black",bg="white", font = "Century 14 bold",height=1,width=8).place(x = 350,y=200)
lab2 = Label(Fr1, justify="left",text ='Password',  fg="black",bg="white", font = "Century 14 bold",height=1,width=8).place(x = 350,y=250)

txt4 = Entry(Fr1, justify="left",bd=2,textvariable=x7 ,fg="black", font = "Century 12 bold",width=15)
txt4.place(x = 500,y=200)
txt5 = Entry(Fr1, justify="left",bd=2,textvariable=x8,fg="black", font = "Century 12 bold",width=15)
txt5.place(x = 500,y=250)

b9 = Button(Fr1, text = "SignIn",fg="black",bd=5, font = "Helvetica 14 bold",height=1,width=8,command=fun16).place(x = 380, y = 320)
b10 = Button(Fr1, text = "SignUp",fg="black",bd=5, font = "Helvetica 14 bold",height=1,width=8,command = fr2).place(x = 520, y = 320)

#------------------------Registration Page-----Fr-2--------------------

lab2 = Label(Fr2, justify="left",text = "Registration Form",
                 fg="black",bg="white", font = "Latin 18 bold",height=1).place(x = 380,y=120)

lab2 = Label(Fr2, justify="left",text ='Username',fg="black",bg="white", font = "Century 14 bold",height=1,width=8).place(x = 350,y=200)
lab2 = Label(Fr2, justify="left",text ='Password',  fg="black",bg="white", font = "Century 14 bold",height=1,width=8).place(x = 350,y=250)
lab2 = Label(Fr2, justify="left",text ='ContactNo.',fg="black",bg="white", font = "Century 14 bold",height=1,width=8).place(x = 350,y=300)


txt1 = Entry(Fr2, justify="left",bd=2,textvariable=x7 ,fg="black", font = "Century 12 bold",width=15)
txt1.place(x = 500,y=200)
txt2 = Entry(Fr2, justify="left",bd=2,textvariable=x8,fg="black", font = "Century 12 bold",width=15)
txt2.place(x = 500,y=250)
txt3 = Entry(Fr2, justify="left",bd=2,textvariable=x9,fg="black", font = "Century 12 bold",width=15)
txt3.place(x = 500,y=300)


b9 = Button(Fr2, text = "Submit",bd=3, font = "Helvetica 14 bold",height=1,width=7,command=fun12).place(x = 430, y = 380)


#------------------MainPage Fr3---------------------------------------------------------------------------

lab2 = Label(Fr3, justify="left",textvariable = x1,
                 fg="black",bg="white", font = "Latin 12 bold").place(x = 30,y=150)
lab2 = Label(Fr3, justify="left",textvariable = x2,
                 fg="black",bg="white", font = "Latin 12 bold").place(x = 50,y=150)
lab2 = Label(Fr3, justify="left",textvariable = x3,
                 fg="black",bg="white", font = "Latin 14 bold").place(x = 100,y=150)
lab2 = Label(Fr3, justify="left",textvariable = x4,
                 fg="black",bg="white", font = "Latin 14 bold").place(x = 100,y=150)
lab2 = Label(Fr3, justify="left",textvariable = x5,
                 fg="black",bg="white", font = "Latin 14 bold").place(x = 100,y=150)
lab2 = Label(Fr3, justify="left",textvariable = x6,
                 fg="black",bg="white", font = "Latin 10 bold").place(x = 100,y=150)

but3 = Button(Fr3, text = "Select File",
            bd=3, font = "Helvetica 10 bold",height=2,width=8,command = OpenData).place(x = 100, y = 20)

but5 = Button(Fr3, text = """Data
Describe""",
            bd=3, font = "Helvetica 10 bold",height=2,width=8,command = fun2).place(x = 200, y = 20)

but6 = Button(Fr3, text = "Mean",
            bd=3, font = "Helvetica 10 bold",height=2,width=8,command = fun3).place(x = 300, y = 20)

but5 = Button(Fr3, text = """Standard
Deviation""",
            bd=3, font = "Helvetica 10 bold",height=2,width=8,command = fun4).place(x = 400, y = 20)

but6 = Button(Fr3, text = """Coefficient
Variation""",
            bd=3, font = "Helvetica 10 bold",height=2,width=10,command = fun5).place(x = 500, y = 20)


#------------------------Conclusion-----Fr-5--------------------

l5= Label(Fr5,text="""Conclusion

            In todays real estate world it has become tough to store huge data and extract them for
            
            one’s requirement and also the extracted data should be useful. A lots of features that
            
            could be added to make the system more widely acceptable. The Decision tree regression
            
            algorithm is used to select relevant features which are used in predicting output of a
            
            database

 """, justify="left",fg="black",bg="white", font = "Helvetica 14 bold").place(x = 160, y =150)

#--------------------------Home---Fr-4--------------------

#l5= Label(Fr4,text='Home Page',justify="left",fg="black",bg="white", font = "Helvetica 14 bold").place(x = 160, y =150)

ph1=ImageTk.PhotoImage(Image.open("5.jpeg"))
lab1 = Label(Fr4,image=ph1).place(x = 0, y = 10)


#------------------------------------------------------------------------

raise_frame(Fr1)
root.geometry("1850x1500+0+0")
root.title("Data Mining Techniques  in Machine Learning")
root.mainloop()



