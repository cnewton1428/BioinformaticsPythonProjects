#Calculate GC Content

gene = open("BRCA1_BAP1.txt", "r")

#set values to 0
g = 0;
a = 0;
c = 0;
t = 0;

#skip first line of header
gene.readline()

for line in gene:
    line = line.lower()
    for char in line:
        if char == "g":
            g+=1
        if char == "a":
            a+=1
        if char == "c":
            c+=1
        if char == "t":
            t+=1

print ("number of g's" + str(g))
print ("number of c's" + str(c))
print ("number of a's" + str(a))
print ("number of t's" + str(t))

#0. = convert to floating point

gc = (g+c+0.) / (a+t+c+g+0.)

print ("gc content:" + str(gc))

#GC content (~0.54) is more than AT expected in homo sapiens
