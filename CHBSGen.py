from sys import argv
import random
import linecache
import sys

script, pl, Wordlist = argv

PassLength = int(pl)
WLLength = 0
for line in open(Wordlist):
    WLLength = WLLength + 1

Wordpool = list()
Job = 0

secureRandom=random.SystemRandom()

while Job < PassLength:
    RandWord = secureRandom.randint(0, WLLength)
    Wordpool.append(linecache.getline(Wordlist,RandWord))
    Job = Job + 1

linecache.clearcache()

print "".join(Wordpool),
