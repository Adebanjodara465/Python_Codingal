#opening a new file
with open('Codingal.txt', 'w') as file:
    file.write('Hello people!')
file.close()

#spliting a file into words
with open ('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("The words in the file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()       