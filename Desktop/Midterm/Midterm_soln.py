# Midterm Solutions 

#Q1
print("Q1")
print("-------------------------------------------------------------")

#Open and read sequence file
genomicFile = open("genomic_dna.txt")
genomicSeq = genomicFile.read()
#Extrac out coding and non coding
cds1 = genomicSeq[0:63]
intron = genomicSeq[63:90]
cds2 = genomicSeq[90:]
#Write results to file
codingFile = open("coding.txt", "w")
nonCodingFile = open("Non_Coding.txt", "w")
codingFile.write(cds1+cds2)
nonCodingFile.write(intron)
#close all files
genomicFile.close()
codingFile.close()
nonCodingFile.close()

print("Reults sent to file")

#Q2
print("Q2")
print("-------------------------------------------------------------")
lenSeq = len(genomicSeq)
lenCoding = len(cds1) + len(cds2)
percentCoding = (lenCoding/lenSeq)*100
print("Percent of seqeunce that is coding is %.2f" %percentCoding)

#Q3
print("Q3")
print("-------------------------------------------------------------")
#open files
accnFile = open("AccessionNumbers.txt")
seqFile = open("Sequences.txt")
#read data
accn = accnFile.readlines()
sequences = seqFile.readlines()

#output to files
i = 0
for i in range(len(accn)):
    f = open(accn[i].strip()+".txt", "w")
    f.write(">" + accn[i] + sequences[i].upper().replace('-', ''))
    f.close()
    i = i + 1
    
print("Reults sent to file")
    

#Q4
print("Q4")
print("-------------------------------------------------------------")
dna1 = input("Enter seq1: ").upper()
dna2 = input("Enter seq2: ").upper()


#Reverse dna2
dna2 = dna2[::-1]

#Complement for dna2
temp1 = dna2.replace('A','t')
temp2 = temp1.replace('T','a')
temp3 = temp2.replace('C','g')
temp4 = temp3.replace('G','c')

dna2 = temp4.upper()

#Compare the two
if dna1 == dna2:
    print("Reverse compliments!")
else:
    print("Not reverse compliments!")


#Q5
print("Q5")
print("-------------------------------------------------------------")

file = open("seq.txt")
fileContents = file.read()

revContents = fileContents[::-1]

print(revContents)

#Q6
print("Q6")
print("-------------------------------------------------------------")

#user input for population size
pop = int(input("Enter population size: "))
while pop < 2:
    pop = int(input("Population size should be greater than 2, please try again: "))

#user input for percent increase
perIncrease = float(input("Enter percent daily population increase: "))
while perIncrease < 0:
    perIncrease = float(input("Percent increase can not be < 0, please try again: "))

#user for number of days
days = int(input("Enter number of days population will be multiplying: "))
while days < 1:
    days = int(input("Number of days can not be less than 1, please try again: "))

#Table header
print("Days \t\t Number of Organisms")
print("_____________________________________")

#Generate Table
for i in range(days):
    print(str(i + 1) + "\t\t" + str(pop))
    pop = pop + (pop * (perIncrease/100))
    

#Q7
print("Q7")
print("-------------------------------------------------------------")

lines = []
string = input("Enter a line of text: ");
while string != "quit": 
    lines.append(string)
    string = input("Enter another line of text: ");

print("Unsorted lines")
for i in lines:
    print(i)

#Sort
print("\n\nSorted lines")
lines.sort()
for i in lines:
    print(i)


#Q8
print("Q8")
print("-------------------------------------------------------------")

totalLines = len(lines)
print ("Total number of lines is " + str(totalLines))

if totalLines >= 4:
    print("2nd line in soted list is: " + lines[1])
    print("3rd line in soted list is: " + lines[2])
    print("4th line in soted list is: " + lines[3])
else:
    print("Number of lines less than 4.")



#Q9
print("Q9")
print("-------------------------------------------------------------")

string = input("Enter a series of numbers separated by spaces: ")
#Use split to separate the string into a list, space is the delimiter
nums = string.split(" ")
total = 0
for i in nums:
    total = total + int(i)
    
avg = total / len(nums)
print("Average of numbers is: " + str(avg))


#Q10
print("Q10")
print("-------------------------------------------------------------")

#Gather inputs
totalCalories = float(input("Enter total # of calories for food: "))
fatGrams = float(input("Enter # of fat grams in food: "))

#Calculate Calories from fat
fatCalories = fatGrams * 9
#Calculate Percent calories from fat
perCalFat = (fatCalories/totalCalories)*100

#Check results
if fatCalories  > totalCalories:
    print("Invalid data, calories from fat can NOT exceed total calories. Try again.")
else:
    if perCalFat < 30:
        print("Food is low in fat.")
    else:
        print("Food is high in fat.")











