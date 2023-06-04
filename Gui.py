import tkinter as tk
import Methods as m

window = tk.Tk()
window.geometry("1000x500+0+0")
window.title("Restaurant Billing System by Syed Dayim Shah")

var1, var2, var3, var4 = tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var5, var6, var7, var8, var9 = tk.IntVar(), tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var10, var11, var12, var13, var14 = tk.IntVar(), tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var15, var16, var17, var18 = tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()

Frame_Top = tk.Frame()
Frame_Top.place(relx=0, rely=0.003, relheight=1, relwidth=1)
Frame_Top.configure(relief='groove')
Frame_Top.configure(borderwidth="8")
Frame_Top.configure(relief="groove")
Frame_Top.configure(background="#d9d9d8")

Label_Name = tk.Label()
Label_Name.place(relx=0.004, rely=0.01, relheight=0.08, width=1353)
Label_Name.configure(background="#000000")
Label_Name.configure(borderwidth="4")
Label_Name.configure(disabledforeground="#a3a3a3")
Label_Name.configure(font="-family {OCR A Std} -size 25 -weight bold")
Label_Name.configure(foreground="#ffffff")
Label_Name.configure(text='''RESTAURANT BILLING SYSTEM''')

Frame_left = tk.Frame(Frame_Top)
Frame_left.place(relx=0, rely=0.08, relheight=0.645, relwidth=0.35)
Frame_left.configure(relief='groove')
Frame_left.configure(borderwidth="8")
Frame_left.configure(relief="groove")
Frame_left.configure(background="#d9d9d9")

Frame_middle = tk.Frame(Frame_Top)
Frame_middle.place(relx=0.347, rely=0.08, relheight=0.645, relwidth=0.354)
Frame_middle.configure(relief='groove')
Frame_middle.configure(borderwidth="8")
Frame_middle.configure(relief="groove")
Frame_middle.configure(background="#d9d9d9")

Frame_bottom = tk.Frame(Frame_Top)
Frame_bottom.place(relx=0, rely=0.72, relheight=0.28, relwidth=0.7)
Frame_bottom.configure(relief='groove')
Frame_bottom.configure(borderwidth="8")
Frame_bottom.configure(relief="groove")
Frame_bottom.configure(background="#c1c2c9")

Frame_right = tk.Frame(Frame_Top)
Frame_right.place(relx=0.697, rely=0.080, relheight=0.38, relwidth=0.31)
Frame_right.configure(relief='groove')
Frame_right.configure(borderwidth="8")
Frame_right.configure(relief="groove")
Frame_right.configure(background="#d9d9d9")

Frame_bottom_right = tk.Frame(Frame_Top)
Frame_bottom_right.place(relx=0.697, rely=0.43, relheight=0.5, relwidth=0.31)
Frame_bottom_right.configure(relief='groove')
Frame_bottom_right.configure(borderwidth="8")
Frame_bottom_right.configure(relief="groove")
Frame_bottom_right.configure(background="#d9d9d9")

listbox_Drinks = tk.Listbox(Frame_bottom)
listbox_Drinks.place(relx=0.3, rely=0.05, relheight=0.2, relwidth=0.2)
listbox_Drinks.configure(background="#d9d9d8")
listbox_Drinks.configure(disabledforeground="#a3a3a3")
listbox_Drinks.configure(font="-family {Segoe UI} -size 14")
listbox_Drinks.configure(foreground="black")
listbox_Drinks.configure(highlightbackground="#d9d9d9")
listbox_Drinks.configure(highlightcolor="black")
listbox_Drinks.configure(borderwidth="5")
listbox_Drinks.configure(justify="right")

listbox_Cakes = tk.Listbox(Frame_bottom)
listbox_Cakes.place(relx=0.3, rely=0.29, relheight=0.2, relwidth=0.2)
listbox_Cakes.configure(background="#d9d9d8")
listbox_Cakes.configure(disabledforeground="#a3a3a3")
listbox_Cakes.configure(font="-family {Segoe UI} -size 14")
listbox_Cakes.configure(foreground="black")
listbox_Cakes.configure(highlightbackground="#d9d9d9")
listbox_Cakes.configure(highlightcolor="black")
listbox_Cakes.configure(borderwidth="5")
listbox_Cakes.configure(justify="right")

listbox_Charge = tk.Listbox(Frame_bottom)
listbox_Charge.place(relx=0.3, rely=0.54, relheight=0.2, relwidth=0.2)
listbox_Charge.configure(background="#d9d9d8")
listbox_Charge.configure(disabledforeground="#a3a3a3")
listbox_Charge.configure(font="-family {Segoe UI} -size 14")
listbox_Charge.configure(foreground="black")
listbox_Charge.configure(highlightbackground="#d9d9d9")
listbox_Charge.configure(highlightcolor="black")
listbox_Charge.configure(borderwidth="5")
listbox_Charge.configure(justify="right")

Cash_Entry = tk.Entry(Frame_bottom)
Cash_Entry.place(relx=0.3, rely=0.78, relheight=0.2, relwidth=0.2)
Cash_Entry.configure(background="#d9d9d8")
Cash_Entry.configure(disabledforeground="#a3a3a3")
Cash_Entry.configure(font="-family {Segoe UI} -size 14")
Cash_Entry.configure(foreground="black")
Cash_Entry.configure(highlightbackground="#d9d9d9")
Cash_Entry.configure(highlightcolor="black")
Cash_Entry.configure(borderwidth="5")
Cash_Entry.configure(justify="right")

