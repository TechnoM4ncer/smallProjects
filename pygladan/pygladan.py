# variable holding predetermined suffix
pyg = 'ay'

# get word to be translated from user
original = raw_input('Enter a word:')

""" make sure returned string is not empty
and does not contain numbers """
if len(original) > 0 and original.isalpha():
    # translate word by concatenation and slicing string
    word = original.lower()
    first = original[0]
    new_word = word + first + pyg
    new_word = word[1:len(new_word)]
    new_word += first + pyg
    
    # print translated word
    print new_word
    
""" if user returned empty string or string with numbers, print empty. """
else:
    print 'empty'