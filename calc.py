import tkinter as tk
from tkinter import Frame
from math import *

DEFAULT_FONT = ('Arial',20,'bold')
window = tk.Tk()

operators = ('+','-','/','*','\u00D7','%','**')

operatorIsPressed = False
specialIsPressed = False
current_text = '0'
total_text = ''


def button_pressed(num):
    global current_text
    global operatorIsPressed , specialIsPressed
    global total_text

    if not total_text or (total_text and total_text[-1] != '='):

        if current_text == '0' and not operatorIsPressed and not specialIsPressed:
            current_text = str(num)
            current_label.set(current_text)
        elif total_text and total_text[-1] in operators and operatorIsPressed:
            current_text = str(num)
            current_label.set(current_text)
            operatorIsPressed = False
        elif total_text and (total_text[-1] == ')' or total_text[-1] == ',') and specialIsPressed:
            current_text = str(num)
            current_label.set(current_text)
            specialIsPressed = False
        else:
            current_text += str(num)
            current_label.set(current_text)

    else:
        current_text = str(num)
        current_label.set(current_text)
        total_text = ''
        total_label.set(total_text)

def dot_button():
    global current_text
    global operatorIsPressed

    if current_text.find('.') == -1:
        current_text += str('.')
    current_label.set(current_text)

    operatorIsPressed = False

def clear_button():
    global current_text
    global total_text
    global operatorIsPressed, specialIsPressed

    current_text = "0"
    total_text = ""
    current_label.set(current_text)
    total_label.set(total_text)

    operatorIsPressed = False
    specialIsPressed = False

def operator_button(n):
    global current_text
    global total_text
    global operatorIsPressed

    if (total_text and total_text[-1] != '=') or not total_text:
        if (total_text and (total_text[-1] not in operators) and total_text.find('=') == -1) or total_text == '' or operatorIsPressed == False:
            if current_text[-1] == '.':
                current_text = current_text[:-1]

            if total_text and total_text[-1] == ')':
                total_text = total_text + str(n)
            elif total_text and total_text[-1] == ',':
                total_text = total_text + current_text + ')' + str(n)
            else:
                total_text = total_text + current_text + str(n)

            current_label.set(current_text)
            total_label.set(total_text)

            operatorIsPressed = True
        elif total_text and (total_text[-1] in operators):
            if total_text.find('**') != -1:
                total_text = total_text[:-2] + str(n)
                total_label.set(total_text)
            else:

                total_text = total_text[:-1] + str(n)
                total_label.set(total_text)

            operatorIsPressed = True


def log_identify(x, y=None):
    if y is None:
        return log10(x)
    else:
        return log(x, y)


def equal():
    global current_text
    global total_text
    global operatorIsPressed

    if total_text and total_text[-1] != '=':
        if total_text and total_text[-1] == ')':
            total_text = total_text + '='
        elif total_text and total_text[-1] == ',':
            total_text = total_text + current_text + ')' + '='
        else:
            total_text = total_text + current_text + '='

        total_label.set(total_text)

        result = str(eval(total_text[:-1],{"sqrt": sqrt,"sqr": square,"fact": factorial,"floor": floor,"ceil": ceil,"log": log_identify}))

        if result[-2:] == '.0':
            result = result[:-2]

        current_text = str(result)
        current_label.set(current_text)

        operatorIsPressed = True


def del_button():
    global current_text

    if len(current_text) > 1:
        current_text = current_text[:-1]
    else:
        current_text = '0'

    current_label.set(current_text)

def negate():
    global current_text

    if current_text.find('-') == -1 and current_text != '0':
        current_text = '-' + current_text
    else:
        current_text = current_text.replace('-','')

    current_label.set(current_text)

def special_operator(n):
    global current_text
    global total_text
    global operatorIsPressed , specialIsPressed

    if (total_text and total_text[-1] != '=') or total_text == '':
        if total_text and total_text[-1] == ')':
            total_text += '+'

        total_text += str(n)
        total_label.set(total_text)

        specialIsPressed = True



def square(x):
    return x ** 2


window.geometry("455x667")
window.title("Calculator")
window.resizable(False,False)
window.iconbitmap("Windows_Calculator_icon.ico")

total_label = tk.StringVar()
current_label = tk.StringVar()
current_label.set(current_text)

