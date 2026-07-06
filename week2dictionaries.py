codon_table = {"ATG": "Methionine", "TAA": "Stop"}
if "ATG" in codon_table:
    print("Found:", codon_table["ATG"])
else:
    print("Not found")