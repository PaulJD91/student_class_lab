class CodeClanStudent:

    def __init__(self, student_name, cohort):
        self.student_name = student_name
        self.cohort = cohort

    def talk(self):
        return print("I can talk!")

    def fav_language(self):
        return input("What is your favourite language? ")  
        if input == "python":
            return print("I love python!")