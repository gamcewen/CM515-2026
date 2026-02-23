### This script is where you should input your solutions in the designated areas only. There is a space at the bottom of the file to do your own code testing.
### Run grading.py to grade your assignment. You may run this script as many times as you'd like; I will evaluate your submissions myself with this exact script.

# This dictionary of RNA codons to amino acid symbols may be useful for some exercises!
codon_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

# You will likely need this package for list_files()
import os


### PART 1: ANALYZING SEQUENCES ###

# This function determines whether two string sequences are equivalent: returns True if they are equivalent, and False if they are not.
def check_equivalence(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    # Takes as input two strings
    # If they are equivalent, returns True
    # If they are not equivalent, returns False
    if seq_1 == seq_2:
        are_equivalent = True
    else:
        are_equivalent = False
    
    return are_equivalent

    ### YOUR CODE ABOVE HERE ###

# This function takes two string sequences and returns a list of the positions where they differ. Returns an empty list if the sequences are identical.
# You may assume both sequences are the same length.
def get_variants(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    # Takes as input two strings
    # Returns a list of positions where they differ
    # If they are equivalent, returns an empty list
    variant_list = []
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            variant_list.append(i)

    ### YOUR CODE ABOVE HERE ###

    return variant_list

# This function takes a string sequence and returns the type of sequence it is: DNA, RNA, protein, or unknown.
# Note: Technically, there are some sequences that could match multiple types. You can ignore these edge cases for this exercise.
def get_seq_type(seq):

    # List of DNA nucleotide one-letter codes, RNA nucleotide one-letter codes, and amino acid one-letter codes
    
    dna_chars = ["A", "G", "C", "T"]
    rna_chars = ["A", "G", "C", "U"]
    aa_chars = codon_dict.values()

    ### YOUR CODE BELOW HERE ###
    # If all characters in a string are DNA one-letter codes, returns 'DNA'
    # If all characters in a string are RNA one-letter codes, returns 'RNA'
    # If all characters in a string are amino acid one-letter codes, returns 'protein'
    # If string contains characters that are not DNA, RNA, or amino acid one-letter codes, returns 'unknown'
    # Warning: Will default to 'DNA' if it is RNA or protein that contains only DNA one-letter codes
    if all(i in dna_chars for i in seq):
        seq_type = "DNA"
    elif all(i in rna_chars for i in seq):
        seq_type = "RNA"
    elif all(i in aa_chars for i in seq):
        seq_type = "protein"
    else:
        seq_type = "unknown"

    ### YOUR CODE ABOVE HERE ###

    return seq_type

# This function has been written for you. You may use it in type_of_point_mutation() if you want to!
def split_rna_to_codons(rna_seq):
    codon_list = []
    for i in range(0, len(rna_seq), 3):
        codon_list.append(rna_seq[i:i+3])
    return codon_list

# This function takes two RNA string sequences and returns the type of point mutation that differentiates them: silent, missense, or nonsense. 
# Return "none" if the sequences are identical. You can assume there is at most one point mutation between the two sequences, and that the sequences are of equal length.
# Hint: You can use the functions you already wrote above, and/or get_protein_seq() from last week's assignment 2.

def get_protein_seq(list_of_codons):

    ### YOUR CODE BELOW HERE ###

    # creates an empty list to store the output
    output_list = []
    for codon in list_of_codons:
         # check to see if each codon is in the codon dictionary, if it is add the corresponding one letter AA code to the ouput list
        if codon in codon_dict:
            output_list.append(codon_dict[codon])
        # check to see if the codon is not in the codon dictionary, if it is not, add 'none' to the output list
        else:
            output_list.append('none')
    return output_list

def type_of_point_mutation(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    # This function takes two RNA string sequences and returns the type of point mutation that differentiates them
    # If RNA sequences are identical, returns 'none'
    # If RNA sequences are not identical, but protein sequences are identical, returns 'silent'
    # If RNA sequences and protein sequences are not identical, but there are no premature stop codons, returns missense
    # If there are premature stop codons, returns nonsense
    protein_1 = get_protein_seq(split_rna_to_codons(seq_1))
    protein_2 = get_protein_seq(split_rna_to_codons(seq_2))
    if seq_1 == seq_2:
        mutation_type = "none"
    elif seq_1 != seq_2 and protein_1 == protein_2:
        mutation_type = "silent"
    elif seq_1 != seq_2 and protein_1 != protein_2 and all(str(i).isalpha() for i in protein_1) and all(str(i).isalpha() for i in protein_2):
        mutation_type = "missense"
    elif "*" in protein_1 or "*" in protein_2:
        mutation_type = "nonsense"

    ### YOUR CODE ABOVE HERE ###

    return mutation_type


### PART 2: FILES ###

# This function returns the list of files in the current directory.
def list_files():

    ### YOUR CODE BELOW HERE ###

    # This function looks in the current directory and returns the list of files present
    current_directory = os.getcwd()
    files_list = os.listdir(current_directory)

    ### YOUR CODE ABOVE HERE ###

    return files_list

# This function returns a list of all the header lines (start with '>') in a given FASTA file.
def extract_fasta_headers(filepath):

   ### YOUR CODE BELOW HERE ###

    # This function takes as input the file path to a FASTA file and returns a list of the header lines
    # Header lines are designated by starting with '>'
    header_list = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('>'):
                header_list.append(line.strip())

    ### YOUR CODE ABOVE HERE ###

    return header_list


### TEST YOUR CODE DOWN HERE (IF YOU WANT TO) ###