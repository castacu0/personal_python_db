class Question:
    """
    What will be called will be the self.prompt and
    self.answer in the other file, without the X ones.
    """
    def __init__(self, promptX, answerX): #-> None:
        self.prompt = promptX
        self.answer = answerX
help(Question)