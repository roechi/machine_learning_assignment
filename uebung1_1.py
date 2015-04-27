fw_chem = open('chemicals.txt')
dic = {}

for line in fw_chem:
    (key, value) = line.split(': ')
    dic[key] = value.strip('\n')

print(dic)
print("\n\n")


from redditdata import *

data_str = ""

for item in data:
    data_str += "Post #" + str(data.index(item)) + "\n"
    data_str += "\t" + item["title"] + "\n"
    data_str += "\t\t" + item["sub"] + "(" + str(item['comments']) + ")" + "\n"

print data_str

fw_data = open('reddit.txt', "w+")
fw_data.write(data_str)
fw_data.close()

import numpy as np

arr = np.array([[1, 1, 1, 1, 1],
[1, 2, 1, 1, 1],
[1, 1, 3, 1, 1],
[1, 1, 1, 4, 1]], int)

#Spaltensummen
for x in arr:
    print(x.sum())

#Zeilensummen
for x in arr.transposed():
    print(x.sum)

r = np.arange(5)

mask = r % 2 == 0
mask
array([ True, False,  True, False,  True], dtype=bool)

select = arr[[1,2]]
select

#array([[1, 2, 1, 1, 1],
#       [1, 1, 3, 1, 1]])

final = select[:, mask]
final

#array([[1, 1, 1],
#       [1, 3, 1]])
#
             
# a) arr * 5 -> multipliziert arr kompnentenweise mit 5
# b) arr * np.arange(arr.shape[1]) -> multipliziert arr mit dem Vektor [0, 1, 2, 3, 4]
# c) arr * np.arange(arr.shape[1]) -> multipliziert arr mit dem Vektor [0, 1, 2, 3], 
# geht aber nicht, da dimensionen nicht übereinstimmen     
# d) arr.T * np.arange(arr.shape[0]) -> transponiert arr.T, und dadurch kann arr mit dem vektor [0, 1, 2, 3] multipliziert werden

v = np.arange(5)

arr * v

v.T * arr