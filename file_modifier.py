def read_and_modify_file(input_file, output_file):
    """
    Reads content from input file, modifies it, and writes to output file
    """
    try:
        # Read from input file
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify content (example modifications)
        modified_content = []
        for line_number, line in enumerate(content, 1):
            # Add line numbers and convert to uppercase
            modified_line = f"{line_number}. {line.strip().upper()}\n"
            modified_content.append(modified_line)

        # Write to output file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        return True

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    # File paths
    input_file = "sample.txt"
    output_file = "modified_sample.txt"

    # Create sample input file
    sample_text = """Hello, this is a sample file.
This is line 2 of the file.
Python is awesome!
File handling is fun."""

    # Write sample content to input file
    with open(input_file, 'w') as file:
        file.write(sample_text)

    print(f"Reading from '{input_file}'...")
    if read_and_modify_file(input_file, output_file):
        print(f"Successfully modified and saved to '{output_file}'!")
        
        # Display the modified content
        print("\nModified content:")
        print("-" * 40)
        with open(output_file, 'r') as file:
            print(file.read())

if __name__ == "__main__":
    main()