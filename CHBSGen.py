#!/usr/bin/env python

import argparse
import random
import linecache
import sys
import traceback

DEFAULT_PASSWORD_LENGTH = 5
DEFAULT_MINIMUM_WORD_LENGTH = 1

def main(argv=None):
    args = argHandler(argv)
    print(generatePassword(args.wordlist, args.passlength, args.minWordLength, args.delimiter))

def argHandler(argv):
    parser = argparse.ArgumentParser(description='Generate correct horse battery staple style password.')

    parser.add_argument('-p','--passlength', default=DEFAULT_PASSWORD_LENGTH, type=int, help='wordlength of the generated password')
    parser.add_argument('-m','--minWordLength', default=DEFAULT_MINIMUM_WORD_LENGTH, type=int, help='specify minimum individual wordlength')
    parser.add_argument('-d','--delimiter', default="", help='specify delimiter')
    parser.add_argument('wordlist', help='text file containing line separated words, used to generate password')

    return parser.parse_args(argv)

def getWordListLength(wordList):
    WLLength = 0
    for line in open(wordList):
        WLLength = WLLength + 1
    
    return WLLength
    
def getWordFromList(wordList, minWordLength):
    secureRandom = random.SystemRandom()
    try:
        if(minWordLength < 1):
            raise ValueError("[errno 2] minWordLength is not positive")
    except:
        traceback.print_exc()
    else:
        while True:
            randLine = secureRandom.randint(0, getWordListLength(wordList))
            randWord = linecache.getline(wordList,randLine)
            if (len(randWord) >= minWordLength+1):
                linecache.clearcache()
                return randWord.rstrip()            

def generatePassword(wordList, passLength, minWordLength, delimiter):
    Wordpool = list()
    Job = 0
    
    try:
        if (passLength < 1):
            raise ValueError("[errno 2] passlength is not positive")
    
    except ValueError:
        traceback.print_exc()    
    
    else:    
        while Job < passLength:
            Wordpool.append(getWordFromList(wordList, minWordLength) + delimiter)
            Job = Job + 1

        return "".join(Wordpool)

if __name__ == "__main__":
    sys.exit(main())