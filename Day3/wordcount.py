words = 0
chars = 0
lines = 0

with open('file.txt', 'r') as f:
    for line in f:
        list = line.split()
        lines += 1
        words += len(list)
        chars += len(line)

print ("no of words: ", words)
print ("no of lines: ", lines)
print ("no of characters: ", chars)