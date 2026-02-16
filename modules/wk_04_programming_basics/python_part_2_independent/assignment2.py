### This script is where you should input your solutions in the designated areas only. There is a space at the bottom of the file to do your own code testing.
### Run grading.py to grade your assignment. You may run this script as many times as you'd like; I will grade your submissions myself with this exact script.

# This function takes an input list and an item, and adds the item to the beginning of the list.
def add_to_list(input_list, item):

    ### YOUR CODE BELOW HERE ###

    input_list.insert(0, item)

    ### YOUR CODE ABOVE HERE ###
    
    return input_list


# This function takes two input lists and combines them.
def merge_lists(list_1, list_2):

    ### YOUR CODE BELOW HERE ###

    merged_list = list_1 + list_2

    ### YOUR CODE ABOVE HERE ###

    return merged_list


# This function takes an input list and an item, and removes all copies of the item from the list.
def remove_from_list(input_list, item):

    ### YOUR CODE BELOW HERE ###

    while item in input_list:
        input_list.remove(item)

    ### YOUR CODE ABOVE HERE ###

    return input_list


# This function takes a numerical grade (e.g. 75.4), and returns True or False depending on whether that grade will earn a B (between 80 and 90)
def check_if_b_grade(grade):

    ### YOUR CODE BELOW HERE ###

    if grade >= 80 and grade < 90:
        is_b_grade = True
    else:
        is_b_grade = False

    ### YOUR CODE ABOVE HERE ###

    return is_b_grade


# This function takes a list of RNA codons, and uses a dictionary to return a list of the amino acid translations. If any codon is invalid (aka, not in the dictionary), return an empty list.
def get_protein_seq(list_of_codons):

    codon_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    ### YOUR CODE BELOW HERE ###

    # creates an empty list to store the output
    output_list = []
    for codon in list_of_codons:
         # check to see if each codon is in the codon dictionary, if it is add the corresponding one letter AA code to the ouput list
        if codon in codon_dict:
            output_list.append(codon_dict[codon])
        # check to see if the codon is not in the codon dictionary, if it is not, return an empty list
        else:
            return []
   

    ### YOUR CODE ABOVE HERE ###
    
    return output_list


# This function reads in a text file, and counts how many times the word of interest appears.
def count_word_in_file(file_path, word_of_interest):

    ### YOUR CODE BELOW HERE ###

    # starts a counter at 0
    word_count = 0
    # opens the file at the designated file path
    with open(file_path, "r") as f:
        for line in f:
            # splits each line of the file into words
            words = line.split()
            for word in words:
                # removes punctuation from the end of each word
                word = word.strip(".,!?;:\"()")
                # converts each word to lowercase
                word = word.lower()
                # checks to see if each word is the word of interest, if it is, add 1 to the counter
                if word == word_of_interest:
                    word_count += 1
    # returns the final count of the word of interest in the file
    return word_count

    ### YOUR CODE ABOVE HERE ###


# This function takes a list of 3 column names, and a list of data for each column (each data list is the same length), then outputs a correctly-formatted CSV file "data.csv".
def create_data_file(column_names_list, column1_data, column2_data, column3_data):

    ### YOUR CODE BELOW HERE ###

     # imports the csv module
    import csv
    # opens the file data.csv in write mode
    with open("data.csv", "w", newline="") as data_file:
        # creates a csv writer object
        writer = csv.writer(data_file)
        # writes the column names in column_names_list to the first row of the file
        writer.writerow(column_names_list)
        # writes the data in column1_data, column2_data, and column3_data to the file
        # column1_data, column2_data, and column3_data are the same length, so the length of column1_data is used to determine how many rows to write to the file
        for i in range(len(column1_data)):
            writer.writerow([column1_data[i], column2_data[i], column3_data[i]])

    ### YOUR CODE ABOVE HERE ###

# This function reads in a CSV file, "file2.csv", and outputs two new files: tav.csv contains ONLY entries with "Tav" as the technician, 
# and andre.csv contains ONLY antries with "Andre" as the technician. Look at file2.csv before writing code!
def filter_data():

    ### YOUR CODE BELOW HERE ###

    # imports the csv module
    import csv
    # opens the file file2.csv in read mode
    with open("file2.csv", "r") as input_file:
        # creates a csv reader object for file2.csv
        reader = csv.reader(input_file)
        # reads the first row of the file and stores it in a variable called headers
        headers = next(reader)
        # opens the file tav.csv in write mode
        with open("tav.csv", "w", newline="") as output_file1, open("andre.csv", "w", newline="") as output_file2:
            # creates a csv writer object for tav.csv
            writer1 = csv.writer(output_file1)
            # creates a csv writer object for andre.csv
            writer2 = csv.writer(output_file2)
            # writes the headers to the first row of tav.csv
            writer1.writerow(headers)
            # writes the headers to the first row of andre.csv
            writer2.writerow(headers)
            # reads through the rest of the rows in the file
            for row in reader:
                # if the value in the fourth column of the row is "Tav", write the row to tav.csv
                if row[3] == "Tav":
                    writer1.writerow(row)
                # if the value in the fourth column of the row is "Andre", write the row to andre.csv
                elif row[3] == "Andre":
                    writer2.writerow(row)

    ### YOUR CODE ABOVE HERE ###



### TEST YOUR CODE DOWN HERE (IF YOU WANT TO) ###