Tax_Listbox = tk.Listbox(Frame_bottom)
Tax_Listbox.place(relx=0.75, rely=0.05, relheight=0.2, relwidth=0.2)
Tax_Listbox.configure(background="#d9d9d8")
Tax_Listbox.configure(disabledforeground="#a3a3a3")
Tax_Listbox.configure(font="-family {Segoe UI} -size 14")
Tax_Listbox.configure(foreground="black")
Tax_Listbox.configure(highlightbackground="#d9d9d9")
Tax_Listbox.configure(highlightcolor="black")
Tax_Listbox.configure(borderwidth="5")
Tax_Listbox.configure(justify="right")

Sub_Listbox = tk.Listbox(Frame_bottom)
Sub_Listbox.place(relx=0.75, rely=0.29, relheight=0.2, relwidth=0.2)
Sub_Listbox.configure(background="#d9d9d8")
Sub_Listbox.configure(disabledforeground="#a3a3a3")
Sub_Listbox.configure(font="-family {Segoe UI} -size 14")
Sub_Listbox.configure(foreground="black")
Sub_Listbox.configure(highlightbackground="#d9d9d9")
Sub_Listbox.configure(highlightcolor="black")
Sub_Listbox.configure(borderwidth="5")
Sub_Listbox.configure(justify="right")

Total_Listbox = tk.Listbox(Frame_bottom)
Total_Listbox.place(relx=0.75, rely=0.54, relheight=0.2, relwidth=0.2)
Total_Listbox.configure(background="#d9d9d8")
Total_Listbox.configure(disabledforeground="#a3a3a3")
Total_Listbox.configure(font="-family {Segoe UI} -size 14")
Total_Listbox.configure(foreground="black")
Total_Listbox.configure(highlightbackground="#d9d9d9")
Total_Listbox.configure(highlightcolor="black")
Total_Listbox.configure(borderwidth="5")
Total_Listbox.configure(justify="right")

listbox_Remain = tk.Listbox(Frame_bottom)
listbox_Remain.place(relx=0.75, rely=0.78, relheight=0.2, relwidth=0.2)
listbox_Remain.configure(background="#d9d9d8")
listbox_Remain.configure(disabledforeground="#a3a3a3")
listbox_Remain.configure(font="-family {Segoe UI} -size 14")
listbox_Remain.configure(foreground="black")
listbox_Remain.configure(highlightbackground="#d9d9d9")
listbox_Remain.configure(highlightcolor="black")
listbox_Remain.configure(borderwidth="5")
listbox_Remain.configure(justify="right")

listbox = tk.Listbox(Frame_bottom_right)
listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
listbox.configure(background="black")
listbox.configure(disabledforeground="#a3a3a3")
listbox.configure(font="-family {Segoe UI} -size 8")
listbox.configure(foreground="white")
listbox.configure(highlightbackground="#d9d9d9")
listbox.configure(highlightcolor="black")
listbox.configure(borderwidth="5")

Entry_Cal = tk.Entry(Frame_right)
Entry_Cal.place(relx=0.02, rely=0.03, height=45, relwidth=0.71, bordermode='ignore')
Entry_Cal.configure(background="#c1c2c9")
Entry_Cal.configure(disabledforeground="#a3a3a3")
Entry_Cal.configure(font="-family {Segoe UI} -size 14")
Entry_Cal.configure(foreground="#000000")
Entry_Cal.configure(insertbackground="black")
Entry_Cal.configure(borderwidth="5")
Entry_Cal.configure(justify="right")

Latte_Entry = tk.Entry(Frame_left)
Latte_Entry.place(relx=0.7, rely=0.1, height=35, relwidth=0.2, bordermode='ignore')
Latte_Entry.configure(background="white")
Latte_Entry.configure(disabledforeground="#a3a3a3")
Latte_Entry.configure(font="-family {Segoe UI} -size 14")
Latte_Entry.configure(foreground="#000000")
Latte_Entry.configure(insertbackground="black")
Latte_Entry.configure(borderwidth="5")

Espresso_Entry = tk.Entry(Frame_left)
Espresso_Entry.place(relx=0.7, rely=0.2, height=35, relwidth=0.2, bordermode='ignore')
Espresso_Entry.configure(background="white")
Espresso_Entry.configure(disabledforeground="#a3a3a3")
Espresso_Entry.configure(font="-family {Segoe UI} -size 14")
Espresso_Entry.configure(foreground="#000000")
Espresso_Entry.configure(insertbackground="black")
Espresso_Entry.configure(borderwidth="5")

Iced_latte_Entry = tk.Entry(Frame_left)
Iced_latte_Entry.place(relx=0.7, rely=0.3, height=35, relwidth=0.2, bordermode='ignore')
Iced_latte_Entry.configure(background="white")
Iced_latte_Entry.configure(disabledforeground="#a3a3a3")
Iced_latte_Entry.configure(font="-family {Segoe UI} -size 14")
Iced_latte_Entry.configure(foreground="#000000")
Iced_latte_Entry.configure(insertbackground="black")
Iced_latte_Entry.configure(borderwidth="5")

SexOn_Entry = tk.Entry(Frame_left)
SexOn_Entry.place(relx=0.7, rely=0.4, height=35, relwidth=0.2, bordermode='ignore')
SexOn_Entry.configure(background="white")
SexOn_Entry.configure(disabledforeground="#a3a3a3")
SexOn_Entry.configure(font="-family {Segoe UI} -size 14")
SexOn_Entry.configure(foreground="#000000")
SexOn_Entry.configure(insertbackground="black")
SexOn_Entry.configure(borderwidth="5")

Cappucino_Entry = tk.Entry(Frame_left)
Cappucino_Entry.place(relx=0.7, rely=0.5, height=35, relwidth=0.2, bordermode='ignore')
Cappucino_Entry.configure(background="white")
Cappucino_Entry.configure(disabledforeground="#a3a3a3")
Cappucino_Entry.configure(font="-family {Segoe UI} -size 14")
Cappucino_Entry.configure(foreground="#000000")
Cappucino_Entry.configure(insertbackground="black")
Cappucino_Entry.configure(borderwidth="5")

