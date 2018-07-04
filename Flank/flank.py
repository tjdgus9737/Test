f = open('reference(ref).txt','r') #read reference
flank = open('Flank.txt','r') #flank file read
w = open('Flank2.txt','w') #file write

f.readline()
ref = f.readlines()

def diff(ref_st,ref_end,flank_st,flank_end):
    
    if((ref_st <= flank_st and flank_st <= ref_end) or (ref_st <= flank_end and flank_end <= ref_end)):
        return 0
    
    if((ref_st >= flank_st and flank_end >= ref_end) or (ref_st <= flank_st and flank_end <= ref_end)):
        return 0
    
    if(ref_st > flank_st):
        if(ref_st - flank_end < 10000):
            return 1
        else:
            return 0
    else:
        if(flank_st - ref_end < 10000):
            return 1
        else:
            return 0


for i in flank.readlines():
    s = i.replace("\n","").replace("\r","").split("\t")
    w.write(s[0]+"\t"+s[1]+"\t"+s[2]+"\t")
    fl = 0
    for j in ref:
        k = j.replace("\r\n","").split("\t")
        
        if(s[3] == k[2] and diff(int(k[4]),int(k[5]),int(s[5]),int(s[6]))):
            w.write(k[12]+"|")
            fl = 1
            
    if(fl == 1):
        w.write("\tFlank\r\n")
    else:
        w.write("\tNo overlap\r\n")

w.close()
