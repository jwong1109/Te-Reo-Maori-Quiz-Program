# Creating the months as a class with the Maori name, and English name,
# and numeric month as objects and putting these details into a list.
# Create a variable to store the number of questions so far
# and the number of correct questions.

class Questions:
    def __init__(self, eng_month, maori_month, numeric_month):
        self.eng_month = eng_month
        self.maori_month = maori_month
        self.numeric_month = numeric_month
        questions.append(self)


questions = []
num_questions = 0
num_correct = 0

Questions("January", "Kohi-tātea", 1)
Questions("February", "Hui-tanguru", 2)
Questions("March", "Poutū-te-rangi", 3)
Questions("April", "Paenga-whāwhā", 4)
Questions("May", "Haratua", 5)
Questions("June", "Pipiri", 6)
Questions("July", "Hōngongoi", 7)
Questions("August", "Here-turi-kōkā", 8)
Questions("September", "Mahuru", 9)
Questions("October", "Whiringa-ā-nuku", 10)
Questions("November", "Whiringa-ā-rangi", 11)
Questions("December", "Hakihea", 12)
