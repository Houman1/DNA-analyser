import logging


class DnaValidityChecker:

    logging.basicConfig(filename='dna_validity_checker.py', level=logging.DEBUG)

    def is_valid(self, dna_string):
        '''Checks DNA string to see if all bases in the sequence are valid'''

        dna_string_formatted = dna_string.replace(" ", "").upper()

        valid_dna = ["A", "T", "C", "G"]

        a_count, t_count, c_count, g_count = self.count_bases(dna_string_formatted)

        if all(base in valid_dna for base in dna_string):
            logging.info("DNA sequence is valid")
            return True
        else:
            logging.error("DNA sequence is invalid")
            return False

    def count_bases(self, dna_string):

        a_count = dna_string.count('A')
        t_count = dna_string.count('T')
        c_count = dna_string.count('C')
        g_count = dna_string.count('G')

        logging.info(
            f"DNA sequence length is: {len(dna_string)}\n"
            f"Counts for DNA bases:\n"
            f"A:{a_count}\n"
            f"T:{t_count}\n"
            f"C:{c_count}\n"
            f"G:{g_count}")

        return a_count, t_count, c_count, g_count
