def analyze_gene(sequence)
    length = len(sequence)
    gc = (sequence.count("G)") + sequence.count("C"))/length * 100
    print("Sequence:", sequence)
    print("Length:", length)
    print("GC content:", gc, "%")
    print("---")
genes = ["ATCGGCTAGCTA", "GCGCGCGC", "ATATATATAT"]
for gene in genes: 
    analyze_gene(gene)