Frappé_Entry = tk.Entry(Frame_left)
Frappé_Entry.place(relx=0.7, rely=0.6, height=35, relwidth=0.2, bordermode='ignore')
Frappé_Entry.configure(background="white")
Frappé_Entry.configure(disabledforeground="#a3a3a3")
Frappé_Entry.configure(font="-family {Segoe UI} -size 14")
Frappé_Entry.configure(foreground="#000000")
Frappé_Entry.configure(insertbackground="black")
Frappé_Entry.configure(borderwidth="5")

Doppio_Entry = tk.Entry(Frame_left)
Doppio_Entry.place(relx=0.7, rely=0.7, height=35, relwidth=0.2, bordermode='ignore')
Doppio_Entry.configure(background="white")
Doppio_Entry.configure(disabledforeground="#a3a3a3")
Doppio_Entry.configure(font="-family {Segoe UI} -size 14")
Doppio_Entry.configure(foreground="#000000")
Doppio_Entry.configure(insertbackground="black")
Doppio_Entry.configure(borderwidth="5")

Iced_cap_Entry = tk.Entry(Frame_left)
Iced_cap_Entry.place(relx=0.7, rely=0.8, height=35, relwidth=0.2, bordermode='ignore')
Iced_cap_Entry.configure(background="white")
Iced_cap_Entry.configure(disabledforeground="#a3a3a3")
Iced_cap_Entry.configure(font="-family {Segoe UI} -size 14")
Iced_cap_Entry.configure(foreground="#000000")
Iced_cap_Entry.configure(insertbackground="black")
Iced_cap_Entry.configure(borderwidth="5")

Mojito_Entry = tk.Entry(Frame_left)
Mojito_Entry.place(relx=0.7, rely=0.9, height=35, relwidth=0.2, bordermode='ignore')
Mojito_Entry.configure(background="white")
Mojito_Entry.configure(disabledforeground="#a3a3a3")
Mojito_Entry.configure(font="-family {Segoe UI} -size 14")
Mojito_Entry.configure(foreground="#000000")
Mojito_Entry.configure(insertbackground="black")
Mojito_Entry.configure(borderwidth="5")

Cheese_Entry = tk.Entry(Frame_middle)
Cheese_Entry.place(relx=0.7, rely=0.1, height=35, relwidth=0.2, bordermode='ignore')
Cheese_Entry.configure(background="white")
Cheese_Entry.configure(disabledforeground="#a3a3a3")
Cheese_Entry.configure(font="-family {Segoe UI} -size 14")
Cheese_Entry.configure(foreground="#000000")
Cheese_Entry.configure(insertbackground="black")
Cheese_Entry.configure(borderwidth="5")

Red_Entry = tk.Entry(Frame_middle)
Red_Entry.place(relx=0.7, rely=0.2, height=35, relwidth=0.2, bordermode='ignore')
Red_Entry.configure(background="white")
Red_Entry.configure(disabledforeground="#a3a3a3")
Red_Entry.configure(font="-family {Segoe UI} -size 14")
Red_Entry.configure(foreground="#000000")
Red_Entry.configure(insertbackground="black")
Red_Entry.configure(borderwidth="5")

Pasta_Entry = tk.Entry(Frame_middle)
Pasta_Entry.place(relx=0.7, rely=0.3, height=35, relwidth=0.2, bordermode='ignore')
Pasta_Entry.configure(background="white")
Pasta_Entry.configure(disabledforeground="#a3a3a3")
Pasta_Entry.configure(font="-family {Segoe UI} -size 14")
Pasta_Entry.configure(foreground="#000000")
Pasta_Entry.configure(insertbackground="black")
Pasta_Entry.configure(borderwidth="5")

lasagna_Entry = tk.Entry(Frame_middle)
lasagna_Entry.place(relx=0.7, rely=0.4, height=35, relwidth=0.2, bordermode='ignore')
lasagna_Entry.configure(background="white")
lasagna_Entry.configure(disabledforeground="#a3a3a3")
lasagna_Entry.configure(font="-family {Segoe UI} -size 14")
lasagna_Entry.configure(foreground="#000000")
lasagna_Entry.configure(insertbackground="black")
lasagna_Entry.configure(borderwidth="5")

Carnitas_Entry = tk.Entry(Frame_middle)
Carnitas_Entry.place(relx=0.7, rely=0.5, height=35, relwidth=0.2, bordermode='ignore')
Carnitas_Entry.configure(background="white")
Carnitas_Entry.configure(disabledforeground="#a3a3a3")
Carnitas_Entry.configure(font="-family {Segoe UI} -size 14")
Carnitas_Entry.configure(foreground="#000000")
Carnitas_Entry.configure(insertbackground="black")
Carnitas_Entry.configure(borderwidth="5")

Cheeseburger_Entry = tk.Entry(Frame_middle)
Cheeseburger_Entry.place(relx=0.7, rely=0.6, height=35, relwidth=0.2, bordermode='ignore')
Cheeseburger_Entry.configure(background="white")
Cheeseburger_Entry.configure(disabledforeground="#a3a3a3")
Cheeseburger_Entry.configure(font="-family {Segoe UI} -size 14")
Cheeseburger_Entry.configure(foreground="#000000")
Cheeseburger_Entry.configure(insertbackground="black")
Cheeseburger_Entry.configure(borderwidth="5")

Layered_Entry = tk.Entry(Frame_middle)
Layered_Entry.place(relx=0.7, rely=0.7, height=35, relwidth=0.2, bordermode='ignore')
Layered_Entry.configure(background="white")
Layered_Entry.configure(disabledforeground="#a3a3a3")
Layered_Entry.configure(font="-family {Segoe UI} -size 14")
Layered_Entry.configure(foreground="#000000")
Layered_Entry.configure(insertbackground="black")
Layered_Entry.configure(borderwidth="5")

