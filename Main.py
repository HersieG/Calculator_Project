from tkinter import *

equation_line = ""
def equation(string):
    global equation_line
    current_str = string
    screen_Label.set("")
    if string != "=":
        equation_line += current_str
        screen_Label.set(equation_line)
    else:
        return calculate(equation_line)
def clear():
    global equation_line
    equation_line = ""
    screen_Label.set(equation_line)

def calculate(string):
    global equation_line
    try:
        answer = eval(string)
        screen_Label.set(answer)
        equation_line = ""
    except ZeroDivisionError as e:
        s = str(e) + " Try again!"
        screen_Label.set(s)
        equation_line = ""
    except SyntaxError:
        screen_Label.set("That is not an equation, try again!")
        equation_line = ""
    finally:
        pass



window = Tk()
window.resizable(height=False, width=False)

screen_Label = StringVar()

label = Label(window, textvariable= screen_Label, font= ('Consolas', 20), bg="white", width=45, height=6)
label.pack()

frame = Frame(window)
frame.pack()


button1 = Button(frame,
                 text="1",
                 height=5,
                 width=5,
                 command= lambda: equation("1"),
                 font=("Comic Sans", 10))
button1.grid(row=2, column=0)

button2 = Button(frame,
                 text="2",
                 height=5,
                 width=5,
                 command= lambda: equation("2"),
                 font=("Comic Sans", 10))

button2.grid(row=2, column=1)
button3 = Button(frame,
                 text="3",
                 height=5,
                 width=5,
                 command= lambda: equation("3"),
                 font=("Comic Sans", 10))
button3.grid(row=2, column=2)

button4 = Button(frame,
                 text="4",
                 height=5,
                 width=5,
                 command= lambda: equation("4"),
                 font=("Comic Sans", 10))
button4.grid(row=1, column=0)

button5 = Button(frame,
                 text="5",
                 height=5,
                 width=5,
                 command= lambda: equation("5"),
                 font=("Comic Sans", 10))
button5.grid(row=1, column=1)

button6 = Button(frame,
                 text="6",
                 height=5,
                 width=5,
                 command= lambda: equation("6"),
                 font=("Comic Sans", 10))
button6.grid(row=1, column=2)

button7 = Button(frame,
                 text="7",
                 height=5,
                 width=5,
                 command= lambda: equation("7"),
                 font=("Comic Sans", 10))

button7.grid(row=0, column=0)

button8 = Button(frame,
                 text="8",
                 height=5,
                 width=5,
                 command= lambda: equation("8"),
                 font=("Comic Sans", 10))
button8.grid(row=0, column=1)

button9 = Button(frame,
                 text="9",
                 height=5,
                 width=5,
                 command= lambda: equation("9"),
                 font=("Comic Sans", 10))
button9.grid(row=0, column=2)

button0 = Button(frame,
                 text="0",
                 height=5,
                 width=5,
                 command= lambda: equation("0"),
                 font=("Comic Sans", 10))
button0.grid(row=3, column=0)

button_Decimal = Button(frame,
                 text=".",
                 height=5,
                 width=5,
                 command= lambda: equation("."),
                 font=("Comic Sans", 10))
button_Decimal.grid(row=3, column=1)

button_equals = Button(frame,
                 text="=",
                 height=5,
                 width=5,
                 command= lambda: equation("="),
                 font=("Comic Sans", 10))
button_equals.grid(row=3, column=2)

button_division = Button(frame,
                 text="/",
                 height=5,
                 width=5,
                 command= lambda: equation("/"),
                 font=("Comic Sans", 10))
button_division.grid(row=0, column=3)

button_muliplication = Button(frame,
                 text="*",
                 height=5,
                 width=5,
                 command= lambda: equation("*"),
                 font=("Comic Sans", 10))
button_muliplication.grid(row=1, column=3)

button_minus = Button(frame,
                 text="-",
                 height=5,
                 width=5,
                 command= lambda: equation("-"),
                 font=("Comic Sans", 10))
button_minus.grid(row=2, column=3)

button_addition = Button(frame,
                 text="+",
                 height=5,
                 width=5,
                 command= lambda: equation("+"),
                 font=("Comic Sans", 10))
button_addition.grid(row=3, column=3)

button_clear = Button(frame,
                 text="clear",
                 height=5,
                 width=5,
                 command= lambda: clear(),
                 font=("Comic Sans", 10))
button_clear.grid(row=4, column=0)





frame.pack()
window.mainloop()