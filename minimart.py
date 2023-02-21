from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import tkinter as tk
######################
import csv
def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file) #fw = ตัวแปร
        fw.writerow(datalist) # datalist = ['Pen', 'Pencil', 'Eraser']


def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
########################

#root = Tk() #main Program
#root.title('Easymart') #name of Program
#root.geometry('800x600') #size of Program


#########################


def calculate_total():
    quantity = int(quantity_input.get())
    price = float(price_input.get())
    total = quantity * price
    total_label.config(text="Total: {:.2f}".format(total))
    return total

root = tk.Tk()
root.title('Easymart')
root.geometry('800x600')

item1= ttk.Button(root, text='Regency')
item1.pack(ipadx=20,ipady=20)
item1.place(x=60,y=40)


quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack(ipadx=20,ipady=20)
quantity_label.place(x=200,y=20)

quantity_input = tk.Entry(root)
quantity_input.pack(ipadx=20,ipady=20)
quantity_input.place(x=200,y=40)

price_label = tk.Label(root, text="Price:")
price_label.pack(ipadx=20,ipady=20)
price_label.place(x=200,y=60)

price_input = tk.Entry(root)
price_input.pack(ipadx=20,ipady=20)
price_input.place(x=200,y=80)


###########SECTION RIGHT##############
#LF1 = ttk.LabelFrame(root, text='กรอกข้อมูลที่ต้องการ')
#LF1.place(x=400,y=100)

#v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
#E1 = ttk.Entry(LF1, textvariable=v_data, font=('Tahoma', 15))
#E1.pack(pady=10,padx=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_total)
calculate_button.pack(ipadx=20,ipady=20)
calculate_button.place(x=200,y=110)

total_label = tk.Label(root, text="Total:")
total_label.pack(ipadx=20,ipady=20)
total_label.place(x=200,y=140)

from datetime import datetime
def Savedata():
      t = datetime.now().strftime('%Y%m%D %H%M%S')
      sum1 = calculate_total()# นำค่า total จาก calculate_total มา
      text = [t, sum1] # [เวลา,ค่าผลลัพธ์จากการคำนวณ]
      writecsv(text) #บันทึกข้อมูล
    

B3 = ttk.Button(root,text='Save', command=Savedata)
B3.pack(ipadx=20,ipady=20)
B3.place(x=200,y=160)




root.mainloop()

