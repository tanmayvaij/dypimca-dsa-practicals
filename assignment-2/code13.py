#  Create a program to create array of string and display all elements in upper and lowercase (use numpy library)

from numpy import array, char

watches = array([ "titan", "rolex", "sonata", "fastrack" ])

ucw = char.upper(watches)
print(ucw)

lcw = char.lower(ucw)
print(lcw)
