def analyze_gene(sequence):
    print("Sequence:", sequence)
    length = len(sequence)
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    GC = (sequence.count("G") + sequence.count("C")) / length * 100
    print("Length:", length)
    print("A count:", a)
    print("T count:", t)
    print("G count:", g)
    print("C count:", c)
    print("GC content:", GC, "%")
    if GC > 50.0:
        print("High")
    else:
        print("low")
    print("---")


genes = ["ATGCGCTG", "ATATAT", "CGTGATGCTT", "TTTTA", "GCGC"]
for gene in genes:
    analyze_gene(gene)


        
