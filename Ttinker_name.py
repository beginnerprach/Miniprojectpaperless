
#---------------------------------------------------------------
import uuid
from buildsqlfile import insert_imformation
from buildsqlfile import view_imformation
from tkinter import * 
from tkinter import ttk
GUI = Tk()
GUI.geometry('800x500')
GUI.title('Name for Certificate of Congratulations')
L = Label(GUI,text= 'Name for Certificate of' , font=('Angsana New ', 40))
L.pack()
#----------------------------------------------------------------
v_Namefull = StringVar()
L1 = Label(GUI,text= 'กรอกชื่อ - สกุล' , font=('Angsana New ',30 ))
L1.pack()
entry_name = Entry(GUI,textvariable=v_Namefull, width=55)
entry_name.pack()

#----------------------------------------------------------------

v_gender = StringVar()
L2 = Label(GUI,text= 'เพศ' , font=('Angsana New ',30 ))
L2.pack()
entry_name = Entry(GUI,textvariable=v_gender , width=30)
entry_name.pack()

#----------------------------------------------------------------
def save_information():
    Name = v_Namefull.get()
    Gender = v_gender.get()
    UIDStudent = uuid.uuid4().hex[:8]
    if Gender == 'male':
        WordUse = 'Mr.'
    elif Gender == 'female':
        WordUse = 'Ms.'
    elif Gender == 'ชาย' :
        WordUse = 'นาย'
    elif Gender == 'หญิง':
        WordUse = 'นางสาว'
    else :
        WordUse = ''
    insert_imformation(Name,Gender,UIDStudent,WordUse)
    v_gender.set('')
    v_Namefull.set('')
    print(view_imformation())

#---------------------------------------------------------------
Butt = ttk.Button(GUI,text='Save',command=save_information)
Butt.pack(pady = 35)
GUI.mainloop()

#---------------------------------------------------------------