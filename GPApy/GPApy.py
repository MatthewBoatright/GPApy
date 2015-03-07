# Project - GPA (Grammar Parser & Adjuster)
# Description - Parses an input grammar, determines if it is LL(1) parsable.
#   If not it will attempt to make it LL(1) parsable.
#   A more detailed description along with instructions will be made available on the GitHub page.
# Author - Matthew Boatright
# Last Updated - March 6th, 2015

import sys

grammar_dictionary = {}
left_recursion = []
checked = []

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
    
    # Read the file line by line has insert the values into their proper place.
    print("Selected Grammar")
    print("----------------")
    for i in range (0, len(lines)):
        if (lines[i].strip() != ""):
            lines[i] = lines[i].strip().replace("@", "empty")
            print(lines[i])
            tokens = lines[i].split("->")
            head = tokens.pop(0).strip()
            tokens = tokens.pop(0).strip().split("|")
            input_nt(head)
            input_rule(head, tokens)

    # Print out the collected grammar rules from the dictionary and display them.
    # Also send them through the left_rec function to determine if left recursion exists.
    print("\n")
    print("Grammar Dictionary")
    print("------------------")
    for key in sorted(grammar_dictionary):
        print(key, grammar_dictionary[key])
        checked = []
        checked.append(key)
        if (left_rec(key, grammar_dictionary[key], checked)):
            left_recursion.append(key)
    print("\n")

    # Now that the grammar has been completely read and inserted into the dictionary we can begin examining the grammar.
    print("Left Recursion")
    print("--------------")
    if left_recursion:
        for key in left_recursion:
            print(key, "has left recursion")
    else:
        print("No instances of left recursion found in the grammar.")
    print("\n")


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
        grammar_dictionary[head] = rule
    else:
        while (len(rule) > 0):
            lst = grammar_dictionary[head]
            tmp = rule.pop().strip()
            if (lst.count(tmp) != 1):
                lst.append(tmp)

# A function to determine the presence of left-recursion (including non-immediate) in the grammar.
# The parameters are as follows: 
#   key - the non-terminal we are looking for. If at any point the first value of a rule matches up with the key then left recursion exists.
#   lst - the current list that is being examined. This is a recursive function and the same key may be compared to multiple lists.
def left_rec(key, lst, chk):
    #print("Browsing", lst, "for", key)
    for rule in lst:
        if rule:
            val = rule.split().pop(0)
            #print("---Looking at", val)
            if (val == key):
                #print("Left recursion exists for key", key)
                return True
            if val in grammar_dictionary:
                #print("---", val, "is a non-terminal. Expanding search into it's rules.")
                if val not in chk:
                    chk.append(val)
                    if (left_rec(key, grammar_dictionary[val], chk)):
                        return True
    #print("No instances of left recusrion found for key", key)
    return False

def factor():
    return False

if __name__ == "__main__":
    main()