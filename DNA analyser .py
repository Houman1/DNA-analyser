

#count DNA bases

def count_bases():
    DNA_string = input("Please enter your DNA string:").upper()
    DNA_string = DNA_string.replace(" ", "")


    valid_DNA = ["A","T", "C", "G"]

    #Make this part a function to run for all the other functions to check whether the DNA meets the requirements
    if all(base in valid_DNA for base in DNA_string):
        print(f"DNA sequence length is: {len(DNA_string)}\nCounts for DNA bases:\nA:{DNA_string.count('A')}\nT:{DNA_string.count('T')}\nC:{DNA_string.count('C')}\nG:{DNA_string.count('G')}")
    else:
        print(f"Invalid DNA sequence")



#Transcribe DNA
def Transcribe_DNA():
    DNA_Seq = input("please input your DNA sequence:").upper()
    #pass it through the function that it checks the DNA seq only has ACGT and removes spaces then run following code.
    DNA_Seq = DNA_Seq.replace("T","U")
    print(DNA_Seq)


#Complementary DNA strand
def reverse_complement():
    DNA_Seq = input("Please input your DNA sequence:")
    complement = {"A":"T","C":"G","T":"A","G":"C"}
    return "".join([complement[base] for base in DNA_Seq[::-1]])





#Translation


def Translation():
    RNA_Seq =  input("Please input your RNA sequence:").upper()

    Amino_Acids = {
        "AUG": "M",
        "UUU":"F" , "UUC": "F",
        "UUA":"L" , "UUG":"L" ,"CUU":"L" ,"CUC":"L" ,"CUA":"L" ,"CUG":"L" ,
        "UCU":"S","UCC":"S","UCG": "S","UCA":"S","AGU":"S" ,"AGC":"S" ,
        "UAU":"Y" ,"UAC":"Y" ,
        "UGU":"C" ,"UGC":"C" ,
        "UGG":"W" ,
        "CCU":"P" ,"CCC":"P" , "CCA":"P","CCG":"P",
        "CAU":"H" , "CAC":"H",
        "CAA":"Q" , "CAG":"Q" ,
        "CGU":"R" , "CGC":"R", "CGA":"R","CGG":"R" ,"AGA":"R","AGG":"R",
        "AUU":"I" , "AUC":"I", "I": "AUA",
        "ACU":"T" , "ACC":"T","ACA":"T" , "ACG":"T" ,
        "AAU":"N" , "AAC":"N",
        "AAA":"K" , "AAG":"K",
        "GUU": "V", "GUC":"V" , "GUA":"V", "GUG":"V",
        "GCU":"A" , "GCC":"A" , "GCA":"A" , "GCG":"A",
        "GAU":"D" , "GAC":"D",
        "GAA":"E" , "GAG":"E",
        "GGU":"G" , "GGC":"G" ,"GGA":"G", "GGG":"G",
        "UAA":"stop","UAG":"stop","UGA":"stop",
    }


    protein_seq =""
    RNA_sequence = [RNA_Seq[i:i + 3] for i in range(0, len(RNA_Seq), 3)]
    for codon ,aa in Amino_Acids.items():
        for i in RNA_sequence:
            if i == codon:
                protein_seq += aa
    print (protein_seq)






#GC content


def GC_Content():

    DNA = input("Please enter your DNA sequence in FASTA format:")
    DNA= DNA.replace(" ", "")

    def GC_percentage(DNA):
        C = DNA.count("C")
        G= DNA.count("G")
        GC_content = ((C + G)/len(DNA))*100
        return GC_content

    import re

    split_DNA = list(filter(lambda  x: x!="", re.split("(\>\d+)", DNA)))
    iDNA = iter(split_DNA)
    DNA_dict = dict(zip(iDNA,iDNA))
    sorted_DNA = sorted(DNA_dict, key=DNA_dict.get)

    for k,v in sorted_DNA.items():
        print(f"{k} GC content: {GC_percentage(v)}%")







