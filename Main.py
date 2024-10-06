#merging two files
with open('Food.txt') as file:
    data1 = file.read(6)
    
#opening the second file
with open('Plants.txt') as file:
     data2 = file.read(4)
     
#opening the last file
with open('Baby.txt') as file:
    data3 = file.read() 
    
#begin the merge...
data1 += "\n"  
data1 += data2
data1 +="\n"
data1 += data3

print("The result of the merge.....")  

file = open('FBP.txt', 'w') 
file.write(data1)
file.close()

print(data1)    