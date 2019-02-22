from sys import exit
 
def game():
    print ("Now you start a game.")
    print ("You enter into a castle, and there are two doors in front of you.")
    print ("Which door you will choose?")

    next = input("> ")

    if next == "left":
        princess_room()
    elif next == "right":
        monster_room()
    else:
        dead("You spend too much time. Game over!")
    
def dead(why):
    print (why)
    exit(0)

def princess_room():
    print ("You need to survive the princess.")
    print ("Which you will do?")
    print ("1. Fight with the monster.")
    print ("2. Kiss the princess.")

    next = input("> ")

    if next == "1":
        print ("Good luck, brave guy!")
        monster_room()
    elif next == "2":
        print ("the princess wakes up and give you a huge house.")
        exit(0)
    else:
        dead("It seems like you do not want to save the princess.")

def monster_room():
    print ("There is a monster and you need to default it.")
    print ("How you will fight with it?")
    print ("1. Hit the stone to it.")
    print ("2. Use the fire.")

    next = input("> ")

    if next == "1":
        dead("You are defaulted by the monster. Game over!")
    elif next == "2":
        print("The monster is defaulted by you and you save the princess. Good job!")
        exit(0)
    else:
        dead("You lose the time. Game over!")


game()