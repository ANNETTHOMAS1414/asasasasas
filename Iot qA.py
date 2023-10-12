from tkinter import*
import datetime

root = Tk()
root.geometry("1200x600+0+0")
root.resizable(0,0)
root.title("IoT Assignment")

Frame1 = Frame(root,bg="gainsboro")
Frame1.pack(side=TOP)

Frame2 = Frame(root)
Frame2.pack(side=TOP)

var = StringVar()

def calculate():
    order_no=int(order_entry.get())
    food_price=int(food_entry.get())
    food_name =str(food_nentry.get())
    drink_dessert=str(dd_entry.get())
    drides_price=int(drides_entry.get())
    tip=int(tip_entry.get())
    total=food_price+drides_price+tip
    var.set(f"Order Number: {order_no}\nFood Price: Rs.{food_price}\nDrink/Dessert Price:Rs.{drides_price}\nTotal Price: Rs.{total}")
    
     

lbl_info = Label(Frame1,font=('aria',30,'bold'),text="RESTAURANT BILLING SYSTEM",fg="navy",bd=10,anchor='w')
lbl_info.grid(row=0,column=0)

date = datetime.datetime.now()

date_info=Label(Frame1,font=('aria',20,'bold' ),text=str(f"{date.day}-{date.month}-{date.year}"),fg="navy",anchor=W)
date_info.grid(row=1,column=0)

order_no=Label(Frame2,font=('aria',16,'bold'),text="Order Number",fg="darkblue",bd=10,anchor='w')
order_no.grid(row=1,column=0)
order_entry=Entry(Frame2,font=('ariel',16,'bold'),bd=6,insertwidth=4,bg="white",justify='right')
order_entry.grid(row=1,column=1)

food_name = Label(Frame2,font=('aria',16,'bold'),text="Food Ordered",fg="darkblue",bd=10,anchor='w')
food_name.grid(row=2,column=0)
food_nentry=Entry(Frame2,font=('ariel',16,'bold'),bd=6,insertwidth=4,bg="white",justify='right')
food_nentry.grid(row=2,column=1)

food_price = Label(Frame2,font=('aria',16,'bold'),text="Food Price",fg="darkblue",bd=10,anchor='w')
food_price.grid(row=3,column=0)
food_entry=Entry(Frame2,font=('ariel',16,'bold'),bd=6,insertwidth=4,bg="white",justify='right')
food_entry.grid(row=3,column=1)

drink_dessert = Label(Frame2,font=('aria',16,'bold'),text="Drink/Dessert",fg="darkblue",bd=10,anchor='w')
drink_dessert.grid(row=4,column=0)
dd_entry=Entry(Frame2,font=('ariel',16,'bold'),bd=6,insertwidth=4,bg="white",justify='right')
dd_entry.grid(row=4,column=1)

drides_price = Label(Frame2,font=('aria',16,'bold'),text="Drink/Dessert Price",fg="darkblue",bd=10,anchor='w')
drides_price.grid(row=5,column=0)
drides_entry=Entry(Frame2,font=('ariel',16,'bold'),bd=6,insertwidth=4,bg="white",justify='right')
drides_entry.grid(row=5,column=1)

tip = Label(Frame2,font=('aria',16,'bold'),text="Tip",fg="darkblue",bd=10,anchor='w')
tip.grid(row=6,column=0)
tip_entry=Entry(Frame2,font=('ariel',16,'bold'),bd=6,insertwidth=4,bg="white",justify='right')
tip_entry.grid(row=6,column=1)

btn=Button(Frame2,padx=16,pady=8,bd=4,fg="black",font=('ariel',20,'bold'),text="CALCULATE",bg="limegreen",command=calculate )
btn.grid(row=7,column=1)

result_label=Label(Frame2,font=('aria',16,'bold'),textvariable=var,fg="black",bd=10,anchor='w')
result_label.grid(row=8,column=1)

root.mainloop()