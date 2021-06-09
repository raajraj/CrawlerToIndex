f = open('query.txt')
line = f.readline()

ms = "max_score"
id = "_id"
index = []

while line:
    if(ms in line):
        line = line.split()
        ms = line[2]
    if(id in line):
        line = line.split()
        index.append(line[2])
    line = f.readline()

print("Max Score: " + ms)
print("ID'S: " + str(index))
