#!/usr/bin/env python

import argparse
import random
import linecache
import sys

DEFAULT_PASSWORD_LENGTH = 5

parser = argparse.ArgumentParser(description='Generate correct horse battery staple style password.')

parser.add_argument('-p','--passlength', default=DEFAULT_PASSWORD_LENGTH, type=int, help='wordlength of the generated password')
parser.add_argument('wordlist', help='text file containing line separated words, used to generate password')

args = parser.parse_args()


WLLength = 0
for line in open(args.wordlist):
    WLLength = WLLength + 1

Wordpool = list()
Job = 0

secureRandom=random.SystemRandom()

while Job < args.passlength:
   RandWord = secureRandom.randint(0, WLLength)
   Wordpool.append(linecache.getline(args.wordlist,RandWord))
   Job = Job + 1

linecache.clearcache()

print("".join(Wordpool))