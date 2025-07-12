# Exercise 34 is about accessing elements of lits

import sys

animals = ['bear', 'tiger', 'aardvark', 'giraffe', 'dragon']

if animals[4] == 'dragon':
    sys.exit(0)
else:
    sys.exit('Index not correct')

# use echo $? in bash to view the last error code
