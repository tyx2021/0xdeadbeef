# Define a function to process the file
def process_file(input_filename, output_filename):
    # Open the input file in read mode
    with open(input_filename, 'r', encoding='utf-8') as infile:
        # Open the output file in write mode
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            # Read each character from the input file
            for char in infile.read():
                # Check if the character is an em space (Unicode \u2003)
                if char == '\u2003':  # Em space character
                    outfile.write('0')  # Write '0' for em space
                else:
                    outfile.write('1')  # Write '1' for all other characters

# Example usage
input_filename = 'whitepages.txt'  # Replace with your input file path
output_filename = 'output.txt'  # Replace with your desired output file path

process_file(input_filename, output_filename)

print("File processing complete. Output written to", output_filename)
