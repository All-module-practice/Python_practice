# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

def tower_builder(n_floors):
    # build here
    new_list=[]
    for i in range(1,n_floors+1):
        spaces=' ' * (n_floors-i)
        star='*' * ((2*i)-1)
        new_list.append(spaces+star+spaces)
    return new_list
