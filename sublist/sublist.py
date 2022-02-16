"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'

def sublist(list_one, list_two):
    """
    Given any two lists A and B, determine if:

    List A is equal to list B; or
    List A contains list B (A is a superlist of B); or
    List A is contained by list B (A is a sublist of B); or
    None of the above is true, thus lists A and B are unequal
    """
    one = ''
    two = ''
    for index, val in enumerate(list_one):
        one += str(list_one[index])
    for index, val in enumerate(list_two):
        two += str(list_two[index])
    one = "".join(one)
    two = "".join(two)
    if one == two:
        if (len(list_one) == len(list_two)):
            return EQUAL
    if (len(one) < len(two)) and (len(list_one) != len(list_two)):
        if one in two:
            return SUBLIST
    if (len(one) > len(two)) and (len(list_one) != len(list_two)):
        if two in one:
            return SUPERLIST
    return UNEQUAL