choc_Entry = tk.Entry(Frame_middle)
choc_Entry.place(relx=0.7, rely=0.8, height=35, relwidth=0.2, bordermode='ignore')
choc_Entry.configure(background="white")
choc_Entry.configure(disabledforeground="#a3a3a3")
choc_Entry.configure(font="-family {Segoe UI} -size 14")
choc_Entry.configure(foreground="#000000")
choc_Entry.configure(insertbackground="black")
choc_Entry.configure(borderwidth="5")

Reuben_Entry = tk.Entry(Frame_middle)
Reuben_Entry.place(relx=0.7, rely=0.9, height=35, relwidth=0.2, bordermode='ignore')
Reuben_Entry.configure(background="white")
Reuben_Entry.configure(disabledforeground="#a3a3a3")
Reuben_Entry.configure(font="-family {Segoe UI} -size 14")
Reuben_Entry.configure(foreground="#000000")
Reuben_Entry.configure(insertbackground="black")
Reuben_Entry.configure(borderwidth="5")

Button_TOTAL = tk.Button()
Button_TOTAL.place(relx=0.699, rely=0.92, height=45, width=100)
Button_TOTAL.configure(activebackground="#ececec")
Button_TOTAL.configure(activeforeground="#000000")
Button_TOTAL.configure(background="#f2f2f2")
Button_TOTAL.configure(borderwidth="5")
Button_TOTAL.configure(disabledforeground="#a3a3a3")
Button_TOTAL.configure(font="-family {Segoe UI} -size 14")
Button_TOTAL.configure(foreground="#000000")
Button_TOTAL.configure(highlightbackground="#d9d9d9")
Button_TOTAL.configure(highlightcolor="black")
Button_TOTAL.configure(pady="0")
Button_TOTAL.configure(text='''TOTAL''')
Button_TOTAL.configure(command=m.total)

Button_RECEIPT = tk.Button()
Button_RECEIPT.place(relx=0.773, rely=0.92, height=45, width=100)
Button_RECEIPT.configure(activebackground="#ececec")
Button_RECEIPT.configure(activeforeground="#000000")
Button_RECEIPT.configure(background="#f2f2f2")
Button_RECEIPT.configure(borderwidth="5")
Button_RECEIPT.configure(disabledforeground="#a3a3a3")
Button_RECEIPT.configure(font="-family {Segoe UI} -size 14")
Button_RECEIPT.configure(foreground="#000000")
Button_RECEIPT.configure(highlightbackground="#d9d9d9")
Button_RECEIPT.configure(highlightcolor="black")
Button_RECEIPT.configure(pady="0")
Button_RECEIPT.configure(text='''RECEIPT''')
Button_RECEIPT.configure(command=m.recipt)

Button_RESET = tk.Button()
Button_RESET.place(relx=0.848, rely=0.92, height=45, width=100)
Button_RESET.configure(activebackground="#ececec")
Button_RESET.configure(activeforeground="#000000")
Button_RESET.configure(background="#f2f2f2")
Button_RESET.configure(borderwidth="5")
Button_RESET.configure(disabledforeground="#a3a3a3")
Button_RESET.configure(font="-family {Segoe UI} -size 14")
Button_RESET.configure(foreground="#000000")
Button_RESET.configure(highlightbackground="#d9d9d9")
Button_RESET.configure(highlightcolor="black")
Button_RESET.configure(pady="0")
Button_RESET.configure(text='''RESET''')
Button_RESET.configure(command=m.reset)

Button_EXIT = tk.Button()
Button_EXIT.place(relx=0.92, rely=0.92, height=45, width=100)
Button_EXIT.configure(activebackground="#ececec")
Button_EXIT.configure(activeforeground="#000000")
Button_EXIT.configure(background="#f2f2f2")
Button_EXIT.configure(borderwidth="5")
Button_EXIT.configure(disabledforeground="#a3a3a3")
Button_EXIT.configure(font="-family {Segoe UI} -size 14")
Button_EXIT.configure(foreground="#000000")
Button_EXIT.configure(highlightbackground="#d9d9d9")
Button_EXIT.configure(highlightcolor="black")
Button_EXIT.configure(pady="0")
Button_EXIT.configure(text='''EXIT''')
Button_EXIT.configure(command=m.exit_window)

Button_7 = tk.Button()
Button_7.place(relx=0.70, rely=0.17, height=45, width=100)
Button_7.configure(activebackground="#ececec")
Button_7.configure(activeforeground="#000000")
Button_7.configure(background="#f2f2f2")
Button_7.configure(borderwidth="5")
Button_7.configure(disabledforeground="#a3a3a3")
Button_7.configure(font="-family {Segoe UI} -size 18")
Button_7.configure(foreground="#000000")
Button_7.configure(highlightbackground="#d9d9d9")
Button_7.configure(highlightcolor="black")
Button_7.configure(pady="0")
Button_7.configure(text='''7''')
Button_7.configure(command=m.set_number7)

Button_8 = tk.Button()
Button_8.place(relx=0.774, rely=0.17, height=45, width=100)
Button_8.configure(activebackground="#ececec")
Button_8.configure(activeforeground="#000000")
Button_8.configure(background="#f2f2f2")
Button_8.configure(borderwidth="5")
Button_8.configure(disabledforeground="#a3a3a3")
Button_8.configure(font="-family {Segoe UI} -size 18")
Button_8.configure(foreground="#000000")
Button_8.configure(highlightbackground="#d9d9d9")
Button_8.configure(highlightcolor="black")
Button_8.configure(pady="0")
Button_8.configure(text='''8''')
Button_8.configure(command=m.set_number8)

