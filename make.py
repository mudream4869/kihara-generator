fin = open("in.txt", "r")
fout = open("out.txt", "a")
for line in fin:
    if len(line) <= 3:
        fout.write(line)
