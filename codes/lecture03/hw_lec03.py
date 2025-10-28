from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class HomeworkLec03:
    def __init__(self):
        self.create_window()
        self.create_widgets()

    def create_window(self):
        self.root = Tk()
        self.root.title("Homework Lecture 03")
        self.root.geometry("400x300")

    def create_widgets(self):
        self.lbl_title = Label(self.root, text="Homework Lecture 03", font=("Arial", 16))
        self.lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.lbl_upload = Label(self.root, text="Upload File:")
        self.lbl_upload.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.btn_upload = Button(self.root, text="Browse", command=self.upload_file)
        self.btn_upload.grid(row=1, column=1, padx=10, pady=10, sticky="E")

        self.txt_display = Text(self.root, width=60, height=10)
        self.txt_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.btn_play = Button(self.root, text="Play", command=self.play_audio)
        self.btn_play.grid(row=3, column=1, padx=10, pady=10, sticky="E")

        self.lbl_ask = Label(self.root, text="Ask:")
        self.lbl_ask.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.entry_question = Entry(self.root, width=30)
        self.entry_question.grid(row=4, column=1, padx=10, pady=10, sticky="E")

        self.lbl_answer = Label(self.root, text="Answer:")
        self.lbl_answer.grid(row=5, column=0, padx=10, pady=10, sticky="W")
        self.txt_answer = Text(self.root, width=40, height=5)
        self.txt_answer.grid(row=5, column=1, padx=10, pady=10, sticky="E")

    def play_audio(self):
        pass

    def upload_file(self):
        pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HomeworkLec03()
    app.run()