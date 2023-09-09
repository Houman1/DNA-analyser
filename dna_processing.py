import logging
from dna_validity_checker import DNAValidityChecker


class DnaProcessing:

    logging.basicConfig(filename='dna_validity_checker.py', level=logging.DEBUG)

    def transcription(dna_sequence):
        '''pass in DNA sequence, will return mRNA sequence'''

        dna_validity_checker = DNAValidityChecker()

        if dna_validity_checker.is_valid(dna_sequence):

            mrna_sequence = dna_sequence.replace("T", "U")
            logging.info(f"mRNA sequence: {mrna_sequence}")

            return mrna_sequence