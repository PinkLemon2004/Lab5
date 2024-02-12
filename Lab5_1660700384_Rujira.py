from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("Calculator By Rujira")
    w = 320
    h = 500
    x = root.winfo_screenwidth()/2 - (w/2)
    y = root.winfo_screenheight()/2 - (h/2)
    root.geometry('%dx%d+%d+%d'%(w,h,x,y))
    root.configure(bg='lightgreen')

    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    return(root)

def createframe(root) :
    top = Frame(root,bg='#685555')
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    top.grid(row=0,column=0,sticky='news')
    
    btnnum = Frame(root,bg='#DD8484')
    btnnum.rowconfigure((0,1,2,3,4),weight=1)
    btnnum.columnconfigure((0,1,2,3),weight=2, uniform="buttons")
    btnnum.grid(row=1,column=0,sticky='news')

    return(root,top,btnnum)

def on_click(button_text):

    current_text = entry_var.get() # ดึงข้อมูลที่ป้อนเข้ามาที่ปัจจุบันใน Entry

    if button_text == "=": # ตรวจสอบถ้าปุ่มที่ถูกคลิกคือ "="
        try:
            result = eval(current_text) # หาผลลัพธ์จากตัวเลขและเครื่องหมายที่ป้อน
            entry_var.set(result)
        except Exception as e: # ถ้าไม่ได้ใส่ตัวเลขในการคำนวณจะขึ้น Error
            entry_var.set("Error")

    elif button_text == "ac": # ถ้าปุ่มที่ถูกคลิกคือ "ac"
        entry_var.set("0") # ให้รีเซ็ตค่าใน Entry เป็น "0"

    elif button_text == "clear": # ถ้าปุ่มที่ถูกคลิกคือ "clear"
        entry_var.set(current_text[:-1]) # ลบตัวอักษรที่ป้อนล่าสุด 1 ตำแหน่ง
    else:
        if current_text == "0" and button_text != ".": # ถ้าข้อมูลที่ป้อนคือ "0" และปุ่มที่ถูกคลิกไม่ใช่ "."
            entry_var.set(button_text) # รีเซ็ตค่าใน Entry เป็นปุ่มที่ถูกคลิก
        else:
            # เพิ่มปุ่มที่ถูกคลิกเข้าไปแทนที่เลข 0
            entry_var.set(current_text + button_text)

def widgettop(top) :
    labeltop = Entry(top,textvariable=entry_var,bg='#080808',font=('Arial',45),fg='#FFFFFF',justify='center')
    labeltop.grid(row= 0,column=0,sticky='news',ipady=15)

def widgetnum(btnnum):
    entry_var.set("0")
    row_val = 0
    col_val = 0
    
    #ลูปตัวเลข 1-9
    for i in range(1,10):
        row_val = (i-1) // 3 + 1
        col_val = (i-1) % 3 
        button_text = str(i)
        btn10 = Button(btnnum, text=button_text, font=('Arial', 16),bg='#080808',fg='#FFFFFF',bd=1, command=lambda btn=button_text: on_click(btn), height=2, width=6)
        btn10.grid(row=row_val, column=col_val,sticky='news')

    #เลข 0 และเครื่องหมายในการคำนวณ
    btn0 = Button(btnnum, text="0", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("0"), height=2, width=6)
    btn0.grid(row=4,columnspan=2,sticky='news')

    btnadd = Button(btnnum, text="+", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("+"), height=2, width=6)
    btnadd.grid(row=3, column=3,sticky='news')

    btnminus = Button(btnnum, text="-", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("-"), height=2, width=6)
    btnminus.grid(row=2, column=3,sticky='news')

    btnmuti = Button(btnnum, text="X", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("*"), height=2, width=6)
    btnmuti.grid(row=1, column=3,sticky='news')

    btndiv = Button(btnnum, text="/", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("/"), height=2, width=6)
    btndiv.grid(row=0, column=3,sticky='news')

    btneq = Button(btnnum, text="=", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("="), height=2, width=6)
    btneq.grid(row=4, column=3,sticky='news')

    btneqac = Button(btnnum, text="AC", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("ac"), height=2, width=6)
    btneqac.grid(row=0, column=0,sticky='news')

    btndel = Button(btnnum, text="Clear", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("clear"), height=2, width=6)
    btndel.grid(row=0, column=1,sticky='news')

    btndot = Button(btnnum, text=".", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("."), height=2, width=6)
    btndot.grid(row=4, column=2,sticky='news')

    btndot = Button(btnnum, text="%", font=('Arial', 16),fg='#FFFFFF',bg='#080808', command=lambda: on_click("%"), height=2, width=6)
    btndot.grid(row=0, column=2,sticky='news')

w = 320
h = 500
root = mainwindow()
entry_var = StringVar()
root,top,btnnum= createframe(root)
widgetnum(btnnum)
widgettop(top)
root.mainloop()
