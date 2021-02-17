#Task 1 With the amino acid sequence of polypeptides: Phe, Val, Asn, Gln, His, Leu, Cys, Gly, Ser:

#a. Define array that contains the amino acids in right order and print in one line

Amino = ["Phe", "Val", "Asn", "Gln", "His", "Leu", "Cys", "Gly", "Ser"]
print(Amino)

#b.Determine number of amino acids in polypeptide and print

print("The number of amino acids in polypeptide is: ", len(Amino))

#c. Add amino acid His to the end of the polypeptide and print

Amino.append("His")
print(Amino)

#d. Ask user input for number for position of amino acid in polypeptide sequence and print corresponding amino acid for the number provided by user
num = int(input("Enter a number between 1 and 9 for amino acid in the polypeptide sequence: "))
print("The Amino Acid at position", num, "is " + Amino[num-1])

#e. Create an inversion: get two positions in sequence from user and invert the sequence of amino acids between them.
#If user enters 3 and then 6, the program should replace Asn, Gln, His, Leu with Leu, His, Gln, Asn. Print array before and after inversion
print("Enter start of your inversion, a number from 1 to ", len(Amino) , ": ")
start = int(input())
print("Enter end of inversion, starting from " + str(start) + " to" , len(Amino) , ": ")
end = int(input())
print("Amino Acid sequence before inversion " + str(Amino))

#For Inversion purposes create another array
AminoAA = Amino[(start-1):end]

#Reverse AminoAA array
AminoAA.reverse()

#Amino Acid Sequence after inversion
Amino = Amino[0:(start-1)] + AminoAA + Amino[end:]
print("Amino Acid polypeptide sequence after inversion " + str(Amino))

#Task 2 print corresponding amino acid after asking for user input
Target = ["Trp", "Arg", "Liu", "Ilu", "Asp"]
n = int(input("Enter a number from 1 to " + str(len(Target))))
if n > len(Target) or n< 1:
    print("Error not in range. Please give a number between 1 and " + str(len(Target)))
else:
    print("The Amino acid at position ", n ,"is", Target[n-1])


#Task 3
DNA = ["C", "C", "G", "T", "A", "A", "C", "G", "C"]

#a Add a T to the end of the array and print
DNA.append("T")
print("The updated sequence after adding a T to the end of the array is ", DNA)

#b. Remove 1st element of array and print
del DNA[0]
print("The updated sequence after removing the 1st element of array is ", DNA)

#c. Add T to the beginning of the array and print
DNA.insert(0, "T")
print("The updated sequence after adding T to the beginning of array is ", DNA)
