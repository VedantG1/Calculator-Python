from tkinter import *

root = Tk()
root.title("Stupid Calculator")
root.resizable(False, False)
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# entry.insert(0, "")
def button_click(number):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if(math == "addition"):
        entry.insert(0, f_num + float(second_number))
    elif(math == "subtraction"):
        entry.insert(0, f_num - float(second_number))
    elif(math == "multiply"):
        entry.insert(0, f_num * float(second_number))
    elif(math == "divide"):
        entry.insert(0, f_num / float(second_number))


def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float((first_number))
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    entry.delete(0, END)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonAdd = Button(root, text="+", padx=40, pady=20, command=button_add)
buttonEqual = Button(root, text="=", padx=88, pady=20, command=button_equal)
buttonClear = Button(root, text="C", padx=40, pady=20, command=button_clear)
buttonSubtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=button_divide)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button0.grid(row=5, column=2, columnspan=2)
buttonClear.grid(row=6, column=2)

buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=7, column=0, columnspan=2)

buttonSubtract.grid(row=5, column=1)
buttonMultiply.grid(row=6, column=0)
buttonDivide.grid(row=6, column=1)

myButton = Button(root, text="Submit", bg="green", fg="yellow")

root.mainloop()
