def read_file():
    """
    Asks user for a filename and attempts to read and display its contents.
    Handles various file-related errors and provides retry options.
    """
    while True:
        try:
            # Get filename from user
            filename = input("\nEnter the filename to read: ")
            
            # Attempt to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
                
                # Display file contents
                print("\nFile contents:")
                print("-" * 50)
                print(content)
                print("-" * 50)
                break
                
        except FileNotFoundError:
            print(f"\nError: File '{filename}' was not found!")
            print("Make sure the file exists in the current directory.")
            
        except PermissionError:
            print(f"\nError: No permission to access '{filename}'!")
            print("Check file permissions and try again.")
            
        except UnicodeDecodeError:
            print(f"\nError: Cannot read '{filename}'!")
            print("Make sure it's a valid text file.")
            
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}")
            
        # Ask if user wants to try again
        retry = input("\nWould you like to try another file? (y/n): ")
        if retry.lower() != 'y':
            print("Goodbye!")
            break

def create_sample_file():
    """Creates a sample text file for testing"""
    try:
        with open("sample.txt", "w") as file:
            file.write("This is a sample text file.\nYou can use this to test the file reader.\nTry reading this file!")
        print("Created 'sample.txt' for testing.")
    except Exception as e:
        print(f"Error creating sample file: {str(e)}")

if __name__ == "__main__":
    print("=== File Reader Program ===")
    print("This program reads and displays the contents of a text file.")
    create_sample_file()
    read_file()