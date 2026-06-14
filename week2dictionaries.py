codon_table = {"ATG": "Methionine", "TAA": "Stop", "GCC": "Alanine", "TGG":"Tryptophan"}

for codon, amino_acid in codon_table.items():
    print(codon, "codes for", amino_acid)