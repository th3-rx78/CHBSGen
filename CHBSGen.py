#!/usr/bin/env python

import argparse
import random
import linecache
import sys

DEFAULT_PASSWORD_LENGTH = 5

def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    args = argHandler()
    print(generatePassword(args.wordlist, args.passlength))

def argHandler():
    parser = argparse.ArgumentParser(description='Generate correct horse battery staple style password.')

    parser.add_argument('-p','--passlength', default=DEFAULT_PASSWORD_LENGTH, type=int, help='wordlength of the generated password')
    parser.add_argument('wordlist', help='text file containing line separated words, used to generate password')

    return parser.parse_args()

def getWordListLength(wordList):
    WLLength = 0
    for line in open(wordList):
        WLLength = WLLength + 1
    
    return WLLength 

def generatePassword(wordList, passLength):
    Wordpool = list()
    Job = 0

    secureRandom=random.SystemRandom()

    while Job < passLength:
       RandWord = secureRandom.randint(0, getWordListLength(wordList))
       Wordpool.append(linecache.getline(wordList,RandWord))
       Job = Job + 1

    linecache.clearcache()

    return "".join(Wordpool)

if __name__ == "__main__":
    main()