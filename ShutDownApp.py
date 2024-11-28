from tkinter import Tk, PhotoImage, Button
import os

root = Tk()
root.title("Shutdown App")
root.geometry("400x580")


def restarttime():
    os.system("shutdown /r /t 30")


def restart():
    os.system("shutdown /r /t 1")


def shutdown():
    os.system("shutdown /s /t 1")


def logout():
    os.system("shutdown -l")


# First Button
restart_time_button = PhotoImage(file="Images/restart_time.png")
first_button = Button(root, image=restart_time_button, borderwidth=0,
                      cursor="hand2", command=restarttime)
first_button.place(x=10, y=10)

# Second Button
close_button = PhotoImage(file="Images/close.png")

second_button = Button(root, image=close_button, borderwidth=0, cursor="hand2",
                       command=root.destroy)
second_button.place(x=200, y=10)

# Third Button
restart_button = PhotoImage(file="Images/restart.png")

third_button = Button(root, image=restart_button, borderwidth=0,
                      cursor="hand2", command=restart)
third_button.place(x=10, y=200)

# Fourth Button
shutdown_button = PhotoImage(file="Images/shutdown.png")

fourth_button = Button(root, image=shutdown_button, borderwidth=0,
                       cursor="hand2", command=shutdown)
fourth_button.place(x=200, y=200)

# Fifth Button
logout_button = PhotoImage(file="Images/log_out.png")

fifth_button = Button(root, image=logout_button, borderwidth=0, cursor="hand2",
                      command=logout)
fifth_button.place(x=10, y=400)

root.mainloop()
