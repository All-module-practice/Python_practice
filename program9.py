# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    # code here
    li=[]
    for i in dna:
        if i=='A':
            li.append('T')
        elif i=='T':
            li.append('A')
        elif i=='C':
            li.append('G')
        elif i=='G':
            li.append('C')
    return "".join(li)
