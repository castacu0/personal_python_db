from QuestionX import Question

some_prompts = [
    "What color are apples?   \n (a) Red   \n (b) Orange   \n (c) Black \n:", 
    "\nWhat color are bananas?   \n (a) Blue,   \n (b) Yellow   \n (c) Purple \n:",
    "\nWhat color are strawberries?,   \n (a) Pink/Red   \n (b) Brown   \n (c) Green \n:"
    ]

list_of_objects = [
    Question(some_prompts[0],  "a"), #this is receiving 2 params acording to  >>> def __init__(self, promtX, answerX):
    Question(some_prompts[1],  "b"),
    Question(some_prompts[2],  "a"), 
]

def function_runner(list_of_objects):
    """Returns your result of a multiple choice quiz.
       
    The user is asked 3 questions and get back the 
    number of questions he got right. Using a 
    Question datatype, I'm storing the values
    my object will take to work. 

    Parameters:
    score increases with every efective loop
    user_answer gets its value from the traveler
    traveler moves through the class instance (object) Question 
              
    Returns:
    Returns the correct results you got
    """
    score = 0
    for traveler in list_of_objects:
        user_answer = input(traveler.prompt,) #   >>>self.prompt
        if user_answer == traveler.answer:   #   >>>self.answer 
            score += 1
    print("\nYou got ", score, "/", len(list_of_objects), " correct.")

help(function_runner)

function_runner(list_of_objects) #caller
