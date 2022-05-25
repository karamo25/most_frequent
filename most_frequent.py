# a function called most_frequent that loads a string of words from a file and prints the letters in decreasing order of frequency
# on python 2.7
import operator

def most_frequent(file_name):
  words = open(file_name).read()
  
  d = dict()
  for letter in word:
      if letter not in d:
          d[letter] = 1
       else:
         d[letter] += 1
          
  sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
  for item in sorted_d:
    print item
 

if _name_ == '_main_':
  file = 'words.txt'
  most_frequent(file)
  print("New changes to be seen by git")
  
