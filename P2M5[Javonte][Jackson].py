curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
elements = open("elements1_20.txt", "r")
elementsltxt = elements.read().lower()
elementslist = elementsltxt.split("\n") #curling the list and formatting it

def elementsquiz(): #defining funciton
    points = 0
    attempts = 5
    correctinputslist = []
    incorrectinputslist = []    #setting up variables 
    while True:
        playerinput = input("Name one of the first twenty elements in the periodic table")
        playerinput = playerinput.lower()
        while playerinput in correctinputslist:
            if (playerinput in correctinputslist):       #this part of the function takes... 
                print("no duplicates please!")           #...the input and makes sure it isnt a duplicate
                playerinput = input("Name one of the first twenty elements in the periodic table")
                playerinput = playerinput.lower()
            if playerinput not in correctinputslist:
                break                                          
        if (playerinput in elementslist): #if answer is correct
            points += 1
            print("good job")
            correctinputslist.append(playerinput) #adding input to a list of answers that can't be chosen again

        else: #if answer is incorrect
            print("sorry that is incorrect")
            incorrectinputslist.append(playerinput)
        attempts -= 1 #form of loop termination
        if attempts <= 0: #if the player is out of times the loop terminates
            break
    print(points * 20, "% correct") #showing % correct
    print("Answers found:", correctinputslist) #showing correct answers
    print("incorrect answers:", incorrectinputslist) #showing incorrect answers




elementsquiz()
