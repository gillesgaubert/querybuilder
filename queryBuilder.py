"""
parser for input  query in dataloader
input file : extract.txt
output file(s) : out0.txt, out1.txt, ...
2 arguments in command line : maxBuffer et idLength, par exemple :
python queryBuilder.py 15000 15
15000 et 15 are default if absents
author : gilles gaubert
"""

import os    
import sys
    
if (len(sys.argv)==3) :
    MAXBUFFER=int(sys.argv[1])   #15000 max size buffer to query in dataloader
    IDLENGTH=int(sys.argv[2])    #15 size of id in nb of characters
else:
    MAXBUFFER=15000
    IDLENGTH=15

os.chdir("./")
myFile = open("extract.txt", "r")
content = myFile.read()

# treatment
bufferSize=MAXBUFFER-MAXBUFFER%(IDLENGTH+3)    # to account for ' and ,
print("Adjusted buffer size to account for separators = "+str(bufferSize))
formatedContent=""
for c in content:
    if (c=="\n"):
        formatedContent=formatedContent+"\',\'"
    else:
        formatedContent=formatedContent+c

formatedContent="\'"+formatedContent+"\'"
sizeFormatedContent=len(formatedContent)
print("size formated content = "+str(sizeFormatedContent))
cursor=0
resizedContent=[]
if (sizeFormatedContent<MAXBUFFER):
    # the easy case
    resizedContent.append(formatedContent)
    print("Only one slice !")
else:            
    # more than one slice
    residualSize=sizeFormatedContent
    while (residualSize>bufferSize):
        part=formatedContent[cursor:cursor+bufferSize]
        cursor=cursor+bufferSize
        residualSize=residualSize-bufferSize
        resizedContent.append(part)
    part=formatedContent[cursor:]
    resizedContent.append(part)
    for cont in resizedContent :
        print("slice size = "+str(len(cont)))
    print("number of slices = "+str(len(resizedContent)))
        
# saving output
os.chdir("./out/")
for i in range (0,len(resizedContent)):
    outputFileName="out"+str(i)+".txt"
    print("creation : "+outputFileName)
    
    outputFile = open(outputFileName, "w")
    outputFile.write(resizedContent[i])
    outputFile.close()

# closing input
myFile.close()
