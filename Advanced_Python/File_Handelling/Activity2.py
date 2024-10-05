#create a new file
new_file = open('New_file.txt', 'x') #x is used to make a new file
new_file.close()

#checking if the file exists
import os
print("Checking if the file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")  
    
#creating a real file if it dosen't exist
my_file = open("my_file.txt", 'w')  
my_file.write("Hi, I am a little doggo")
my_file.close() 

#delete the Codingal file
os.remove('Codingal2.txt')  

#delete the folder
os.rmdir("MyFolder") 
