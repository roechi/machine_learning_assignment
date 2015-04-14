fw = open('chemicals.txt')
dic = {}

for line in fw:
    (key, value) = line.split(': ')
    dic[key] = value.strip('\n')

print(dic)