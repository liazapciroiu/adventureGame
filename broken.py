import time
import random
import randomItems

# randomItems.getRandomItems()


def getRandomItems():
    location = randomItems.locations.random.randint(0, 2)
    randomNumber = random.randint(0, 2)
    weapon = randomItems.weaponsToFind[randomNumber]
    artWeapon = randomItems.articulatedWeapons[randomNumber]
    creature = randomItems.creatures[random.randint(0, 2)]
    return location, weapon, artWeapon, creature


def printPause(message):
    print(message)
    time.sleep(0.8)


def introStory(location):
    printPause(f'You find yourself {location}.')
    printPause('In front of you are two passageways.')
    printPause('Which way do you want to go?')


def getWeapon(weapon, artWeapon):
    printPause(f'You notice right there waiting for you {weapon}.')
    printPause(f'You get {artWeapon} and off you go.')


def creatureBattle(location, weapon, artWeapon, creature):
    printPause(f'All of the sudden a {creature} cuts your way!')
    printPause('What do you want to do?')
    response = input('You can either fight(Press 1) or run away(Press 2) \n')
    if response == '2':
        printPause('GAME OVER \nYou lost!')
        playAgain(location, weapon, artWeapon, creature)
    elif response == '1':
        printPause(f'You take out {artWeapon}.')
        printPause(
            f'When the {creature} sees {artWeapon} it disappears into thin air.')
        printPause('GAME OVER \n You win!!!')
        playAgain(location, weapon, artWeapon, creature)


def leftPath(weapon, artWeapon, creature):
    printPause('You go to the left and something marvelous happens.')
    getWeapon(weapon, artWeapon)
    creatureBattle(artWeapon, creature)


def rightPath(weapon, artWeapon, creature):
    printPause('You go to the right and something unbelivable happens.')
    getWeapon(weapon, artWeapon)
    creatureBattle(artWeapon, creature)


def playerChoices(weapon, artWeapon, creature):
    response = input('Enter L to take the pathway to the left. \n'
                     'Enter R to take the pathway to the right \n').lower()
    if response == 'l':
        leftPath(weapon, artWeapon, creature)
    elif response == 'r':
        rightPath(weapon, artWeapon, creature)
    else:
        printPause('Please enther a valid option:')
        playerChoices(weapon, artWeapon, creature)


def playAgain(location, weapon, artWeapon, creature):
    response = input('Do you want to play again? (y/n)').lower()
    if response == 'y':
        playGame(location, weapon, artWeapon, creature)
    elif response == 'n':
        printPause('Thank you for playing!')
    else:
        printPause('I don\'t understand')


def playGame(location, weapon, artWeapon, creature):
    introStory(location)
    playerChoices(weapon, artWeapon, creature)


getRandomItems()
playGame(location, weapon, artWeapon, creature)
