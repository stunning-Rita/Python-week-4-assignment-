# File Handling & Exception Handling Program

def modify_content(line):
    """
    Modify a line of text.
    Example modification: convert to uppercase and add line numbers.
    """
    return line.upper()  # You can change this to any modification you like

def main():
    try:
        # Ask user for input file
        input_file = input("Enter the name of the file to read: ")

        # Open input file safely
        with open(input_file, "r") as infile:
            lines = infile.readlines()

        # Modify lines
        modified_lines = [modify_content(line) for line in lines]

        # Write modified lines to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content has been written to '{output_file}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