Button_9 = tk.Button()
Button_9.place(relx=0.847, rely=0.17, height=45, width=100)
Button_9.configure(activebackground="#ececec")
Button_9.configure(activeforeground="#000000")
Button_9.configure(background="#f2f2f2")
Button_9.configure(borderwidth="5")
Button_9.configure(disabledforeground="#a3a3a3")
Button_9.configure(font="-family {Segoe UI} -size 18")
Button_9.configure(foreground="#000000")
Button_9.configure(highlightbackground="#d9d9d9")
Button_9.configure(highlightcolor="black")
Button_9.configure(pady="0")
Button_9.configure(text='''9''')
Button_9.configure(command=m.set_number9)

Button_plus = tk.Button()
Button_plus.place(relx=0.92, rely=0.17, height=45, width=100)
Button_plus.configure(activebackground="#ececec")
Button_plus.configure(activeforeground="#000000")
Button_plus.configure(background="#f2f2f2")
Button_plus.configure(borderwidth="5")
Button_plus.configure(disabledforeground="#a3a3a3")
Button_plus.configure(font="-family {Segoe UI} -size 18")
Button_plus.configure(foreground="#000000")
Button_plus.configure(highlightbackground="#d9d9d9")
Button_plus.configure(highlightcolor="black")
Button_plus.configure(pady="0")
Button_plus.configure(text='''+''')
Button_plus.configure(command=m.set_number_plus)

Button_4 = tk.Button()
Button_4.place(relx=0.70, rely=0.235, height=45, width=100)
Button_4.configure(activebackground="#ececec")
Button_4.configure(activeforeground="#000000")
Button_4.configure(background="#f2f2f2")
Button_4.configure(borderwidth="5")
Button_4.configure(disabledforeground="#a3a3a3")
Button_4.configure(font="-family {Segoe UI} -size 18")
Button_4.configure(foreground="#000000")
Button_4.configure(highlightbackground="#d9d9d9")
Button_4.configure(highlightcolor="black")
Button_4.configure(pady="0")
Button_4.configure(text='''4''')
Button_4.configure(command=m.set_number4)

Button_5 = tk.Button()
Button_5.place(relx=0.774, rely=0.235, height=45, width=100)
Button_5.configure(activebackground="#ececec")
Button_5.configure(activeforeground="#000000")
Button_5.configure(background="#f2f2f2")
Button_5.configure(borderwidth="5")
Button_5.configure(disabledforeground="#a3a3a3")
Button_5.configure(font="-family {Segoe UI} -size 18")
Button_5.configure(foreground="#000000")
Button_5.configure(highlightbackground="#d9d9d9")
Button_5.configure(highlightcolor="black")
Button_5.configure(pady="0")
Button_5.configure(text='''5''')
Button_5.configure(command=m.set_number5)

Button_6 = tk.Button()
Button_6.place(relx=0.847, rely=0.235, height=45, width=100)
Button_6.configure(activebackground="#ececec")
Button_6.configure(activeforeground="#000000")
Button_6.configure(background="#f2f2f2")
Button_6.configure(borderwidth="5")
Button_6.configure(disabledforeground="#a3a3a3")
Button_6.configure(font="-family {Segoe UI} -size 18")
Button_6.configure(foreground="#000000")
Button_6.configure(highlightbackground="#d9d9d9")
Button_6.configure(highlightcolor="black")
Button_6.configure(pady="0")
Button_6.configure(text='''6''')
Button_6.configure(command=m.set_number6)

Button_minus = tk.Button()
Button_minus.place(relx=0.92, rely=0.235, height=45, width=100)
Button_minus.configure(activebackground="#ececec")
Button_minus.configure(activeforeground="#000000")
Button_minus.configure(background="#f2f2f2")
Button_minus.configure(borderwidth="5")
Button_minus.configure(disabledforeground="#a3a3a3")
Button_minus.configure(font="-family {Segoe UI} -size 18")
Button_minus.configure(foreground="#000000")
Button_minus.configure(highlightbackground="#d9d9d9")
Button_minus.configure(highlightcolor="black")
Button_minus.configure(pady="0")
Button_minus.configure(text='''-''')
Button_minus.configure(command=m.set_number_minus)

Button_1 = tk.Button()
Button_1.place(relx=0.70, rely=0.3, height=45, width=100)
Button_1.configure(activebackground="#ececec")
Button_1.configure(activeforeground="#000000")
Button_1.configure(background="#f2f2f2")
Button_1.configure(borderwidth="5")
Button_1.configure(disabledforeground="#a3a3a3")
Button_1.configure(font="-family {Segoe UI} -size 18")
Button_1.configure(foreground="#000000")
Button_1.configure(highlightbackground="#d9d9d9")
Button_1.configure(highlightcolor="black")
Button_1.configure(pady="0")
Button_1.configure(text='''1''')
Button_1.configure(command=m.set_number1)

Button_2 = tk.Button()
Button_2.place(relx=0.774, rely=0.3, height=45, width=100)
Button_2.configure(activebackground="#ececec")
Button_2.configure(activeforeground="#000000")
Button_2.configure(background="#f2f2f2")
Button_2.configure(borderwidth="5")
Button_2.configure(disabledforeground="#a3a3a3")
Button_2.configure(font="-family {Segoe UI} -size 18")
Button_2.configure(foreground="#000000")
Button_2.configure(highlightbackground="#d9d9d9")
Button_2.configure(highlightcolor="black")
Button_2.configure(pady="0")
Button_2.configure(text='''2''')
Button_2.configure(command=m.set_number2)

