# a function called most_frequent that takes a string and prints the letters in decreasing order of frequency
# on python 2.7
import operator

def most_frequent(word):
  d = dict()
  for i in word:
      if i not in d:
          d[i] = 1
       else:
          d[i] += 1
 sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
 print sorted_d
 
