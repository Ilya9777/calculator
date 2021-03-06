import tkinter as tk

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)

def add_operation (operation):
    value = calc.get()
    if value[-1]in '-+/*':
        value=value[:-1]
    elif '+'in value or '-'in value or '*'in value or '/'in value :
        calculate()
        value=calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)

def add_comma (comma):
    value = calc.get()
    if value[-1]in '.':
        value=value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value+comma)

def calculate ():
    value = calc.get()
    if value[-1] in '-+/*':
        value= value +value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0, eval(value))

def clear():
    calc.delete(0,tk.END)
    calc.insert(0,"0")

def backspace() :
    value = calc.get()
    if len(value)==1 or value[0] == '0':
        calc.delete(0,tk.END)
        calc.insert(0,"0")
    else:
        calc.delete(0,tk.END)
        calc.insert(0,value[:-1])
    


def sqrt():
    sqrt='**0.5'
    

def make_digit_button(digit):
    return tk.Button(text=digit,bd=5,font= ('Arial',13),command=lambda :add_digit(digit))

def make_comma_button(comma):
    return tk.Button(text=comma,bd=5,font= ('Arial',13), command=lambda :add_comma(comma))

def make_operation_button(operation):
    return tk.Button(text=operation,bd=5,font= ('Arial',13),fg='red', command=lambda :add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation,bd=5,font= ('Arial',13),fg='red', command=calculate)
def make_clear_button(operation):
    return tk.Button(text=operation,bd=5,font= ('Arial',13),fg='red', command=clear)

def add_sign_button():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0,value)

def make_sign_button(operation):
    return tk.Button(text=operation,bd=5,font= ('Arial',13),fg='red', command=lambda :add_sign_button())

def make_del_button(operation):
    return tk.Button(text=operation,bd=5,font= ('Arial',13),fg='red', command=backspace)

def press_key(event):
    #print (event)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '-+*/':
        add_operation(event.char)
    elif event.char in '.':
        add_comma(event.char)
    elif event.char in '=' or event.char in '\r':
        calculate()
    

win =tk.Tk()
win['bg'] = '#33ffe6'
win.title('??????????????????????')
win.geometry(f"300x340+100+200")
win.bind('<Key>',press_key)

calc = tk.Entry(win,justify=tk.RIGHT, font=('Arial',15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0, columnspan=5, stick='we',padx=5)

make_digit_button('1').grid(row=1,column=1,stick='wens',padx=5,pady=5)
make_digit_button('2').grid(row=1,column=2,stick='wens',padx=5,pady=5)
make_digit_button('3').grid(row=1,column=3,stick='wens',padx=5,pady=5)
make_digit_button('4').grid(row=2,column=1,stick='wens',padx=5,pady=5)
make_digit_button('5').grid(row=2,column=2,stick='wens',padx=5,pady=5)
make_digit_button('6').grid(row=2,column=3,stick='wens',padx=5,pady=5)
make_digit_button('7').grid(row=3,column=1,stick='wens',padx=5,pady=5)
make_digit_button('8').grid(row=3,column=2,stick='wens',padx=5,pady=5)
make_digit_button('9').grid(row=3,column=3,stick='wens',padx=5,pady=5)
make_digit_button('0').grid(row=4,column=1,stick='wens',padx=5,pady=5)
make_comma_button('.').grid(row=4,column=2,stick='wens',padx=5,pady=5)
make_operation_button('+').grid(row=2,column=4,stick='wens',padx=5,pady=5)
make_operation_button('-').grid(row=3,column=4,stick='wens',padx=5,pady=5)
make_operation_button('*').grid(row=4,column=4,stick='wens',padx=5,pady=5)
make_operation_button('/').grid(row=5,column=4,stick='wens',padx=5,pady=5)
make_operation_button('**').grid(row=2,column=0,stick='wens',padx=5,pady=5)
make_operation_button('V').grid(row=3,column=0,stick='wens',padx=5,pady=5)

make_sign_button('+/-').grid(row=4,column=0,stick='wens',padx=5,pady=5)

make_calc_button('=').grid(row=4,column=3,stick='wens',padx=5,pady=5)
make_clear_button('C').grid(row=1,column=4,stick='wens',padx=5,pady=5)

make_del_button('del').grid(row=1,column=0,stick='wens',padx=5,pady=5)




win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)
win.grid_columnconfigure(4,minsize=60)


win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)


win.mainloop()