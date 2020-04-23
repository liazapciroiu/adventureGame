import time
import random
import randomItems


# # def getRandomItems():
location = randomItems.locations[random.randint(0, 2)]
randomNumber = random.randint(0, 2)
weapon = randomItems.weaponsToFind[randomNumber]
artWeapon = randomItems.articulatedWeapons[randomNumber]
creature = randomItems.creatures[random.randint(0, 2)]
# return location, weapon, artWeapon, creature


def printPause(message):
    print(message)
    time.sleep(0.8)


def introStory():
    printPause(f'You find yourself {location}.')
    printPause('In front of you are two passageways.')
    printPause('Which way do you want to go?')


def validInput(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            printPause('Please select a valid option:')
    return response


def getWeapon():
    printPause(f'You notice right there waiting for you {weapon}.')
    printPause(f'You get {artWeapon} and off you go.')


def creatureBattle():
    printPause(f'All of the sudden a {creature} cuts your way!')
    printPause('What do you want to do?')
    response = validInput(
        'You can either fight(Press 1) or run away(Press 2). \n',
        '2', '1')
    if response == '2':
        printPause('GAME OVER \nYou lost!')
    elif response == '1':
        printPause(f'You take out {artWeapon}.')
        printPause(f'When the {creature} sees '
                   f'{artWeapon} it disappears into thin air.')
        printPause('GAME OVER \nYou win!!!')
    playAgain()


def theAction(path, attribute):
    printPause(f'You go to the {path} and something {attribute} happens.')
    getWeapon()
    creatureBattle()


def playerChoices():
    response = validInput('Enter L to take the pathway to the left. \n'
                          'Enter R to take the pathway to the right. \n',
                          'l', 'r')
    if response == 'l':
        theAction('left', 'marvelous')
    elif response == 'r':
        theAction('right', 'unbelivable')


def playAgain():
    # del location, weapon, artWeapon, creature
    response = validInput('Do you want to play again? (y/n)', 'y', 'n')
    if response == 'y':
        # del location, weapon, artWeapon, creature
        playGame()
    elif response == 'n':
        printPause('Thank you for playing!')


def playGame():
    # del location
    # getRandomItems()
    introStory()
    playerChoices()
    


playGame()
