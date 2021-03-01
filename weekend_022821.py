#!/usr/bin/python

import mymodule022821

class weekend():
  day_off="Yes extra day off"
  learn_stuff="Yes learn some stuff"

  def __init__(self, whichday, dowhat):
    self.whichday=whichday
    self.dowhat=dowhat

  def location(self, where):
    print('During weekend on ' + self.whichday + ' it is awesome to have activity like ' + self.dowhat + ' at ' + where + ' which is really relax')
 
w1=weekend('Sat', 'Hiking')
print(w1.whichday)

w1.location('Lake Chabot')

class weekend2(weekend):
  pass

w2=weekend2('Sun', 'Church')

w2.location('remotely')  

# dict

thisdict={
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

# for a in thisdict:
#   print(a)
# 
# for b in thisdict:
#   print(thisdict[b])

# for a in thisdict.keys():
#   print(a)
# 
# for b in thisdict.values():
#   print(b)

# for a,b in thisdict.items():
#   print(a,b)

# adding dict items

thisdict["Thurs"]="Four"

print(thisdict)

# how to invert dict

invert={}

for a in thisdict:
  invert[thisdict[a]]=a

print(invert)

# try except

today="Sun"

try:
  print(today)
except:
  print('today is NOT defined')

# method

def addsum(first, second):
  print('after adding ' + str(first) + ' and ' + str(second) + 'total becomes ', first + second ,' is our answer'  )

addsum(3,4)

# run method under module

mymodule022821.greeting('Jordan')

month="Feb"

if month == "Feb":
  print("Month is Feb")
else:
  print("Month is NOT Feb")


