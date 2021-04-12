class Laptop:
    """Hello"""
    def __init__(self, colorX, windowsX, yearX): #  METHOD 1
        self.color = colorX       #String
        self.windows = windowsX   #Boolean
        self.year = yearX         #Integer
    
    def it_is_windows(self): #  METHOD 2     #🧧 on_honor_roll
        if self.windows == True:
            return True
        else:
            return False #It's MAC or Linux
help(Laptop)