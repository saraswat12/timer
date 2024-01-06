from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# _______________________________ Reset MECHANISM __________________________________ #

def reset_timer():
    Window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0



# _______________________________ timer MECHANISM __________________________________ #


def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 2 == 0:
        if reps == 8:
                # it's the 8th rep
            label.config(text = "break", fg = GREEN)
            count_down(long_break_sec)
        else:
                 # it's the 2nd/4th/6th rep
             label.config(text = "short break", fg =RED )
             count_down(short_break_sec)

    else:
            # it's the 1st/3rd/5th/7th rep
        label.config(text = "Work time", fg =PINK )
        count_down(work_sec)
        
    

 
# _______________________________ COUNTDOWN MECHANISM __________________________________ #

def count_down(count):
    #print(count)
    global timer
    count_minutes = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_sec}")
    if count>0:
        timer = Window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        check_mark.config(text=marks)
        

        

# _______________________________ GUI SETUP ____________________________________________ #

Window = Tk()
Window.title("new")
Window.config(padx=100, pady=20, bg=YELLOW)




label = Label(text = "TIMER", font=(FONT_NAME, 35, "bold"), bg =YELLOW, fg=GREEN)
label.grid(column=1, row=0)
              

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0) #highlightthickness for removing the border of canvas to set to 0
image = PhotoImage(file=r"D:\python_new projects\condown\tomato.png")
canvas.create_image(103, 112, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=RED, highlightthickness=0, command = start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=RED, highlightthickness=0, command =reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW)
check_mark.grid(column=1, row=3)


Window.mainloop()

















