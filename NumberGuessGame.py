import random
#random_number = random.randint(1, 10)
#Create empty variable for holding the guessed value to be entered by user
#and get loop to start since it's a string and will never == random_number at first
number_guessed = ''
#Create run variable to be able to enter loop
run = 'y'

while run == 'y':
    #reset the guessed variable so if the newly generated one is the same as previous,
    #the game will still run another round
    number_guessed = ''
    random_number = random.randint(1, 1)
    #while loop runs while the guessed number doesn't match the generated one
    while number_guessed != random_number:
        number_guessed = int(input("Enter your guess: "))
        #If the correct number is guessed, ask to go again
        if number_guessed == random_number:
            print('Go again? (y/n): ', end='')
            #update the run variable to go through the loop again, or terminate
            run = input()
