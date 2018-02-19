import csv

_author_ = "Jeff Pratt"
_project_ = 'PythonDemoApp'


class TriviaQuestion():
    def __init__(self, question, choiceA, choiceB, choiceC, choiceD, answer):
        self.question = question
        self.a = choiceA
        self.b = choiceB
        self.c = choiceC
        self.d = choiceD
        self.answer = answer


class TriviaGame:
    def start(self):
        score = 0
        question_list = list()
        with open("questions", "rt") as csvFile:
            triviaReader = csv.reader(csvFile, delimiter=",")
            for line in triviaReader:
                question_dict = {"question": line[0], "a": line[1], "b": line[2], "c": line[3], "d": line[4],
                                 "answer": line[5]}
                question_list.append(question_dict)
        print("Welcome to the trivia game! Time to learn some python!")
        for q in question_list:
            print("Question : " + q["question"])
            print("a. " + q["a"])
            print("b. " + q["b"])
            print("c. " + q["c"])
            print("d. " + q["d"])
            answer = input("Answer : ").strip()
            if q["question"] == "Is Tableau somewhere I would like to work?":
                print("correct!")
                print("")
                score += 1
            elif answer == q["answer"]:
                print("correct!")
                print("")
                score += 1
            else:
                print("Bummer.. The correct answer was " + q["answer"] + " : " + q[q["answer"]])
                print("")
        print('Your score was : ' + str(score)+' out of ' + str(len(question_list)) +' ... Good Job!')

TriviaGame().start()
