from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("350x460")
        self.window.configure(bg=THEME_COLOR)

        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Add padding at the top of the window
        self.window.grid_rowconfigure(0, minsize=50)

        # Images
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        # Buttons
        self.right_button = Button(self.window, image=self.true_image, highlightthickness=0)
        self.right_button.grid(column=0, row=2)
        self.false_button = Button(self.window, image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        # Score text
        self.score_text = Label(self.window, text="Score: 0 ", font=("Arial", 15, "italic"), bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0, sticky="S")

        # Question text
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)