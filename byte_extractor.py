import re

def extract_hex_bytes_to_text_strict(input_file, output_file):
    # Regex for matching lines starting exactly with a 4-digit hex offset followed by space
    # e.g. '0000 ' or '00a0 '
    offset_pattern = re.compile(r'^[0-9a-fA-F]{4}\s')

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if offset_pattern.match(line):
                parts = line.strip().split()
                hex_bytes = parts[1:17]
                hex_line = ' '.join(hex_bytes)
                outfile.write(hex_line + '\n')
            # else: skip lines that do not start with hex offset

    print(f"✅ Strict filtered hex bytes extracted to '{output_file}'")

# Example usage
extract_hex_bytes_to_text_strict('simulation_test.txt', 'output.txt')
