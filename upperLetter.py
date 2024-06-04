
class upperLetters:

    def __init__(self, text):
        self.text = text

    def get_String(self, letters):
        self.letters = letters
        letters.upper()

    def print_String(self):
        print("Text is: ", self.text)
        print("The upper letter text is: ", self.letters)

sentence = upperLetters("vlady e ligla!")
sentence.get_String()
sentence.print_String()

