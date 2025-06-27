from tkinter import *
import random

TYPED = []
NO_CHAR = 0
begin = False
def count_down(count):
    global begin, NO_CHAR
    if not begin:
        count = 0
    if my_text.get() != "":
        begin = True
    if begin:
        count_label.config(text=f"Timer : {int(count / 1000)}", fg="green")
        if int(count / 1000) >= 60:
            count_label.config(fg = "red")
            sample.destroy()
            my_text.destroy()
            no_word = len(TYPED)
            def cpn(index):
                global NO_CHAR
                if index != no_word:
                    NO_CHAR = NO_CHAR + len(TYPED[index]) + 1
                    cpn(index+1)
            cpn(0)
            NO_CHAR = NO_CHAR - 1
            result = Label(text=f"Result is WPS:{int(NO_CHAR/5)}", font=("Arial", 50, "bold"))
            result.grid(row=1, column=0)
            return None
    pass_text = my_text.get()
    if " " in pass_text:
        pass_text = pass_text.split()[0]
        if pass_text == text_lis[0]:
            TYPED.append(text_lis[0])
            text_lis.pop(0)
            sample.config(text=get_text())

        my_text.delete(0, END)

    window.after(1, count_down, count+1)

def get_text():
    t_text = ""
    for i in range(10):
        t_text = t_text + text_lis[i] + " "
    return t_text


window = Tk()
window.title("Typing Test")
window.config(padx=50, pady=50)
window.minsize(width=500, height=100)


count_label = Label(text="Timer : 0",font=("Arial", 20, "bold"))
count_label.grid(row=0,column=0)

with open(file="text.txt", mode="r") as data:
    text = data.readlines()                                        #here there is problem of - sign instead of geting - it get â€”.
    text_lis = random.choice(text).replace("â€”", "-").split(" ")  # or using encoding='utf-8' in open.
TEXT = get_text()
sample = Label(text=TEXT, font=("Arial", 20, "bold"))
sample.grid(row=1,column=0,columnspan=100)

window.after(2, get_text)
my_text = Entry(font=("Arial", 15, "bold"))
my_text.grid(row=2,column=0,columnspan=100)


timer = count_down(0)
window.mainloop()