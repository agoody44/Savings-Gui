from tkinter import Tk, Button, Label,DoubleVar,Entry

window = Tk()
window.title("Monthly Savings App")
window.configure(background="#42b883")
window.geometry("350x500")
window.resizable(width=False,height=False)

def savings():
    # income_tax = (33 / 100)
    value = float(hourly_entry.get())
    daily = value * 8
    dv_value.set("%.2f" % daily)
    weekly = daily * 5
    wv_value.set("%.2f" % weekly)
    monthly = weekly * 4
    mv_value.set("%.2f" % monthly)
    value = float(bills_entry.get())
    bills = monthly - value
    bv_value.set("%.2f" % bills)


def clear():
    hourly_value.set("")
    bv_value.set("")
    dv_value.set("")
    wv_value.set("")
    mv_value.set("")

# houlry $
hourly_wage = Label(window,text="Hourly Wage",bg="red",fg="white",width=14)
hourly_wage.grid(column=0,row=0,padx=15,pady=15)

hourly_value = DoubleVar()
hourly_entry = Entry(window,textvariable=hourly_value,width=14)
hourly_entry.grid(column=1,row=0)
hourly_entry.delete(0,'end')

# bills $ option RED
bill_wage = Label(window,text="Damn Bills lol",bg="red",fg="white",width=14)
bill_wage.grid(column=0,row=2,padx=15,pady=15)

bv_value = DoubleVar()
bills_entry = Entry(window,textvariable=bv_value,width=14)
bills_entry.grid(column=1,row=2)
bills_entry.delete(0,'end')

# Weekly $ input block
weekly_wage = Label(window,text="Wage",bg="grey",fg="white",width=14)
weekly_wage.grid(column=0,row=3,padx=15,pady=15)

# Monthy $ input block
monthly_wage = Label(window,text="Wage",bg="grey",fg="white",width=14)
monthly_wage.grid(column=0,row=4,padx=15,pady=15)

# Daily wage option BLUE
dv_wage = Label(window,text= "Daily Wage",bg="blue",fg="white",width=14)
dv_wage.grid(column=0,row=3)

dv_value = DoubleVar()
dv_entry = Entry(window,textvariable=dv_value,width=14)
dv_entry.grid(column=1,row=3,pady=30)
dv_entry.delete(0,'end')

# Weekly wage option Blue
wv_wage = Label(window,text= "Weekly Wage",bg="blue",fg="white",width=14)
wv_wage.grid(column=0,row=4)

wv_value = DoubleVar()
wv_entry = Entry(window,textvariable=wv_value,width=14)
wv_entry.grid(column=1,row=4,pady=30)
wv_entry.delete(0,'end')

# Monlthy wage option BLUE
mv_wage = Label(window,text= "Monthly Wage",bg="blue",fg="white",width=14)
mv_wage.grid(column=0,row=5)

mv_value = DoubleVar()
mv_entry = Entry(window,textvariable=mv_value,width=14)
mv_entry.grid(column=1,row=5,pady=30)
mv_entry.delete(0,'end')

# Money left over
mv_wage = Label(window,text= "Money Left Over",bg="blue",fg="white",width=14)
mv_wage.grid(column=0,row=6)

bv_value = DoubleVar()
mv_entry = Entry(window,textvariable=bv_value,width=14)
mv_entry.grid(column=1,row=6,pady=30)
mv_entry.delete(0,'end')


wage_btn = Button(window,text="Wage",bg="grey",fg="black",width=14,command=savings)
wage_btn.grid(column=0,row=7,padx=15)

clear_btn = Button(window,text="Clear",bg="grey",fg="black",width=14,command=clear)
clear_btn.grid(column=1,row=7,padx=15)




window.mainloop()
