f = open('reference.txt','r') #read reference
target = open('target.txt','r') #flank file read
w = open('match.txt','w') #file write

ref = f.readlines()

for i in target.readlines():
    s = i.replace("\n","").replace("\r","").split("\t")
    w.write(s[0]+"\t")
    fl = 0
    
    for j in ref:
        k = j.replace("\n","").replace("\r","").split("\t")
        if(s[0] == k[0]):
            w.write(k[1]+"\t"+k[2]+"\t"+k[3]+"\t"+k[4]+"\t"+k[5]+"\t"+k[6]+"\t"+k[7]+"\t"+k[8]+"\t"+k[9]+"\n")
            fl = 1

    if(fl == 0):
        w.write("\n")

w.close()
