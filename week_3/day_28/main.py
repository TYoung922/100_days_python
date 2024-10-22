from itertools import count
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
high_reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    stage_info.config(text="Start Timer", fg=PINK)
    check_tracking["text"] = ""
    high_check["text"] = ""

    global reps
    global high_reps
    reps = 0
    high_reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    test_work = 10
    test_short = 5
    test_long = 14


    print(reps)
    if reps % 8 == 0:
        countdown(long_break)
        # countdown(test_long)
        stage_info.config(text="Long  Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break)
        # countdown(test_short)
        stage_info.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        # countdown(test_work)
        stage_info.config(text="Get to Work", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    global reps
    num_checks = int(reps / 2)


    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if 10 > count_sec >= 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        if reps == 9:
            check_tracking["text"] = ""
            global high_reps
            reps = 1
            high_reps += 1
            high_check["text"] = "✔" * high_reps

        else:
            check_tracking["text"] = "✔" * num_checks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


#Info text
stage_info = Label(text="Start Timer", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40, "bold"))
stage_info.grid(column=1, row=0)

#Tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


#buttons
start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2, pady=10)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2, pady=10)

#Check marks
reps_state = Label(text="Reps", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
reps_state.grid(column=1, row=2)

# current_status = int(reps / 2)
# checkmark = "✔" * current_status
check_tracking = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "normal"))
check_tracking.grid(column=1, row=3)

high_check = Label(bg=YELLOW, fg=RED, font=(FONT_NAME, 12, "normal"))
high_check.grid(column=1, row=4)






window.mainloop()







