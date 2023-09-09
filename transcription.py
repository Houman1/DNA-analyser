


class Transcription():

#Transcribe DNA
def transcribe_DNA(dna_sequence):
    '''pass in DNA sequence, will return mRNA sequence'''

    #pass it through the function that it checks the DNA seq only has ACGT and removes spaces then run following code.
    dna_sequence = dna_sequence.replace("T","U")
    print(dna_sequence)