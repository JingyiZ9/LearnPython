from sys import exit
from random import randint

class start(object):

    def __init__(self, age):
        self.age = age
    
    def start(self):
        if self.age > 25:
            goldenroom().enter()
        else:
            monsterroom().enter()

class goldenroom(object):

    def enter(self):
        print ("Welcome! You entered into the golden room.")
        print ("How many gold you want to take?")

        gold = input("> ")

        if int(gold) > 1000:
            print ("you are greedy!")
            death().play() 
        else:
            print ("good job, you win the game!")
            exit(1)

class monsterroom(object):

    def enter(slef):
        print ("Welcome, you entered into the monster room.")
        print ("how do you plan to default the monster?")

        method = input("> ")

        if method == "fire":
            print("the monster is defaulted and you win the game!")
            exit(1)
        else:
            print("Sorry, you are defaulted.")
            death().play()

class death(object):

    def play(self):
        print("that game is over!")
        exit(1)

game = start(27)
game.start()
