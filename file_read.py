
file_path = "Datafile.txt" 

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
