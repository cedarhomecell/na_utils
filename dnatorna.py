"""
Convert DNA sequences to RNA.
"""
def rna(seq):
    """Convert a DNA sequence to RNA"""
    # Determine the case of the original sequence
    seq_upper = seq.isupper()

    # Convert to lower case
    seq = seq.lower()

    # Swap out 't' for 'u'
    seq = seq.replace('t','u')

    # Return the correct case
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """Convert a DNA sequence into its reverse complement as RNA"""

    # Determine the case of the original sequence
    seq_upper = seq.isupper()

    # Reverse the sequence
    seq = seq[::-1]

    # Convert to uppercase
    seq = seq.upper()

    # Comput complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('C', 'g')
    seq = seq.replace('G', 'c')

    # Return in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq
