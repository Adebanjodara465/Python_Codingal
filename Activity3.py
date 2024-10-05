#program to merge two files..

#reading data from file1
with open('Codingal.txt') as fp:
    data1 = fp.read()
    
#red the data from file 2
with open('sample.txt') as fp:
    data2 = fp.read()
    
#mergind the two files, adding the data of files 1 &2

data1 +="\n"
data1 +=data2
print("Merging the two files...")  
with open("MergeFile.txt",'w') as fp:
    fp.write(data1)      