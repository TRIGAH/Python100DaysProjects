from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
CANVAS_COLOR = "#ffffff"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20,pady=20)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR,highlightthickness=0,fg="white")
        self.score_label.grid(row=0,column=2)

        self.canvas = Canvas(width=300,height=250) 
        self.canvas_color=self.canvas.config(bg=CANVAS_COLOR)
        self.question_text=self.canvas.create_text(150,125,text="",font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=3,pady=50)

        self.true_image = PhotoImage(file="day-34\\quizzler-app-start\\images\\true.png")
        self.true_button = Button(image=self.true_image, command=self.is_correct_answer)
        self.true_button.config(padx=20,pady=20)
        self.true_button.grid(row=2,column=1)

        self.false_image = PhotoImage(file="day-34\\quizzler-app-start\\images\\false.png")
        self.false_button = Button(image=self.false_image,command=self.is_wrong_answer)
        self.false_button.config(padx=20,pady=20)
        self.false_button.grid(row=2,column=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()   
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.canvas.config(bg=CANVAS_COLOR) 
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the Quiz.... Start Over")
            self.canvas.config(bg=CANVAS_COLOR) 
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def is_correct_answer(self):
        user_answer=self.quiz.check_answer("True") 
        self.give_feedback(user_answer)
        self.score = self.quiz.score
        self.score_label.config(text=f"Score: {self.score}")

    def is_wrong_answer(self):
        user_answer=self.quiz.check_answer("False") 
        self.give_feedback(user_answer)

    def give_feedback(self,user_answer): 
        if user_answer == True:
            self.canvas.config(bg="#00FF00")
            self.window.after(1000,func=self.get_next_question)
        else:
            self.canvas.config(bg="#FF0000")
            self.window.after(1000,func=self.get_next_question)


     