label = tk.Label(window,textvariable=total_label,font=DEFAULT_FONT,bg='white',width=24,height=2,anchor='e',padx=25)
label.pack(expand=True,fill='both')

currentLabel = tk.Label(window,textvariable=current_label,font=DEFAULT_FONT,bg='white',width=24,height=1,anchor='e',padx=25)
currentLabel.pack(expand=True,fill='both')

frame = Frame(window)
frame.pack(expand=True,fill='both')

#digits
button1 = tk.Button(frame, text=1, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(1))
button1.grid(row=4,column=1)
button2 = tk.Button(frame, text=2, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(2))
button2.grid(row=4,column=2)
button3 = tk.Button(frame, text=3, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(3))
button3.grid(row=4,column=3)

button4 = tk.Button(frame, text=4, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(4))
button4.grid(row=3,column=1)
button5 = tk.Button(frame, text=5, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(5))
button5.grid(row=3,column=2)
button6 = tk.Button(frame, text=6, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(6))
button6.grid(row=3,column=3)

button7 = tk.Button(frame, text=7, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(7))
button7.grid(row=2,column=1)
button8 = tk.Button(frame, text=8, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(8))
button8.grid(row=2,column=2)
button9 = tk.Button(frame, text=9, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(9))
button9.grid(row=2,column=3)

button0 = tk.Button(frame, text=0, height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:button_pressed(0))
button0.grid(row=5,column=2)
buttonDot =  tk.Button(frame, text='.', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:dot_button())
buttonDot.grid(row=5,column=3)
buttonNegate =  tk.Button(frame, text='\u00B1', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:negate())
buttonNegate.grid(row=5,column=1)
#digits

#operators
buttonAdd =  tk.Button(frame, text='+', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command=lambda:operator_button('+'))
buttonAdd.grid(row=4,column=4)
buttonSub =  tk.Button(frame, text='-', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:operator_button('-'))
buttonSub.grid(row=3,column=4)
buttonMult =  tk.Button(frame, text='\u00D7', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:operator_button('*'))
buttonMult.grid(row=2,column=4)
buttonDiv =  tk.Button(frame, text='/', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:operator_button('/'))
buttonDiv.grid(row=1,column=4)
buttonEqual =  tk.Button(frame, text='=', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command = lambda:equal())
buttonEqual.grid(row=5,column=4)
#operators

buttonMod = tk.Button(frame, text='%', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:operator_button('%'))
buttonMod.grid(row=1,column=3)
buttonFactorial = tk.Button(frame, text='𝑛!', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"fact({current_text})"))
buttonFactorial.grid(row=1,column=2)
buttonSqrt = tk.Button(frame, text='\u221A𝑛', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"sqrt({current_text})"))
buttonSqrt.grid(row=1,column=1)

buttonDel = tk.Button(frame, text='Del', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:del_button())
buttonDel.grid(row=0,column=4)
buttonClear = tk.Button(frame, text='C', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:clear_button())
buttonClear.grid(row=0,column=3)
buttonAbs = tk.Button(frame, text='|𝑥|', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"abs({current_text})"))
buttonAbs.grid(row=0,column=2)
buttonReciprocal = tk.Button(frame, text='\u00B9/ₓ', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"1/({current_text})"))
buttonReciprocal.grid(row=0,column=1)

buttonCeil = tk.Button(frame, text='\u2308𝑥\u2309', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"ceil({current_text})"))
buttonCeil.grid(row=0,column=0)
buttonFloor = tk.Button(frame, text='\u230a𝑥\u230b', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"floor({current_text})"))
buttonFloor.grid(row=1,column=0)
buttonSqr = tk.Button(frame, text='𝑥\u00B2', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"sqr({current_text})"))
buttonSqr.grid(row=2,column=0)
buttonXy = tk.Button(frame, text='𝑥\u02B8', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:operator_button('**'))
buttonXy.grid(row=3,column=0)
buttonLogyX = tk.Button(frame, text='logᵧ𝑥', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"log({current_text},"))
buttonLogyX.grid(row=4,column=0)
buttonLogX = tk.Button(frame, text='log 𝑥', height=2, width=5, font=DEFAULT_FONT, bd= 0,activebackground ='light gray',command= lambda:special_operator(f"log({current_text})"))
buttonLogX.grid(row=5,column=0)


if __name__ == '__main__':
    window.mainloop()