import re

# Define sequence 1
seq1 = 'PASTE_YOUR_REFERENCE_SEQUENCE_HERE'

# Specify the path to your file
file_path = 'SPECIFY_THE_PATH_TO_YOUR_FILE_HERE.txt'

# Open the file and read its content
with open(file_path, 'r') as file:
    file_content = file.read()

# Use regular expressions to extract name and sequence
pattern = re.compile(r'>([^\n]+)\n([ACGTURYKMSWBDHVNacgturykmswbdhvn\n]+)')

matches = pattern.findall(file_content)

# Process and save sequences
with open('output_sequences.txt', 'w') as output_file:
    for name, seq2 in matches:
        processed_sequence = ''
        min_length = min(len(seq1), len(seq2))

        for i in range(min_length):
            if seq2[i] == "N": 
                processed_sequence += seq1[i]
            elif seq2[i] == "R": 
                processed_sequence += seq1[i]
            elif seq2[i] == "W": 
                processed_sequence += seq1[i]
            elif seq2[i] == "Y": 
                processed_sequence += seq1[i]
            elif seq2[i] == "M": 
                processed_sequence += seq1[i]
            elif seq2[i] == "K": 
                processed_sequence += seq1[i]
            elif seq2[i] == "S": 
                processed_sequence += seq1[i]
            elif seq2[i] == "D": 
                processed_sequence += seq1[i]
            elif seq2[i] == "V": 
                processed_sequence += seq1[i]
            elif seq2[i] == "H": 
                processed_sequence += seq1[i]
            elif seq2[i] == "B": 
                processed_sequence += seq1[i]
            elif seq2[i] == "X": 
                processed_sequence += seq1[i]
            else:
                processed_sequence += seq2[i]

        # Save the result to the output file
        output_file.write(f">{name}\n{processed_sequence}\n")

print("Sequences processed and saved in 'output_sequences.txt'")
