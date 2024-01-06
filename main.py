import math
from tkinter import *

countw = 1500
countb = 300
countlb = 1200
run = True
iterate = 0
mark = "✔"
def click():
    global iterate,run,mark
    run = True
    iterate+=1

    if run is True:
        if iterate % 8 ==0:
            mark = ""
            timer.config(text="Long Break", fg="red")
            check1.config(text=mark)
            work(countlb)
            mark = "✔"
        elif iterate % 2 != 0:
            print(iterate)
            work(countw)
            timer.config(text="Work", fg ="green")
        else:
            for i in range(0, 1):
                check1.config(text=mark)
                mark += "✔"
            timer.config(text="Break", fg="orange")
            work(countb)

def work(count):
    global run
    if run is True:
        sec = count % 60
        min = math.floor(count/60)
        print(count)
        if count >= 0:
            # used for sec reduce
            screen.after(1000, work, count - 1)
            if sec <10:
                canva.itemconfig(change_text, text=f"{min}:0{sec}")
            else:
                canva.itemconfig(change_text, text=f"{min}:{sec}")
        else:
            click()

def reset():
    global run,iterate
    iterate=0
    canva.itemconfig(change_text, text="00:00")
    timer.config(text="Timer" ,fg="black")
    check1.config(text="")
    run = False


screen = Tk()
screen.minsize(width=700, height=700)
screen.title("Pomodora")
screen.config(bg="lightblue", padx=200, pady=100)

start = Button(text="start", command=click)
start.grid_configure(row=3, column=1)

reset = Button(text="reset", command=reset)
reset.grid_configure(row=3, column=3)

timer = Label(text="Timer", padx=5, pady=5, font=("Arial", 20, "bold"), bg="lightblue")
timer.grid_configure(row=1, column=2)

check1 = Label(font="Arial", bg="lightblue", fg="green")
check1.grid_configure(row=4, column=2)

canva = Canvas(width=210, height=240, bg="lightblue", highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canva.create_image(107, 120, image=pic)
change_text = canva.create_text(110, 130, text="00:00", fill="white", font=("Arial", 20, "bold"))
canva.grid_configure(row=2, column=2)



screen.mainloop()







