import sqlite3
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk

win1 = Tk()

#root=Tk()

conn = sqlite3.connect('wild.db')
c = conn.cursor()

#root = Tk()
#root.title("Wildlife Project")

# Function to display all records


def sar():


    ar = Tk()
    ar.title("All Reocrds")
    # ar.geometry("150x190")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT oid,* FROM wildlife")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(ar, text=printrec, font=fontStyle1)
    label.grid(row=3, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Function for displaying Classifications


def cal():

    CLA = Tk()
    CLA.title("Classifications")

    allbutton = Button(CLA, text="All", command=allcla, activeforeground="white", activebackground="green",
                       font=fontStyle1, width=30)
    allbutton.grid(row=0, column=0)
    thrbutton = Button(CLA, text="Threatened", command=thrcla, activeforeground="white", activebackground="green",
                       font=fontStyle1, width=30)
    thrbutton.grid(row=1, column=0)
    endbutton = Button(CLA, text="Endangered", command=endcla, activeforeground="white", activebackground="green",
                       font=fontStyle1, width=30)
    endbutton.grid(row=2, column=0)
    cributton = Button(CLA, text="Critically Endangered", command=cricla, activeforeground="white",
                       activebackground="green", font=fontStyle1, width=30)
    cributton.grid(row=3, column=0)

# Function to display ALL CLASSIFICATIONS

def allcla():
    all = Tk()
    all.title("All Classifications")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT * FROM cla")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(all, text=printrec, font=fontStyle1)
    label.grid(row=3, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Function to display THREATENED CLASSIFICATIONS


def thrcla():
    thr = Tk()
    thr.title("Threatened Species")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT * FROM cla WHERE cla='Threatened'")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(thr, text=printrec, font=fontStyle1)
    label.grid(row=3, column=1, columnspan=2)

    conn.commit()
    conn.close()

# Function to display ENDANGERED CLASSIFICATIONS


def endcla():
    end = Tk()
    end.title("Endangered Species")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT * FROM cla WHERE cla='Endangered'")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(end, text=printrec, font=fontStyle1)
    label.grid(row=3, column=1, columnspan=2)

    conn.commit()
    conn.close()

# Function to display CRITICALLY ENDANGERED CLASSIFICATIONS


def cricla():
    cri = Tk()
    cri.title("Critically Endangered Species")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT * FROM cla WHERE cla='Critically Endangered'")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(cri, text=printrec, font=fontStyle1)
    label.grid(row=3, column=1, columnspan=2)

    conn.commit()
    conn.close()

# Display page for DELETE


def delrec():
    global Del

    Del = Tk()
    Del.title("Delete Record")

    global dno

    dno = Entry(Del, width=30)
    dno.grid(row=0, column=1)
    dnolabel = Label(Del, text="Enter the record number to be deleted", font=fontStyle1)
    dnolabel.grid(row=0, column=0)
    dokbutton = Button(Del, text="OK", command=dconf, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    dokbutton.grid(row=1, column=1)

# CONFORMATION for DELETE


def dconf():
    global DCONF

    DCONF = Tk()
    DCONF.title("Confirm Deletion")

    dconflabel = Label(DCONF, text="Do you want to save these changes?", font=fontStyle1)
    dconflabel.grid(row=0, column=0)

    yesbutton = Button(DCONF, text="Yes", command=delt, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    yesbutton.grid(row=1, column=2)

    nobutton = Button(DCONF, text="No", command=desdel, activeforeground="white", activebackground="green",
                      font=fontStyle1)
    nobutton.grid(row=1, column=1)

# Function to destroy Tk box when NO


def desdel():
    DCONF.destroy()
    Del.destroy()

# Function to DELETE


def delt():
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    temp = dno.get()

    c.execute("SELECT species FROM wildlife WHERE oid=:oid",
              {
                  'oid': temp
              })
    x = c.fetchone()
    # y = x[0]
    # print(x[0])
    c.execute("DELETE FROM wildlife WHERE oid=:oid",
              {
                  'oid': temp
              })

    conn.commit()

    c.execute("DELETE FROM cla WHERE species=:name",
              {
                  'name': x[0]
              })

    Del.destroy()
    DCONF.destroy()

# Display page for INSERT


def insrec():
    global Insert

    Insert = Tk()
    Insert.title("Insert Record")

    global iname
    global inum

    iname = Entry(Insert, width=30)
    iname.grid(row=0, column=1)
    inum = Entry(Insert, width=30)
    inum.grid(row=1, column=1)
    inamelabel = Label(Insert, text="Enter the species name", font=fontStyle1)
    inamelabel.grid(row=0, column=0)
    inumlabel = Label(Insert, text="Enter the population", font=fontStyle1)
    inumlabel.grid(row=1, column=0)
    iokbutton = Button(Insert, text="OK", command=iconf, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    iokbutton.grid(row=2, column=1)

# CONFORMATION for INSERT


def iconf():
    global ICONF

    ICONF = Tk()
    ICONF.title("Confirm Insertion")

    iconflabel = Label(ICONF, text="Do you want to save these changes?", font=fontStyle1)
    iconflabel.grid(row=0, column=0)

    yesbutton = Button(ICONF, text="Yes", command=insert, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    yesbutton.grid(row=1, column=2)

    nobutton = Button(ICONF, text="No", command=desins, activeforeground="white", activebackground="green",
                      font=fontStyle1)
    nobutton.grid(row=1, column=1)

# Function to destroy Tk box when NO


def desins():
    ICONF.destroy()
    Insert.destroy()

# Function to INSERT


def insert():
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("INSERT INTO wildlife VALUES (:name, :num)",
              {
                  'num': inum.get(),
                  'name': iname.get()
              })

    conn.commit()

    t = inum.get()
    if int(t) >= 10000:
        clastr = "Threatened"
    elif 2000 <= int(t) < 5000:
        clastr = "Endangered"
    elif 0 <= int(t) < 2000:
        clastr = "Critically Endangered"

    c.execute("INSERT INTO cla VALUES (:name, :status)",
              {
                  'name': iname.get(),
                  'status': clastr
              })

    conn.commit()
    conn.close()

    Insert.destroy()
    ICONF.destroy()

# Display page for UPDATE


def uprec():
    global Up

    Up = Tk()
    Up.title("Update Record")

    global name
    global num
    global sno
    global dreason

    sno = Entry(Up, width=30)
    sno.grid(row=0, column=1)
    name = Entry(Up, width=30)
    name.grid(row=1, column=1)
    num = Entry(Up, width=30)
    num.grid(row=2, column=1)
    dreason = Entry(Up, width=30)
    dreason.grid(row=3, column=1)
    snolabel = Label(Up, text="Record number", font=fontStyle1)
    snolabel.grid(row=0, column=0)
    namelabel = Label(Up, text="Enter the species name", font=fontStyle1)
    namelabel.grid(row=1, column=0)
    numlabel = Label(Up, text="Enter the population change", font=fontStyle1)
    numlabel.grid(row=2, column=0)
    dreasonlabel = Label(Up, text="Enter reason of death", font=fontStyle1)
    dreasonlabel.grid(row=3, column=0)
    uokbutton = Button(Up, text="OK", command=upd, activeforeground="white", activebackground="green", font=fontStyle1)
    uokbutton.grid(row=4, column=1)

# Function to insert into DREASON


def drr(t):
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("INSERT INTO dreason VALUES(:name, :pop, :rea)",
              {
                  'name': name.get(),
                  'pop': t,
                  'rea': dreason.get()
              })

    conn.commit()
    conn.close()

    Up.destroy()

# Function for displaying all Casuses of deaths (CODs)


def COD():
    cod = Tk()
    cod.title("Causes of Death")
    # ar.geometry("150x190")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT * FROM dreason")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(cod, text=printrec, font=fontStyle1)
    label.grid(row=3, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Function for UPDATE


def upd():
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    recid = sno.get()

    c.execute("SElECT population FROM wildlife WHERE oid=:oid", {'oid': recid})
    t = c.fetchone()
    tem = num.get()
    tem = t[0] - int(tem)
    print(tem)
    #    print(tem)

    c.execute("UPDATE wildlife SET population = :num, species = :name WHERE oid=:oid",
              {
                  'num': tem,
                  'name': name.get(),
                  'oid': sno.get()
              })

    conn.commit()

    # t = tem
    if tem >= 10000:
        clastrr = "Threatened"
    elif 2000 <= tem < 5000:
        clastrr = "Endangered"
    elif 0 <= tem < 2000:
        clastrr = "Critically Endangered"

    c.execute("UPDATE cla set cla = :sta WHERE species=:name",
              {
                  'name': name.get(),
                  'sta': clastrr
              })

    conn.commit()
    conn.close()

    drr(tem)

# INVASIVE species page


def inv():
    iroot = Tk()
    iroot.title("Invasive species")

    isrbutton = Button(iroot, text="Show records", width=20, command=isar, activeforeground="white",
                       activebackground="green", font=fontStyle1)
    isrbutton.grid(row=1, column=1)

    iupdatebutton = Button(iroot, text="Update records", width=20, command=iuprec, activeforeground="white",
                           activebackground="green", font=fontStyle1)
    iupdatebutton.grid(row=0, column=1)

    iinsertbutton = Button(iroot, text="Insert Record", width=20, command=iinsrec, activeforeground="white",
                           activebackground="green", font=fontStyle1)
    iinsertbutton.grid(row=2, column=1)

    idelbutton = Button(iroot, text="Delete Record", width=20, command=idelrec, activeforeground="white",
                        activebackground="green", font=fontStyle1)
    idelbutton.grid(row=3, column=1)

# Function to display all record in INVASIVE


def isar():
    iar = Tk()
    iar.title("All Reocrds")
    # iar.geometry("150x190")

    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("SELECT oid,* FROM invasive")
    records = c.fetchall()

    print(records)
    printrec = ''

    for record in records:
        printrec += str(record) + "\n"

    label = Label(iar, text=printrec, font=fontStyle1)
    label.grid(row=3, column=0, columnspan=2)

    conn.commit()
    conn.close()

# DELETE page for INVASIVE


def idelrec():
    global iDel

    iDel = Tk()
    iDel.title("Delete Record")

    global idno

    idno = Entry(iDel, width=30)
    idno.grid(row=0, column=1)
    idnolabel = Label(iDel, text="Enter the record number to be deleted", font=fontStyle1)
    idnolabel.grid(row=0, column=0)
    idokbutton = Button(iDel, text="OK", command=idconf, activeforeground="white", activebackground="green",
                        font=fontStyle1)
    idokbutton.grid(row=1, column=1)

# CONFORMATION for INSERT in INVASIVE


def idconf():
    global IDCONF

    IDCONF = Tk()
    IDCONF.title("Confirm Deletion (INVASIVE)")

    idconflabel = Label(IDCONF, text="Do you want to save these changes?", font=fontStyle1)
    idconflabel.grid(row=0, column=0)

    yesbutton = Button(IDCONF, text="Yes", command=idelt, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    yesbutton.grid(row=1, column=2)

    nobutton = Button(IDCONF, text="No", command=idesins, activeforeground="white", activebackground="green",
                      font=fontStyle1)
    nobutton.grid(row=1, column=1)

# Function to destroy Tk box when NO in INVASIVE


def idesins():
    IDCONF.destroy()
    iDel.destroy()

# Function to DELETE in INVASIVE


def idelt():
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    temp = idno.get()
    c.execute("DELETE FROM invasive WHERE oid=:oid",
              {
                  'oid': temp
              })

    conn.commit()
    conn.close()

    iDel.destroy()
    IDCONF.destroy()

# UPDATE page for INVASIVE


def iuprec():
    global iUp

    iUp = Tk()
    iUp.title("Update Record")

    global name
    global num
    global sno
    global num2

    sno = Entry(iUp, width=30)
    sno.grid(row=0, column=1)
    name = Entry(iUp, width=30)
    name.grid(row=1, column=1)
    num = Entry(iUp, width=30)
    num.grid(row=2, column=1)
    snolabel = Label(iUp, text="Record number", font=fontStyle1)
    snolabel.grid(row=0, column=0)
    namelabel = Label(iUp, text="Enter the species name", font=fontStyle1)
    namelabel.grid(row=1, column=0)
    numlabel = Label(iUp, text="Enter the population change", font=fontStyle1)
    numlabel.grid(row=2, column=0)
    uokbutton = Button(iUp, text="OK", command=iupd, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    uokbutton.grid(row=4, column=1)

# Function to UPDATE in INVASIVE


def iupd():
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    recid = sno.get()

    c.execute("SElECT population FROM invasive WHERE oid=:oid", {'oid': recid})
    t = c.fetchone()
    tem = num.get()
    tem = t[0] + int(tem)
    tem1 = t[0]
    #    print(tem)

    c.execute("UPDATE invasive SET oldpopulation = :t, population = :num, species = :name WHERE oid=:oid",
              {

                  't': tem1,
                  'num': tem,
                  'name': name.get(),
                  'oid': sno.get()

              })

    conn.commit()
    conn.close()
    iUp.destroy()

# INSERT page for INVASIVE


def iinsrec():
    global iInsert

    iInsert = Tk()
    iInsert.title("Insert Record")

    global inum2
    global inum
    global iname

    iname = Entry(iInsert, width=30)
    iname.grid(row=0, column=1)
    inum = Entry(iInsert, width=30)
    inum.grid(row=1, column=1)
    inum2 = Entry(iInsert, width=30)
    inum2.grid(row=2, column=1)
    inamelabel = Label(iInsert, text="Enter the species name:", font=fontStyle1)
    inamelabel.grid(row=0, column=0, sticky=W)
    inumlabel = Label(iInsert, text="Enter the population 6 months back:", font=fontStyle1)
    inumlabel.grid(row=1, column=0, sticky=W)
    inum2label = Label(iInsert, text="Enter the population:", font=fontStyle1)
    inum2label.grid(row=2, column=0, sticky=W)
    iokbutton = Button(iInsert, text="OK", command=iiconf, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    iokbutton.grid(row=3, column=1)

# CONFORMATION for INSERT in INVASIVE


def iiconf():
    global IICONF

    IICONF = Tk()
    IICONF.title("Confirm Insertion (INVASIVE)")

    iiconflabel = Label(IICONF, text="Do you want to save these changes?", font=fontStyle1)
    iiconflabel.grid(row=0, column=0)

    yesbutton = Button(IICONF, text="Yes", command=iinsert, activeforeground="white", activebackground="green",
                       font=fontStyle1)
    yesbutton.grid(row=1, column=2)

    nobutton = Button(IICONF, text="No", command=idesins, activeforeground="white", activebackground="green",
                      font=fontStyle1)
    nobutton.grid(row=1, column=1)

# Function to destroy Tk box when NO


def idesins():
    IICONF.destroy()
    iInsert.destroy()

# Function to INSERT in INVASIVE


def iinsert():
    conn = sqlite3.connect('wild.db')
    c = conn.cursor()

    c.execute("INSERT INTO invasive VALUES (:name, :num, :num2)",
              {
                  'num': inum.get(),
                  'name': iname.get(),
                  'num2': inum2.get(),
              })

    conn.commit()
    conn.close()

    iInsert.destroy()
    IICONF.destroy()

# CONNECT function


def connecto():

    content = e1.get()
    content1 = e2.get()
    if (content == 'admin' and content1 == 'pass'):

        win1.destroy()
        root = Tk()
        root.title("Wildlife Conservation")

        fontStyle = tkFont.Font(family="Times", size=14, weight=tkFont.BOLD)
        fontStyle1 = tkFont.Font(family="Times", size=11, slant=tkFont.ITALIC)

        titlelabel = Label(root, text="Wildlife Conservation", font=fontStyle, foreground="green")
        titlelabel.grid(row=0, column=1, columnspan=30)

        srbutton = Button(root, text="Show records", width=30, command=sar, activeforeground="white",
                          activebackground="green", font=fontStyle1)
        srbutton.grid(row=1, column=1)

        updatebutton = Button(root, text="Update records", width=30, command=uprec, activeforeground="white",
                              activebackground="green", font=fontStyle1)
        updatebutton.grid(row=2, column=1)

        insertbutton = Button(root, text="Insert Record", width=30, command=insrec, activeforeground="white",
                              activebackground="green", font=fontStyle1)
        insertbutton.grid(row=3, column=1)

        delbutton = Button(root, text="Delete Record", width=30, command=delrec, activeforeground="white",
                           activebackground="green", font=fontStyle1)
        delbutton.grid(row=4, column=1)

        clabutton = Button(root, text="Classifications", width=30, command=cal, activeforeground="white",
                           activebackground="green", font=fontStyle1)
        clabutton.grid(row=5, column=1)

        dreasonbutton = Button(root, text="COD", width=30, command=COD, activeforeground="white",
                               activebackground="green", font=fontStyle1)
        dreasonbutton.grid(row=6, column=1)

        invbutton = Button(root, text="Invasive Species", width=30, command=inv, activeforeground="white",
                           activebackground="green", font=fontStyle1)
        invbutton.grid(row=7, column=1)

        root.mainloop()

fontStyle = tkFont.Font(family="Times", size=14, weight=tkFont.BOLD)
fontStyle1 = tkFont.Font(family="Times", size=11, slant=tkFont.ITALIC)

win1.title("Wildlife Conservation")
#win1.resizable(0, 0)
aLabel = ttk.Label(win1,  text="Welcome to Wildlife Conservation System")
aLabel.grid(column=0,  row=0)

aLabel = ttk.Label(win1, text="username")
aLabel.grid(column=0, row=1)

aLabel = ttk.Label(win1, text="password")
aLabel.grid(column=0, row=2)


username_text=StringVar()
e1 = ttk.Entry(win1, textvariable=username_text)
e1.grid(row=1, column=1)

password_text=StringVar()
e2 = ttk.Entry(win1, textvariable=password_text)
e2.grid(row=2, column=1)

b1 = ttk.Button(win1, text="Enter",  width=12, command=connecto)
b1.grid(row=3, column=1)

e1.bind('<Return>', connecto)
e2.bind('<Return>',  connecto)
win1.mainloop()


'''
#Create table for Classifications

#already done
#c.execute("CREATE TABLE cla (species text, cla text)")

conn.commit()


# main:

fontStyle = tkFont.Font(family="Times", size=14, weight=tkFont.BOLD)
fontStyle1 = tkFont.Font(family="Times", size=11, slant=tkFont.ITALIC)

titlelabel = Label(root, text="Wildlife Conservation", font=fontStyle, foreground="green")
titlelabel.grid(row=0, column=1, columnspan=30)

srbutton = Button(root, text="Show records", width=30, command=sar, activeforeground="white", activebackground="green",
                  font=fontStyle1)
srbutton.grid(row=1, column=1)

updatebutton = Button(root, text="Update records", width=30, command=uprec, activeforeground="white",
                      activebackground="green", font=fontStyle1)
updatebutton.grid(row=2, column=1)

insertbutton = Button(root, text="Insert Record", width=30, command=insrec, activeforeground="white",
                      activebackground="green", font=fontStyle1)
insertbutton.grid(row=3, column=1)

delbutton = Button(root, text="Delete Record", width=30, command=delrec, activeforeground="white",
                   activebackground="green", font=fontStyle1)
delbutton.grid(row=4, column=1)

clabutton = Button(root, text="Classifications", width=30, command=cal, activeforeground="white",
                   activebackground="green", font=fontStyle1)
clabutton.grid(row=5, column=1)

dreasonbutton = Button(root, text="COD", width=30, command=COD, activeforeground="white",
                       activebackground="green", font=fontStyle1)
dreasonbutton.grid(row=6, column=1)

invbutton = Button(root, text="Invasive Species", width=30, command=inv, activeforeground="white",
                   activebackground="green", font=fontStyle1)
invbutton.grid(row=7, column=1)

root.mainloop()
'''
'''
#Create table for Classifications


c.execute("CREATE TABLE cla (species text, cla text)")

conn.commit()
conn.close()


# Create table wildlife with attributes species name and population size


c.execute("""CREATE TABLE wildlife(species text, population integer)""")
conn.commit()

# Insert statements for the wildlife table


c.execute("""INSERT INTO wildlife VALUES ('Polar Bear','20000')""")
c.execute("""INSERT INTO wildlife VALUES ('Panda','2000')""")
c.execute("""INSERT INTO wildlife VALUES ('Cheetah','10000')""")
c.execute("""INSERT INTO wildlife VALUES ('Dolphin','1000')""")
c.execute("""INSERT INTO wildlife VALUES ('Elephant','50000')""")
c.execute("""INSERT INTO wildlife VALUES ('Leopard','7000')""")
c.execute("""INSERT INTO wildlife VALUES ('Lion','50000')""")
c.execute("""INSERT INTO wildlife VALUES ('Orangutan','7000')""")
c.execute("""INSERT INTO wildlife VALUES ('Rhinoceros','20000')""")
c.execute("""INSERT INTO wildlife VALUES ('Tiger','3500')""")

conn.commit()


# Create table dreason with attributes species name and decrease in population size and the cause


c.execute("""CREATE TABLE dreason(species text, populationdecrease integer, reason text)""")
conn.commit()
'''

'''
species and population sizes

polar bear - 20000
panda - 2000
cheetah - 10000
dolphins - 1000
elephant - 50000
leopard - 7000
lion - 50000
orangutan - 7000
rhinoceros - 20000
tiger - 3500
'''
'''
categories

threatened <= 10000
endangered <= 5000
critically endangered <= 2000
'''
