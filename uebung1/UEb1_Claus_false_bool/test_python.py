dictionary1 = {}
with open("C:\Users\Holland\Desktop\py_ueb1_1.txt") as f:
    for line in f:
       ke, va = line.split() #standard argument is emptyspace, var names are free
       print ke,va
       dictionary1[ke] = va # placeholdervars, similar to i in for-loop

for ke in dictionary1:
		print dictionary1[ke] #output of a map has no particular order