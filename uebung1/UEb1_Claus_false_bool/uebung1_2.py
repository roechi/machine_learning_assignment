from redditdata import data
i = 0
f = open("C:\Users\Holland\Desktop\_reddit.txt",'w') #write object is f
for dic in data:
    
    f.write("Post #"+str(i)+"\n")
    f.write('\t' + dic['title']+"\n")
    f.write('\t'+ '\t' + dic['sub'] +" ("+str(dic['comments'])+")"+"\n")
    i = i+1

f.close();
#parse data-List, alle drei dictionaries (i)
#jeweils write to file "Post #"+i newline "    " + wert1 newline "        " + wert2 +" "+wert3