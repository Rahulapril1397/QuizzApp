"""
    This is doc string.
"""
class ObjectiveTest(Quiz):
    """
        This is doc string.
    """
    OBJECTQUESTION = Quiz.objective_questions()

    def __init__(self, answer_objective):
        self.answer_objective = answer_objective

    def objective_quiz(self):
        """
            This is doc string.
        """
        for row in range(0, 10):
            objective_question = df.lioc[row, "Questions"]
            objective_option_a = df.loc[row, "A"]
            objective_option_b = df.loc[row, "B"]
            objective_option_c = df.loc[row, "C"]
            objective_option_d = df.loc[row, "D"]

            print("Question: ", objective_question)
            print("Opt A:", objective_option_a)
            print("Opt B:", objective_option_b)
            print("Opt C:", objective_option_c)
            print("Opt D:", objective_option_d)

            self.answer_objective = Quiz.user_answer()

class SubjectiveTest(Quiz):
    """
        This is doc string.
    """
    SUBJECTIVEQUESTION = Quiz.subjective_questions()

    def __init__(self, answer_subjective):
        self.answer_subjective = answer_subjective

    def subjective_quiz(self):
        """
            This is doc string.
        """
        for row in range(0, 10):
            subjective_question = df.lioc[row, "Questions"]
            subjective_option_a = df.loc[row, "A"]
            subjective_option_b = df.loc[row, "A"]
            subjective_option_c = df.loc[row, "A"]
            subjective_option_d = df.loc[row, "A"]

            print("Question: ", subjective_question)
            print("Opt A:", subjective_option_a)
            print("Opt B:", subjective_option_b)
            print("Opt C:", subjective_option_c)
            print("Opt D:", subjective_option_d)

            self.answer_subjective = Quiz.user_answer()
