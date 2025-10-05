def extract_hex_bytes_to_text(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue

            # Split line into parts
            parts = line.split()

            # Skip the first part (line number / offset)
            hex_bytes = parts[1:17]  # max 16 bytes per line

            # Join hex bytes into a line
            hex_line = ' '.join(hex_bytes)

            # Write to output
            outfile.write(hex_line + '\n')

    print(f"✅ Hex bytes extracted to '{output_file}'")

# Example usage
extract_hex_bytes_to_text('input.txt', 'output.txt')
