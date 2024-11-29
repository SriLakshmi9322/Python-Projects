from tkinter import Tk, PhotoImage, ttk, Label, GROOVE, Frame, Text
from tkinter import WORD, Scrollbar, Button, messagebox, END
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

translator = Translator()


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    """Translate the text from one language to another."""
    try:
        text_ = text1.get(1.0, END).strip()  # Strip to remove extra newline
        source_lang = combo1.get()
        target_lang = combo2.get()

        if text_:
            # Find source and target language codes
            source_code = next((k for k, v in language.items()
                                if v.lower() == source_lang.lower()), None)
            target_code = next((k for k, v in language.items()
                                if v.lower() == target_lang.lower()), None)

            if not source_code or not target_code:
                raise ValueError("Invalid language selection!")

            # Translate
            translated_text = translator.translate(text_, src=source_code,
                                                   dest=target_code).text
            text2.delete(1.0, END)
            text2.insert(END, translated_text)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")


# Icon
image_icon = PhotoImage(file="Images\\google_translator.png")
root.iconphoto(False, image_icon)

# Arrow
arrow_image = PhotoImage(file="Images\\arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

language = LANGUAGES
languageV = list(language.values())
# lang1 = language.keys()

# Statement to be Translated
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white",
               width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Translated Statement
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", width=18, bd=5,
               relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate Button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="purple", cursor="hand2", bd=5,
                   bg='red', fg="white", command=translate_now)
translate.place(x=480, y=250)


# Function Call
label_change()

root.configure(bg="white")
root.mainloop()
