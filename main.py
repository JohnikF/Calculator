import tkinter

window = tkinter.Tk()
window.title("Calculator")
window.geometry("300x300")
window.configure(bg="silver")


def add():
    print("Adding")
    num_1 = text_num1.get()
    num_2 = text_num2.get()
    print(num_1)
    print(num_2)
    result = int(num_1) + int(num_2)
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))


def sub():
    print("Subtracting")
    num_1 = text_num1.get()
    num_2 = text_num2.get()
    print(num_1)
    print(num_2)
    result = int(num_1) - int(num_2)
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))


def mul():
    print("Multiplying")
    num_1 = text_num1.get()
    num_2 = text_num2.get()
    print(num_1)
    print(num_2)
    result = int(num_1) * int(num_2)
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))

def div():
    print("Dividing")
    num_1 = text_num1.get()
    num_2 = text_num2.get()
    print(num_1)
    print(num_2)
    result = int(num_1) / int(num_2)
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, str(result))


button_add = tkinter.Button(window, text="+", command=add, width= 7, height= 2, bg="gold")
button_add.place(x=95, y=110)

button_sub = tkinter.Button(window, text="-", command=sub, width= 7, height= 2, bg="gold")
button_sub.place(x=160, y=110)

button_mul = tkinter.Button(window, text="*", command=mul, width= 7, height= 2, bg="gold")
button_mul.place(x=95, y=154)

button_div = tkinter.Button(window, text="/", command=div, width= 7, height= 2, bg="gold")
button_div.place(x=160, y=154)

text_num1 = tkinter.Entry(window, width=20, bg="black", fg="gold")
text_num1.place(x=95, y=40)

text_num2 = tkinter.Entry(window, width=20, bg="black", fg="gold")
text_num2.place(x=95, y=81)

text_answer = tkinter.Entry(window, width=20, bg="black", fg="gold")
text_answer.place(x=95, y=221)

label_num1 = tkinter.Label(window, text="Enter the first number↓", bg="silver")
label_num1.place(x=95, y=20)

label_num2 = tkinter.Label(window, text="Enter the second number↓", bg="silver")
label_num2.place(x=95, y=61)

label_answer = tkinter.Label(window, text="This is the answer↓", bg="silver")
label_answer.place(x=95, y=200)

window.mainloop()
