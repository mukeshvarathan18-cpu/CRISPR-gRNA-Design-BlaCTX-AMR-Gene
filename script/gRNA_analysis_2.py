# gRNA Analysis - BlaCTX CRISPR Project
# calculating GC content and reading gRNA results

# GC content calculator
def gc_content(sequence):
    sequence = sequence.upper()
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)
    gc = (g + c) / total * 100
    return round(gc, 2)

# my gRNA sequences from CHOPCHOP
grnas = {
    "Cas9_gRNA1":  "ACGCTGCGTAATCTGACGCT",
    "Cas9_gRNA2":  "CATTGTCCGGCGAACGCCCA",
    "Cas9_gRNA3":  "GCTAAGTTCCGCCAGCGTCA",
    "Cas12_gRNA1": "TTCGCCGGACAATGTTAATGATGATGGC",
    "Cas12_gRNA2": "TTCGCAAATTGTCTATCGCGCAGACGAG",
    "Cas12_gRNA3": "TTCTTAATTTCAACACGCTGGTTTAAAA",
    "Cas13_gRNA1": "AGCAAAAGCTGGAAGCGTTGGAGAAAAG",
    "Cas13_gRNA2": "CAAAAGCTGGAAGCGTTGGAGAAAAGCA",
    "Cas13_gRNA3": "AAAAGCTGGAAGCGTTGGAGAAAAGCAC",
}

print("=== GC Content of all gRNAs ===")
print()
for name, seq in grnas.items():
    gc = gc_content(seq)
    if gc < 40:
        status = "low"
    elif gc > 70:
        status = "high"
    else:
        status = "optimal"
    print(f"{name} | GC: {gc}% | {status}")
