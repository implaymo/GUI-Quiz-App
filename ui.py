from tkinter import *

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("400x600")
        self.window.configure(bg=THEME_COLOR)
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=0, columnspan=1, padx=20, pady=20)

        # Configure the grid to expand the canvas
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.window.mainloop()