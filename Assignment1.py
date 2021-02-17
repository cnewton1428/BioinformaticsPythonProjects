#Task 1. Using print function print exact statement as stated in Question 1

print("What is the difference between \na' and " + 'a"? Or between a" and ' + 'a\\"?'+ "\n\nOne is what we see when we're typing our program. \nThe other is what appears on the " + "console.")




#Task 2. Perform Transcription by transcribing DNA to RNA. Replace all T's to U's

DNA = "ATGCTG"
RNA = DNA.replace("T", "U")
print("The DNA sequence is: ", DNA, "\nThe RNA sequence is: ", RNA)




#Task 3. Calculate AT and GC content in a given sequence.
DNA = "ATGTACATAGCGAACGCTTTGCTATCATTATATTGA"
length = len(DNA)

#Find the total of each nucleotide
a_count = DNA.count('A')
t_count = DNA.count('T')
g_count = DNA.count('G')
c_count = DNA.count('C')

#For total AT content 1st add both A and T counts then divide by total number of nucleotides in sequence
at_count = ((a_count + t_count)/length)*100

#For total GC content 1st add both G and C counts then divide by total number of nucleotides in sequence
gc_count = ((g_count + c_count)/length)*100

#print each GC content and AT content using percentage 
print("The GC content of the DNA sequence given is: {:.1f}".format(gc_count) +"%" + "\nThe AT content of the DNA sequence given is: {:.1f}".format(at_count) + "%")
