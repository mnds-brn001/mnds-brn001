from tkinter import *
import random
import string

top = Tk()
top.title('CopyAssignment Tkinter CRUD SQLite')
top.geometry('430x400')

def CreateOperation():
    from create import InsertData

    top1 = Tk()
    top1.geometry("300x200")
    top1.title("Create operation of CRUD")

    letters = string.ascii_lowercase
    random_id = ''.join(random.choice(letters) for i in range(8))

    name = StringVar(top1)
    ID = StringVar(top1)

    ID.set(random_id)

    Label(top1,text='Name').grid( row=0, column=0, padx=20, pady=20, sticky='w')
    Entry(top1, textvariable=name).grid (row=0, column=1,padx=20)

    Label(top1, text='ID(auto generated)').grid(row=1, padx= 20, column= 0, sticky='w')
    Entry(top1, textvariable= ID, state='disabled').grid(row=1, column=1)

    Button(top1, text='Create',fg='white',bg='green', font=('Arial',20), command=lambda: InsertData(name.get(),random_id)).grid(row=2,column=0,columnspan=2,pady=20)

    top1.mainloop()

Button(top,text="Create", bg='green',fg='white', width=12, font=('Arial',18),command=lambda: CreateOperation()).grid(row=0, column=0, padx=25,pady=30)

def ReadOperation():
    from read import Read

    top2 = Tk()
    top2.geometry('250x200')
    top2.title("Read operation of CRUD")

    Label(top2, text="Name").grid(row=0, column=0, padx=30, sticky='w')
    Label(top2, text='   |      ').grid(row=0,column=1)
    Label(top2, text='ID').grid(row=0, padx=20,column=2, sticky='w')

    Label(top2, text='--------'*5).grid(row=1, padx= 20, column= 0, columnspan= 5)

    data= Read()
    for i in range(len(data)):
        Label(top2, text=data[i][0]).grid(row=2+i, column=0, sticky='w', padx=20)
        Label(top2, text=" |  ").grid(row=2+i, column= 1)
        Label(top2, text=data[i][1]).grid(row=2+i, column=2, sticky='w')

    top2.mainloop()

Button(top, text='Read', bg='green', fg='white', width=12, font=("Arial",18), command=lambda:ReadOperation()).grid(row=0, column=1)

def UpdateOperation():
    from read import Read
    from update import Update

    top3= Tk()
    top3.geometry("250x200")
    top3.title('Operação de Atualização do CRUD')

    data= Read()
    id_list=[]
    for i in data:
        id_list.append(i[1])

    e = StringVar(top3)
    e.set('Select ID')
    OptionMenu(top3, e, *id_list).pack(pady=15)

    name = StringVar(top3)
    name.set('New name')
    Entry(top3, textvariable=name).pack(pady=15)

    def MyUpdate():
        Update(name.get(), e.get())
        top3.destroy()
    Button(top3, text="Update", command=lambda: MyUpdate(), bg='green', fg='white', font=('Arial',18)).pack(pady=15)

    top3.mainloop()

Button(top, text='Update', bg='green', fg='white', width=12, font=('Arial',18), command= lambda: UpdateOperation()).grid(row=1,pady=20, column=0)

def DeleteOperation():
    from read import Read
    from delete import Delete

    top4= Tk()
    top4.geometry('250x200')
    top4.title('Operação Deletar do CRUD')

    data= Read()
    id_list= []
    for i in data:
        id_list.append(i[1])

    e = StringVar(top4)
    e.set("Select ID")
    OptionMenu(top4, e, *id_list).pack()
    
    def MyDelete():
        Delete(e.get())
        top4.destroy()
    Button(top4, text="Delete", bg='Green', fg='white', width=12, font=("Arial", 18), command= lambda: MyDelete()).pack(pady=20)

    top4.mainloop ()

Button(top, text='Delete', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: DeleteOperation()).grid(row=1, column=1)

top.mainloop()