print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input ("Enter a Word:")
if len(original) > 0 and original.isalpha():  <- if the input is bigger than zero shows the input
  print original
else:
    print "empty"
    
    --------- original.isalpha() is to make sure that in the string does not contain interger
    
    
    pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
    print 'empty'
    
    ------- new_word = new_word[1:len(new_word)] is will start to print from the 1 char until the lenght of the new_word variable