Button_3 = tk.Button()
Button_3.place(relx=0.847, rely=0.3, height=45, width=100)
Button_3.configure(activebackground="#ececec")
Button_3.configure(activeforeground="#000000")
Button_3.configure(background="#f2f2f2")
Button_3.configure(borderwidth="5")
Button_3.configure(disabledforeground="#a3a3a3")
Button_3.configure(font="-family {Segoe UI} -size 18")
Button_3.configure(foreground="#000000")
Button_3.configure(highlightbackground="#d9d9d9")
Button_3.configure(highlightcolor="black")
Button_3.configure(pady="0")
Button_3.configure(text='''3''')
Button_3.configure(command=m.set_number3)

Button_multi = tk.Button()
Button_multi.place(relx=0.92, rely=0.3, height=45, width=100)
Button_multi.configure(activebackground="#ececec")
Button_multi.configure(activeforeground="#000000")
Button_multi.configure(background="#f2f2f2")
Button_multi.configure(borderwidth="5")
Button_multi.configure(disabledforeground="#a3a3a3")
Button_multi.configure(font="-family {Segoe UI} -size 18")
Button_multi.configure(foreground="#000000")
Button_multi.configure(highlightbackground="#d9d9d9")
Button_multi.configure(highlightcolor="black")
Button_multi.configure(pady="0")
Button_multi.configure(text='''x''')
Button_multi.configure(command=m.set_number_sub)

Button_0 = tk.Button()
Button_0.place(relx=0.70, rely=0.368, height=45, width=100)
Button_0.configure(activebackground="#ececec")
Button_0.configure(activeforeground="#000000")
Button_0.configure(background="#f2f2f2")
Button_0.configure(borderwidth="5")
Button_0.configure(disabledforeground="#a3a3a3")
Button_0.configure(font="-family {Segoe UI} -size 18")
Button_0.configure(foreground="#000000")
Button_0.configure(highlightbackground="#d9d9d9")
Button_0.configure(highlightcolor="black")
Button_0.configure(pady="0")
Button_0.configure(text='''0''')
Button_0.configure(command=m.set_number0)

Button_dot = tk.Button()
Button_dot.place(relx=0.774, rely=0.368, height=45, width=100)
Button_dot.configure(activebackground="#ececec")
Button_dot.configure(activeforeground="#000000")
Button_dot.configure(background="#f2f2f2")
Button_dot.configure(borderwidth="5")
Button_dot.configure(disabledforeground="#a3a3a3")
Button_dot.configure(font="-family {Segoe UI} -size 18")
Button_dot.configure(foreground="#000000")
Button_dot.configure(highlightbackground="#d9d9d9")
Button_dot.configure(highlightcolor="black")
Button_dot.configure(pady="0")
Button_dot.configure(text='''.''')
Button_dot.configure(command=m.set_number_dot)

Button_equal = tk.Button()
Button_equal.place(relx=0.847, rely=0.368, height=45, width=100)
Button_equal.configure(activebackground="#ececec")
Button_equal.configure(activeforeground="#000000")
Button_equal.configure(background="#f2f2f2")
Button_equal.configure(borderwidth="5")
Button_equal.configure(disabledforeground="#a3a3a3")
Button_equal.configure(font="-family {Segoe UI} -size 18")
Button_equal.configure(foreground="#000000")
Button_equal.configure(highlightbackground="#d9d9d9")
Button_equal.configure(highlightcolor="black")
Button_equal.configure(pady="0")
Button_equal.configure(text='''=''')
Button_equal.configure(command=m.equal)

Button_div = tk.Button()
Button_div.place(relx=0.92, rely=0.368, height=45, width=100)
Button_div.configure(activebackground="#ececec")
Button_div.configure(activeforeground="#000000")
Button_div.configure(background="#f2f2f2")
Button_div.configure(borderwidth="5")
Button_div.configure(disabledforeground="#a3a3a3")
Button_div.configure(font="-family {Segoe UI} -size 18")
Button_div.configure(foreground="#000000")
Button_div.configure(highlightbackground="#d9d9d9")
Button_div.configure(highlightcolor="black")
Button_div.configure(pady="0")
Button_div.configure(text='''/''')
Button_div.configure(command=m.set_number_div)

Button_c = tk.Button()
Button_c.place(relx=0.92, rely=0.105, height=45, width=100)
Button_c.configure(activebackground="#ececec")
Button_c.configure(activeforeground="#000000")
Button_c.configure(background="#f2f2f2")
Button_c.configure(borderwidth="5")
Button_c.configure(disabledforeground="#a3a3a3")
Button_c.configure(font="-family {Segoe UI} -size 18")
Button_c.configure(foreground="#000000")
Button_c.configure(highlightbackground="#d9d9d9")
Button_c.configure(highlightcolor="black")
Button_c.configure(pady="0")
Button_c.configure(text='''C''')
Button_c.configure(command=m.clear)

cost_of_drinks = tk.Label(Frame_bottom)
cost_of_drinks.place(relx=0.01, rely=0.1, height=25, width=200, bordermode='ignore')
cost_of_drinks.configure(background="#c1c2c9")
cost_of_drinks.configure(disabledforeground="#a3a3a3")
cost_of_drinks.configure(font="-family {aril black} -size 15")
cost_of_drinks.configure(foreground="#000000")
cost_of_drinks.configure(text='''Cost of Drinks''')

cost_of_cakes = tk.Label(Frame_bottom)
cost_of_cakes.place(relx=0.01, rely=0.35, height=25, width=200, bordermode='ignore')
cost_of_cakes.configure(background="#c1c2c9")
cost_of_cakes.configure(disabledforeground="#a3a3a3")
cost_of_cakes.configure(font="-family {aril black} -size 15")
cost_of_cakes.configure(foreground="#000000")
cost_of_cakes.configure(text='''Cost of Food Items''')

Service_Charge = tk.Label(Frame_bottom)
Service_Charge.place(relx=0.01, rely=0.6, height=25, width=200, bordermode='ignore')
Service_Charge.configure(background="#c1c2c9")
Service_Charge.configure(disabledforeground="#a3a3a3")
Service_Charge.configure(font="-family {aril black} -size 15")
Service_Charge.configure(foreground="#000000")
Service_Charge.configure(text='''  Service Charge''')

