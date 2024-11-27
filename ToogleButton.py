from tkinter import Tk, PhotoImage, Button

root = Tk()
root.title("Toogle Switch")
root.geometry("400x600")
root.config(bg="white")

button_mode = True


def customize():
    global button_mode
    if button_mode:
        button.config(image=off, bg="#26242f", activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode = False
    else:
        button.config(image=on, bg="white", activebackground="white")
        root.config(bg="white")
        button_mode = True


on = PhotoImage(file="Images\\light.png")
off = PhotoImage(file="Images\\dark.png")

button = Button(root, image=on, bd=0, bg="white", activebackground="white",
                command=customize)
button.pack(padx=50, pady=50)

root.mainloop()
