# GPApy
LL(1) Grammar Parser &amp; Adjuster (written in python)

The purpose of this project is primarily a learning experience for myself to become more familiar with both Python and GitHub.!

The description of the project:
This is a program that will accept an input file as a command line argument. It will parse the file line by line and break it down into tokens.
Each token will be added to a dictionary as either a non-terminal or a rule. Once this is done it will attempt to parse the grammar from a top-down perspective.
It will check for conflicts in the form of left-recursion, factor when necessary, as well as generate first and follow sets to determine if it is LL(1) parsable.
If it is not it will attempt to adjust the grammar to make it so.

More info to come soon.

Sample output:
Reading file: input.txt 

Selected Grammar
----------------
A -> B

B -> C

C -> da

C -> dd | big

C -> da

C -> empty

D ->



A ['B']

B ['C']

C ['da', 'dd', 'big', 'empty']

D 0
