from sys import exit
from random import randint

class Death(object):

    quips = {
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    }

    def enter(self):
        a = randint(0,len(self.quips)-1)
        print (Death.quips[a])
        exit(1)

a = Death()
a.enter()
