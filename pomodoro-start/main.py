from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps,marks
    marks=""
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(fg=GREEN,text="Timer")
    check_mark_label.config(text=marks)



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED) 

    elif reps % 2 == 0:
        count_down(short_break_sec)  
        timer_label.config(text="Break",fg=PINK) 
  
    else:
        count_down(work_sec)   
        timer_label.config(text="Work",fg=GREEN) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer=window.after(1000,count_down,count-1)
    else:
        start_timer()  
        global marks
        work_session = math.floor(reps/2)  
        for _ in range(work_session):
            marks += "✓"

        check_mark_label.config(text=marks)    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN,highlightthickness=0 ,font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=2,row=0)

canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)
tomato_img  = PhotoImage(file="pomodoro-start\\tomato.png")
canvas.create_image(100,100,image = tomato_img )
timer_text=canvas.create_text(102,135,text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2,row=4)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0,row=5)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=5,row=5)

check_mark_label = Label(bg=YELLOW,fg=GREEN,highlightthickness=0,font=(FONT_NAME, 15, "bold"))
check_mark_label.grid(column=2,row=7)

window.mainloop()