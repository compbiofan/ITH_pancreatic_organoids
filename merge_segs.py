from sys import argv


def main(infile, outfile):
    f = open(infile, "r")
    outFile = open(outfile, "w")
    line = f.readline()
    line = line.rstrip().split(",")
    outFile.write("CHROM\tSTART\tEND")
    for cluster in line[4:]:
        outFile.write("\t" + cluster)
    outFile.write("\n")
    line = f.readline()
    #print(line)
    temp = line.rstrip().split(",")[1:]
    #print(temp)
    if (temp[0] == "chrX"):
        temp[0] = "chr23"
    if(temp[0] == "chrY"):
        temp[0] = "chr24"
    prevChrom = int(temp[0][3:])
    prevStart = int(temp[1])
    prevEnd = int(temp[2])
    prevCNs = []
    res = []
    for cn in temp[3:]:
        cn = float(cn)
        prevCNs.append(round(cn))
    for line in f:
        temp = line.rstrip().split(",")[1:]
        #print(temp)
        if (temp[0] == "chrX"):
            temp[0] = "chr23"
        if(temp[0] == "chrY"):
            temp[0] = "chr24"
        curChrom = int(temp[0][3:])
        curStart = int(temp[1])
        curEnd = int(temp[2])
        curCNs = []
        for cn in temp[3:]:
            cn = float(cn)
            curCNs.append(round(cn))
        if(curChrom != prevChrom):
            temp = [prevChrom, prevStart, prevEnd]
            #outFile.write(str(prevChrom) + "\t" + str(prevStart) + "\t" + str(prevEnd))
            for cn in prevCNs:
                #outFile.write("\t" + str(cn))
                temp.append(cn)
            #outFile.write("\n")
            res.append(temp)
            prevChrom = curChrom
            prevStart = curStart
            prevEnd = curEnd
            prevCNs = curCNs
            continue
        flag = False
        if(curStart - 1 == prevEnd):
            flag = True
            for i in range(len(curCNs)):
                if(curCNs[i] != prevCNs[i]):
                    flag = False
                    break
        if(flag):
                prevEnd = curEnd
                prevCNs = curCNs
        else:
            #outFile.write(str(prevChrom) + "\t" + str(prevStart) + "\t" + str(prevEnd))
            temp = [prevChrom, prevStart, prevEnd]
            for cn in prevCNs:
                #outFile.write("\t" + str(cn))
                temp.append(cn)
            #outFile.write("\n")
            res.append(temp)
            prevChrom = curChrom
            prevStart = curStart
            prevEnd = curEnd
            prevCNs = curCNs
    #outFile.write(str(prevChrom) + "\t" + str(prevStart) + "\t" + str(prevEnd))
    temp = [prevChrom, prevStart, prevEnd]
    for cn in prevCNs:
        #outFile.write("\t" + str(cn))
        temp.append(cn)
    res.append(temp)
    #print(res)
    for seg in res:
        flag = True
        prev = seg[3]
        #print(prev, end = " ")
        for i in seg[4:]:
            #print(i, end=" ")
            if prev != i:
                
                flag = False
                break
        if not flag:
            for i in seg:
                outFile.write(str(i) + "\t")
            outFile.write("\n")
        #print()
if __name__ == "__main__":
    main(argv[1], argv[2])
                

