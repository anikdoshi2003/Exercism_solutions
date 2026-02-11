"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def checker(big,small):
    if small == []:
        return True
    if len(small) > len(big):
        return False
    else:
        for i in range(0,len(big)- len(small) + 1):
            if big[i : i + len(small)] == small:
                return True
            
        return False
            

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif checker(list_one,list_two):
        return SUPERLIST
    elif checker(list_two, list_one):
        return SUBLIST
    else:
        return UNEQUAL
