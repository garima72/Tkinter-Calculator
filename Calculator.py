import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

e = tk.Entry(window, width=45, borderwidth=5)
e.place(x=10, y=10)


n1 = None
math = ""


def click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, tk.END)

def add():
    global n1
    global math
    first_number = e.get()
    math = "addition"
    n1 = int(first_number)
    e.delete(0, tk.END)

def sub():
    global n1
    global math
    first_number = e.get()
    math = "subtraction"
    n1 = int(first_number)
    e.delete(0, tk.END)

def mult():
    global n1
    global math
    first_number = e.get()
    math = "multiplication"
    n1 = int(first_number)
    e.delete(0, tk.END)

def div():
    global n1
    global math
    first_number = e.get()
    math = "division"
    n1 = int(first_number)
    e.delete(0, tk.END)

# --- Function for equal ---
def equal():
    second_number = e.get()
    e.delete(0, tk.END)
    
    if math == "addition":
        e.insert(0, n1 + int(second_number))
    elif math == "subtraction":
        e.insert(0, n1 - int(second_number))
    elif math == "multiplication":
        e.insert(0, n1 * int(second_number))
    elif math == "division":
        if int(second_number) != 0:
            e.insert(0, n1 / int(second_number))
        else:
            e.insert(0, "Error")

#BUTTONS

# Row 1: 1, 2, 3
b1 = tk.Button(window, text='1', width=12, command=lambda: click(1))
b1.place(x=10, y=60)
b2 = tk.Button(window, text='2', width=12, command=lambda: click(2))
b2.place(x=110, y=60)
b3 = tk.Button(window, text='3', width=12, command=lambda: click(3))
b3.place(x=210, y=60)

# Row 2: 4, 5, 6
b4 = tk.Button(window, text='4', width=12, command=lambda: click(4))
b4.place(x=10, y=110)
b5 = tk.Button(window, text='5', width=12, command=lambda: click(5))
b5.place(x=110, y=110)
b6 = tk.Button(window, text='6', width=12, command=lambda: click(6))
b6.place(x=210, y=110)

# Row 3: 7, 8, 9
b7 = tk.Button(window, text='7', width=12, command=lambda: click(7))
b7.place(x=10, y=160)
b8 = tk.Button(window, text='8', width=12, command=lambda: click(8))
b8.place(x=110, y=160)
b9 = tk.Button(window, text='9', width=12, command=lambda: click(9))
b9.place(x=210, y=160)

# Row 4: 0, +, -
b0 = tk.Button(window, text='0', width=12, command=lambda: click(0))
b0.place(x=10, y=210)
b_add = tk.Button(window, text='+', width=12, command=add)
b_add.place(x=110, y=210)
b_sub = tk.Button(window, text='-', width=12, command=sub)
b_sub.place(x=210, y=210)

# Row 5: *, /, =
b_mult = tk.Button(window, text='*', width=12, command=mult)
b_mult.place(x=10, y=260)
b_div = tk.Button(window, text='/', width=12, command=div)
b_div.place(x=110, y=260)
b_equal = tk.Button(window, text='=', width=12, command=equal)
b_equal.place(x=210, y=260)

# Row 6: clear
b_clear = tk.Button(window, text='clear', width=12, command=clear)
b_clear.place(x=10, y=310)



window.mainloop()