Cash = tk.Label(Frame_bottom)
Cash.place(relx=0.01, rely=0.82, height=25, width=200, bordermode='ignore')
Cash.configure(background="#c1c2c9")
Cash.configure(disabledforeground="#a3a3a3")
Cash.configure(font="-family {aril black} -size 15")
Cash.configure(foreground="#000000")
Cash.configure(text='''Cash             ''')

Paid_Tax = tk.Label(Frame_bottom)
Paid_Tax.place(relx=0.5, rely=0.1, height=25, width=200, bordermode='ignore')
Paid_Tax.configure(background="#c1c2c9")
Paid_Tax.configure(disabledforeground="#a3a3a3")
Paid_Tax.configure(font="-family {aril black} -size 15")
Paid_Tax.configure(foreground="#000000")
Paid_Tax.configure(text='''Paid Tax''')

Sub_Total = tk.Label(Frame_bottom)
Sub_Total.place(relx=0.5, rely=0.35, height=25, width=200, bordermode='ignore')
Sub_Total.configure(background="#c1c2c9")
Sub_Total.configure(disabledforeground="#a3a3a3")
Sub_Total.configure(font="-family {aril black} -size 15")
Sub_Total.configure(foreground="#000000")
Sub_Total.configure(text=''' Sub Total''')

Total_Cost = tk.Label(Frame_bottom)
Total_Cost.place(relx=0.5, rely=0.6, height=25, width=200, bordermode='ignore')
Total_Cost.configure(background="#c1c2c9")
Total_Cost.configure(disabledforeground="#a3a3a3")
Total_Cost.configure(font="-family {aril black} -size 15")
Total_Cost.configure(foreground="#000000")
Total_Cost.configure(text='''  Total Cost''')

Remain = tk.Label(Frame_bottom)
Remain.place(relx=0.5, rely=0.82, height=25, width=200, bordermode='ignore')
Remain.configure(background="#c1c2c9")
Remain.configure(disabledforeground="#a3a3a3")
Remain.configure(font="-family {aril black} -size 15")
Remain.configure(foreground="#000000")
Remain.configure(text='''Remain  ''')

Label_Drinks = tk.Label(Frame_left)
Label_Drinks.place(relx=0.004, rely=0.0, relheight=0.08, width=130)
Label_Drinks.configure(background="#d9d9d9")
Label_Drinks.configure(borderwidth="4")
Label_Drinks.configure(disabledforeground="#a3a3a3")
Label_Drinks.configure(font="-family {aril black} -size 17 -weight bold")
Label_Drinks.configure(foreground="black")
Label_Drinks.configure(text='''Drinks''')

Label_Cakes = tk.Label(Frame_middle)
Label_Cakes.place(relx=0, rely=0.0, relheight=0.08, width=130)
Label_Cakes.configure(background="#d9d9d9")
Label_Cakes.configure(borderwidth="4")
Label_Cakes.configure(disabledforeground="#a3a3a3")
Label_Cakes.configure(font="-family {aril black} -size 17 -weight bold")
Label_Cakes.configure(foreground="black")
Label_Cakes.configure(text='''Items''')

Checkbutton_Latte = tk.Checkbutton(Frame_left)
Checkbutton_Latte.configure(text="Latte")
Checkbutton_Latte.configure(variable=var1)
Checkbutton_Latte.place(relx=0.1, rely=0.1, height=35, bordermode='ignore')
Checkbutton_Latte.configure(font="-family {Segoe UI} -size 14")
Checkbutton_Latte.configure(background="#d9d9d9")
Checkbutton_Latte.configure(command=m.Latte)

Espresso_Checkbutton = tk.Checkbutton(Frame_left)
Espresso_Checkbutton.configure(text="Espresso")
Espresso_Checkbutton.configure(variable= var2)
Espresso_Checkbutton.place(relx=0.1, rely=0.2, height=35, bordermode='ignore')
Espresso_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Espresso_Checkbutton.configure(background="#d9d9d9")
Espresso_Checkbutton.configure(command=m.Espresso)

Iced_latte_Checkbutton = tk.Checkbutton(Frame_left)
Iced_latte_Checkbutton.configure(text="Iced Latte")
Iced_latte_Checkbutton.configure(variable= var3)
Iced_latte_Checkbutton.place(relx=0.1, rely=0.3, height=35, bordermode='ignore')
Iced_latte_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Iced_latte_Checkbutton.configure(background="#d9d9d9")
Iced_latte_Checkbutton.configure(command=m.Iced_latte)

SexOn_Checkbutton = tk.Checkbutton(Frame_left)
SexOn_Checkbutton.configure(text="Coffee")
SexOn_Checkbutton.configure(variable= var4)
SexOn_Checkbutton.place(relx=0.1, rely=0.4, height=35, bordermode='ignore')
SexOn_Checkbutton.configure(font="-family {Segoe UI} -size 14")
SexOn_Checkbutton.configure(background="#d9d9d9")
SexOn_Checkbutton.configure(command=m.SexOn)

Cappucino_Checkbutton = tk.Checkbutton(Frame_left)
Cappucino_Checkbutton.configure(text="Cappuccino")
Cappucino_Checkbutton.configure(variable= var5)
Cappucino_Checkbutton.place(relx=0.1, rely=0.5, height=35, bordermode='ignore')
Cappucino_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Cappucino_Checkbutton.configure(background="#d9d9d9")
Cappucino_Checkbutton.configure(command=m.Cappucino)

