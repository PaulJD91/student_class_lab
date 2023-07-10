class CodeClanStudent:

    def __init__(self, student_name, cohort):
        self.student_name = student_name
        self.cohort = cohort

    def talk(self):
        return print("I can talk!")

    def fav_language(self, favourite_language):
        return print("I love " + favourite_language)  
        