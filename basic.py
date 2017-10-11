+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "PYTHON" [4]

print fifth_letter

parrot = "Norwegian Blue"
print len(parrot) <- Will print the lenght of the parrot string

parrot = "Norwegian Blue"
print parrot.lower() <- will convert everything to lower case
print parrot.upper()  <- will convert everything to uppercase

pi = 3.14

print str(pi) <- turns a int into a string

# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

input
'''wefwefwefwefe'''
name = raw_input("What is your name? ") <-- raw_input let the user type an input
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

my_string = raw_input ("What is you father\'s name?")
print len(my_string)
print my_string.upper()
