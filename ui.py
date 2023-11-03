from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # User answer
        self.user_answer = None

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
        self.true_button = Button(self.window, image=self.true_image,
                                  highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(self.window, image=self.false_image,
                                   highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        # Score text
        self.score_text = Label(self.window, text=f"Score: {self.quiz.score}",
                                font=("Arial", 15, "italic"), bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0, sticky="S")

        # Question text
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets next question"""
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_button_pressed(self):
        """Checks if true button got pressed"""
        if not self.quiz.still_has_questions():
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            exit()
        else:
            self.user_answer = "True"
            self.quiz.check_answer(user_answer=self.user_answer)
            self.update_score()
            self.get_next_question()

    def false_button_pressed(self):
        """Checks if false button got pressed"""
        if not self.quiz.still_has_questions():
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            exit()
        else:
            self.user_answer = "False"
            self.quiz.check_answer(user_answer=self.user_answer)
            self.update_score()
            self.get_next_question()


    def update_score(self):
        """Update score"""
        self.score_text.config(text="Score: " + str(self.quiz.score))
        if self.quiz.current_question.answer == self.user_answer:
            self.canvas.config(bg="green")
            self.window.after(1000, self.revert_background_color)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.revert_background_color)

    def revert_background_color(self):
        """"Changes background of canvas back to original"""
        self.canvas.config(bg="white")
