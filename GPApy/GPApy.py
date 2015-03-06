# Project - GPA (Grammar Parser & Adjuster)
# Description - Parses an input grammar, determines if it is LL(1) parsable.
#   If not it will attempt to make it LL(1) parsable.
#   A more detailed description along with instructions will be made available on the GitHub page.
# Author - Matthew Boatright
# Last Updated - March 6th, 2015

import sys

grammar_dictionary = {}

def main():
    
    if (len(sys.argv) < 2):
        print("This program requires a single file as a command line argument in order to run.")
    else:
        read(str(sys.argv[1]))

# This function will read the input file line by line.
# It will replace all instances of '->' or '|' with "" so that they are not part of the token array.
# Any instance of '@' will be replaced with "empty".
# The first token from a split line will be a terminal and will be sent to the method that controls the dictionary.
# Every following token on that line will be a separate rule that the non-terminal can go to.
def read(input):
    print("Reading file:" ,input ,"\n")
    
    file = open(input, 'r')
    lines = file.readlines()
    
    print("Selected Grammar")
    print("----------------")

    for i in range (0, len(lines)):
        if (lines[i].strip() != ""):
            lines[i] = lines[i].strip().replace("@", "empty")
            print(lines[i])
            tokens = lines[i].replace("->", "").replace("|", "").split()
            for j in range (0, len(tokens)):
                tk = tokens[j].strip()
                if (j == 0):
                    head = tk
                    #print("Nonterminal: ", tk)
                    input_nt(head)
                else:
                    #print("Leads to rule: ", tk)
                    input_rule(head, tk)

    print("\n")
    for key in sorted(grammar_dictionary):
        print(key, grammar_dictionary[key])

# In this method, a non-terminal is passed. It is then added to the global grammar_dictionary variable.
# If it already exists, the method will do nothing. Otherwise it will be added and given a default value by 0.
def input_nt(nt):
    #print("Adding ", nt, " to the dictionary")
    if nt not in grammar_dictionary:
        #print(nt, " doesn't exist - add it to the dictionary.")
        grammar_dictionary[nt] = 0

# In this method, a rule and the non-terminal it came from is passed. It will check to see if the current value is 0.
# If it is that means no rules have been added yet, so a listvariable is created and set to the key.
# If a list is already in place it will check to see if the rule is already in the list (no need for duplicate rules).
def input_rule(head, rule):
    #print("Adding ", rule, " to ", head)
    if (grammar_dictionary[head] == 0):
        lst = [rule]
        grammar_dictionary[head] = lst
    else:
        lst = grammar_dictionary[head]
        if (lst.count(rule) != 1):
            lst.append(rule)

if __name__ == "__main__":
    main()