Frappé_Checkbutton = tk.Checkbutton(Frame_left)
Frappé_Checkbutton.configure(text="Frappe")
Frappé_Checkbutton.configure(variable= var6)
Frappé_Checkbutton.place(relx=0.1, rely=0.6, height=35, bordermode='ignore')
Frappé_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Frappé_Checkbutton.configure(background="#d9d9d9")
Frappé_Checkbutton.configure(command=m.Frappé)

Doppio_Checkbutton = tk.Checkbutton(Frame_left)
Doppio_Checkbutton.configure(text="Doppio")
Doppio_Checkbutton.configure(variable= var7)
Doppio_Checkbutton.place(relx=0.1, rely=0.7, height=35, bordermode='ignore')
Doppio_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Doppio_Checkbutton.configure(background="#d9d9d9")
Doppio_Checkbutton.configure(command=m.Doppio)

Iced_cap_Checkbutton = tk.Checkbutton(Frame_left)
Iced_cap_Checkbutton.configure(text="Iced Cappuccino")
Iced_cap_Checkbutton.configure(variable= var8)
Iced_cap_Checkbutton.place(relx=0.1, rely=0.8, height=35, bordermode='ignore')
Iced_cap_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Iced_cap_Checkbutton.configure(background="#d9d9d9")
Iced_cap_Checkbutton.configure(command=m.Iced_cap)

Mojito_Checkbutton = tk.Checkbutton(Frame_left)
Mojito_Checkbutton.configure(text="Mojito")
Mojito_Checkbutton.configure(variable= var9)
Mojito_Checkbutton.place(relx=0.1, rely=0.9, height=35, bordermode='ignore')
Mojito_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Mojito_Checkbutton.configure(background="#d9d9d9")
Mojito_Checkbutton.configure(command=m.Mojito)

Cheese_Checkbutton = tk.Checkbutton(Frame_middle)
Cheese_Checkbutton.configure(text="Cheese Cake")
Cheese_Checkbutton.configure(variable= var10)
Cheese_Checkbutton.place(relx=0.1, rely=0.1, height=35, bordermode='ignore')
Cheese_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Cheese_Checkbutton.configure(background="#d9d9d9")
Cheese_Checkbutton.configure(command=m.Cheese)

Red_Checkbutton = tk.Checkbutton(Frame_middle)
Red_Checkbutton.configure(text="Red Velvet Cake")
Red_Checkbutton.configure(variable= var11)
Red_Checkbutton.place(relx=0.1, rely=0.2, height=35, bordermode='ignore')
Red_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Red_Checkbutton.configure(background="#d9d9d9")
Red_Checkbutton.configure(command=m.Red)

Pasta_Checkbutton = tk.Checkbutton(Frame_middle)
Pasta_Checkbutton.configure(text="Pasta Puttanesca")
Pasta_Checkbutton.configure(variable= var12)
Pasta_Checkbutton.place(relx=0.1, rely=0.3, height=35, bordermode='ignore')
Pasta_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Pasta_Checkbutton.configure(background="#d9d9d9")
Pasta_Checkbutton.configure(command=m.Pasta)

lasagna_Checkbutton = tk.Checkbutton(Frame_middle)
lasagna_Checkbutton.configure(text="Lasagna Bolognese")
lasagna_Checkbutton.configure(variable= var13)
lasagna_Checkbutton.place(relx=0.1, rely=0.4, height=35, bordermode='ignore')
lasagna_Checkbutton.configure(font="-family {Segoe UI} -size 14")
lasagna_Checkbutton.configure(background="#d9d9d9")
lasagna_Checkbutton.configure(command=m.lasagna)

Carnitas_Checkbutton = tk.Checkbutton(Frame_middle)
Carnitas_Checkbutton.configure(text="Carnitas Burrito")
Carnitas_Checkbutton.configure(variable= var14)
Carnitas_Checkbutton.place(relx=0.1, rely=0.5, height=35, bordermode='ignore')
Carnitas_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Carnitas_Checkbutton.configure(background="#d9d9d9")
Carnitas_Checkbutton.configure(command=m.Carnitas)

Cheeseburger_Checkbutton = tk.Checkbutton(Frame_middle)
Cheeseburger_Checkbutton.configure(text="Cheeseburger")
Cheeseburger_Checkbutton.configure(variable= var15)
Cheeseburger_Checkbutton.place(relx=0.1, rely=0.6, height=35, bordermode='ignore')
Cheeseburger_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Cheeseburger_Checkbutton.configure(background="#d9d9d9")
Cheeseburger_Checkbutton.configure(command=m.Cheeseburger)

Layered_Checkbutton = tk.Checkbutton(Frame_middle)
Layered_Checkbutton.configure(text="Layered Rainbow Cake")
Layered_Checkbutton.configure(variable= var16)
Layered_Checkbutton.place(relx=0.1, rely=0.7, height=35, bordermode='ignore')
Layered_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Layered_Checkbutton.configure(background="#d9d9d9")
Layered_Checkbutton.configure(command=m.Layered)

choc_Checkbutton = tk.Checkbutton(Frame_middle)
choc_Checkbutton.configure(text="Choc-Honeycomb Cake")
choc_Checkbutton.configure(variable= var17)
choc_Checkbutton.place(relx=0.1, rely=0.8, height=35, bordermode='ignore')
choc_Checkbutton.configure(font="-family {Segoe UI} -size 14")
choc_Checkbutton.configure(background="#d9d9d9")
choc_Checkbutton.configure(command=m.choc)

Reuben_Checkbutton = tk.Checkbutton(Frame_middle)
Reuben_Checkbutton.configure(text="Reuben sandwich")
Reuben_Checkbutton.configure(variable= var18)
Reuben_Checkbutton.place(relx=0.1, rely=0.9, height=35, bordermode='ignore')
Reuben_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Reuben_Checkbutton.configure(background="#d9d9d9")
Reuben_Checkbutton.configure(command=m.Reuben)
