""" I created a MadLibs game, the user is asked to input words of a certain type such as an adjective, noun or past tense verb. Then, a story is printed to the screen with the input from the user."""

# Madlib Story:

# Parts of Speech Mad Libs from Everyday Speech
""" Tina and John walked deep into the _(adjective)_ woods. They came upon a _(adjective)_ old house. The house looked so _(adjective)_ and creepy. On the front porch sat an old large _(noun)_. Tina thought she heard a _(adjective)_ sound coming from the house. John _(past tense verb)_ so high he touched a tree branch!"""

#Properties
# firstAdj
# secondAdj
# thirdAdj
# noun
# fourthAdj
# pastTenseVerb

# User Input Functions
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#Testing code
def test():
    user_value = user_input("Please eneter a value: ")
    print(user_value)

# Run Test
#test()

#Madlibs Function
def getWordsFromUser():
    firstAdj = user_input("Give me an adjective: ")
    secondAdj = user_input("Give me an adjective: ")
    thirdAdj = user_input("Give me an adjective: ")
    noun = user_input("Give me noun: ")
    fourthAdj = user_input("Give me an adjective: ")
    pastTenseVerb = user_input("Give me a past tense action verb: ")
    #Print user input + story
    print("Tina and John walked deep into the %s woods. They came upon a %s old house. The house looked so %s and creepy. On the front porch sat an old large %s. Tina thought she heard a %s sound coming from the house. John %s so high he touched a tree branch!" % (firstAdj, secondAdj, thirdAdj, noun, fourthAdj, pastTenseVerb))


getWordsFromUser()
