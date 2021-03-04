#My work
#1. From file genomic_dna.txt print out to files the coding(exons saved as coding.txt) and non-coding regions(introns saved into another file called non_coding.txt)

#Read DNA sequence from file
file_name = open("genomic_dna.txt")
my_dna = file_name.read()

dna_length = len(my_dna)
print("Total DNA length "+ str(dna_length))

#Extract the DNA sequences
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:123]

#Open 2 output files 
out1 = open("coding.txt", "w")
out2 = open("non_coding.txt", "w")

#Write the 2 exon sequences to coding file and 1 intron sequence to non-coding file
out1.write(exon1 + exon2)
out2.write(intron)

file_name.close()
out1.close()
out2.close()


#2. Modify code from Q1 so it calculates what percentage of sequence is coding and display the result to screen

#Read DNA sequence from file
file_name = open("genomic_dna.txt")
my_dna = file_name.read()

#Amount of coding sequence
exon1 = my_dna[0:62]
exon2 = my_dna[90:123]

coding_length = len(exon1 +exon2)
total = len(my_dna)

print("Percentage of coding sequence :","{:.2f}".format(100* coding_length / total))


#3.From sequences.txt file which contains 3 sequences (one sequence per line) and AccessionNumbers.txt, write a program that reads in those files and produces 3 separate FASTA files. Each accession number corresponds to eqch sequence

#Take in sequence and list in upper case

def Seq(seq):
    contain = ""

    for i in seq:
        if (i.upper() in "ACTG"):
            contain += i.upper()
    return contain

#Open files
seq = open("sequences.txt")
acc = open("AccessionNumbers.txt")

#Read in one line from above files
seq_one = seq.readline()
acc_one = acc.readline()

#Till the end of the files each

while (seq_one and acc_one):
    #Use strip to remove any leading spaces at beginning and trailing spaces at end
    seq_one = Seq(seq_one.strip())
    acc_one = acc_one.strip()
    #Create file with accession number as text file
    out = open(acc_one+".txt","w")
    #Write accession number
    out.write(">"+acc_one+"\n")
    #Attach sequence
    out.write(seq_one)
    out.close()
    #Read sequence and accession number
    seq_one = seq.readline()
    acc_one = acc.readline()

seq.close()
acc.close()


#4. Write program that checks if two DNA sequences given as input by the user are reverse compliments of one another
dna = {'ins':'0'}
key = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def reverse_complement(seq):
    for k,v in dna.items():
        seq = seq.replace(k,v)
    bases = list(seq)
    bases = reversed([key.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in dna.items():
        bases = bases.replace(v,k)
    return bases

a1=input("Enter first DNA sequence ")
a1=a1.upper()
a2=input("Enter Second DNA sequence")
a2=a2.upper()

dna1=reverse_complement(a1)
print("dna1 ",dna11)
dna2=reverse_complement(dna1)
print("dna2 ",dna2)
dna3=reverse_complement(dna2)
print("dna3 ",dna3)
dna4=reverse_complement(dna3)
print("dna4 ",dna4)
if (a1==dna2 and a2==dna1):
print("yes, THEY ARE REVERSE COMPLEMENT")
else:
print("no, THEY ARE NOT REVERSE COMPLEMENT")


#5.Program that reads a file then prints in reverse order last line first using sequence.txt file
file = open("sequences.txt", "r")
for i in file:
    print(i[::-1], end = "")
print()


#6. Predict size of population of organisms
initial = float(input("Enter starting size of population :"))
while(initial<2):
    print("Starting population should be atleast 2\n")
    initial = float(input("Enter starting size of population :"))
average = float(input("Enter average percent of daily population increase :"))
while(average<0):
    print("It should not be negative\n")
    average = float(input("Enter average percent of daily population increase :"))
days = float(input("Enter number of days for multiplication :"))
while(days<1):
    print("It should not be less than 1\n")
    days = float(input("Enter number of days they will multiply :"))
print("Day of Organisms")
i=1
while(i<=days):
    print(i, initial)
    initial = initial + (average*initial/100)
    i+=1


#7. Take user entered lines and store in array
lines = []

#User enter quit program prints out with sorted lines

while True:
    line = input('Enter line: ')
    if line == 'quit':
        break
    lines.append(line)

lines.sort()

# print lines
for line in lines:
        print(line)


#8. Copy from above and change to get number of lines 
lines = []

while True:
    line = input('Enter line: ')
    if line == 'quit':
        break
    lines.append(line)

lines.sort()

# print lines
print("The number of lines are: ", len(lines))
print("Line 2 is :", lines[1])
print("Line 3 is :", lines[2])
print("Line 4 is :", lines[3])


#9. Sequence of lengths

enter = input("Enter list of sequence lengths:")

#Split string to create an array
arr = [int(a) for a in enter.split("")]
totalArr = 0

#Use for loop for sum of all sequence lengths
for i in arr:
    totalArr += i
Avg = totalArr/len(arr)
print("Average is ", Avg)


#10.Calculation of number of calories and fat in grams in food item
calories = 0
fat = 0

while True:
    calories = float(input("Enter number of calories per serving: "))
    if (calories <= 0):
        print("Number of calories must not be negative!")
    else:
        break;

while True:
    fat = float(input("Enter the number of fat in grams: "))
    if (fat <= 0 or fat*9 >calories):
        print("Input is Invalid. Number of grams of fat must not be negative and calories from fat cannot exceed total calories")
    else:
        break;

#for percentage of fat calories
percent = (9*fat/calories) * 100
if (percent <= 30):
    print("%.2f percentage of calories from fat. Food is low in fat." %percent)
else:
    print("%.2f percentage of calories from fat. This is not a low fat food." %percent)

    

