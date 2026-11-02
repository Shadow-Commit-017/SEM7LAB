# Step 1: Input DNA sequence
dna = input("Enter DNA sequence: ").upper()

# Step 2: Validate DNA sequence
if not dna or not all(b in "ATGC" for b in dna):
    print("Invalid DNA sequence")

else:
    print("\nOriginal DNA:", dna)

    # Step 3: Sequence Manipulation

    # Complementary sequence
    complement = dna.translate(str.maketrans("ATGC", "TACG"))
    print("Complementary Sequence:", complement)

    # Reverse sequence
    reverse = dna[::-1]
    print("Reverse Sequence:", reverse)

    # Reverse complement
    print("Reverse Complement:", complement[::-1])

    # Step 4: Calculate GC Content
    gc = dna.count('G') + dna.count('C')
    gc_content = (gc / len(dna)) * 100

    print("GC Content:", round(gc_content, 2), "%")

    # Step 5: Find Motif
    motif = input("\nEnter motif: ").upper()

    if not motif or not all(b in "ATGC" for b in motif):
        print("Invalid motif")
    elif motif in dna:
        print("Motif found at position:", dna.find(motif) + 1)
    else:
        print("Motif not found")

    # Step 6: Identify Coding Region (ORF)
    start = dna.find("ATG")

    if start != -1:
        found = False

        for i in range(start + 3, len(dna) - 2, 3):
            if dna[i:i+3] in ["TAA", "TAG", "TGA"]:
                print("\nCoding Region:", dna[start:i+3])
                found = True
                break

        if not found:
            print("\nNo complete coding region found")
    else:
        print("\nStart codon not found")
