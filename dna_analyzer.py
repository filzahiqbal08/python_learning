#ask user to input a DNA sequence and store it
user_sequence = input("Enter the nucleotide sequence: ")
#counts how many 'A' there are in the DNA sequence
count_A = user_sequence.count('A')
#counts how many 'T' there are in the DNA sequence
count_T = user_sequence.count("T")
#counts how many 'C' there are in the DNA sequence
count_C = user_sequence.count('C')
#counts how many 'G' there are in the DNA sequence
count_G = user_sequence.count("G")
#counts ammount of "G" and "C" in sequence divides it by total amount of nucleotides in sequence, multiplies by 100 and rounds down to 1 decimal
gc_content = round((count_G + count_C) / len(user_sequence) * 100, 1)
 #analyzes if the elements of set "user_sequence" is contained within the other set             
if set(user_sequence).issubset({"A", "T", "C", "G"}):
    #prints the length of the DNA sequence
    print("Your sequence is", len(user_sequence), "nuceleotides long.")
    #prints the count of A from the variable count_A
    print("There are", count_A, "A in your sequence.")
    #prints the count of T from count_T
    print("There are", count_T, "T in your sequence.")
    #prints the count of C from count_C
    print("There are", count_C, "C in your sequence.")
    #prints the count of G from count_G
    print("There are", count_G, "G in your sequence.")
    #prints GC content as a percent
    print("There is", (gc_content), "%" "GC in your sequence.")
    #checks if GC content in DNA sequence is > 50% and prints High GC
    if gc_content > 50.0:
        print("High GC")
    #checks another condiition if previous condiition is false to see if GC content in DNA sequence == 50% and prints Balanced GC
    elif gc_content == 50.0:
        print("Balanced GC")
    #checks last condition if previous were false and prints Low GC
    else:
        print("Low GC")

#given that the previous if statement was false because subset a did not contain the elements of subset b, prints error
else:
    print("Error:Invalid sequence")


