#!/usr/bin/env python
import re
import collections

'''\
Literary Analysis
Description

Your English teacher has just asked you to write a paper comparing two of the 
works from the free, online literature library at Project Gutenberg. Since you 
are a computer scientist, you decide to put your skills to use. You plan to 
compare your two favorite works of classic literature in terms of the 
vocabulary used in each. Since this a bit outside the scope of the assignment 
as described by your English teacher, you ask for permission before you 
proceed. Intruiged by your proposal, your English teacher agrees and you are 
ready to go.

You plan to write a program that will take a text file as input and return a 
report listing alphabetically all the words in the file and the number of 
occurances of each.

source:http://openbookproject.net/pybiblio/practice/\
'''


def main():
    '''\
    Ask the user for a text file then analyse it to see how many times each 
    word in the file is used\
    '''
    
    filename = input("enter the path to the file that you would like to analyse: ")
    counter = collections.Counter()
    with open(filename) as file:
        for line in file:
            # Use regex to find all words in the line
            words = re.findall(r'\w+', line.lower())
            counter.update(words)
    print(counter)
    return counter
            
if __name__ == "__main__":
    main()

