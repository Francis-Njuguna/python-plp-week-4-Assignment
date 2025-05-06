# File Reading and Error Handling Project 📝

## Overview
This project contains two Python programs demonstrating file handling and error management in Python.

## Programs

### 1. File Reader (`file_reader.py`) 📖
A program that handles file reading with comprehensive error handling.

#### Features
- Interactive file reading interface
- Robust error handling for common file operations:
  - Missing files
  - Permission issues
  - Invalid file formats
- User-friendly retry mechanism
- Auto-generated sample file for testing

#### Usage
```bash
python file_reader.py
```

#### Example Output
```
=== File Reader Program ===
This program reads and displays the contents of a text file.
Created 'sample.txt' for testing.

Enter the filename to read: sample.txt

File contents:
--------------------------------------------------
This is a sample text file.
You can use this to test the file reader.
Try reading this file!
--------------------------------------------------
```

### 2. File Modifier (`file_modifier.py`) ✏️
A program that reads, modifies, and writes files.

#### Features
- Reads input files
- Adds line numbers
- Converts text to uppercase
- Creates backup of original file
- Error handling for file operations

#### Usage
```bash
python file_modifier.py
```

## Project Structure
```
python-plp-week-4-Assignment/
├── README.md
├── file_reader.py
├── file_modifier.py
├── sample.txt (auto-generated)
└── modified_sample.txt (generated when running modifier)
```

## Requirements
- Python 3.x
- Windows OS
- VS Code (recommended)

## Getting Started

1. Clone or download the project
2. Open in VS Code:
```bash
code python-plp-week-4-Assignment
```

3. Run the programs:
```bash
# For file reader
python file_reader.py

# For file modifier
python file_modifier.py
```

## Error Handling
The programs handle various scenarios:
- ❌ File not found
- 🚫 Permission denied
- 📄 Invalid file format
- ⚠️ Unexpected errors

## Contributing
Feel free to fork and submit pull requests.

## License
MIT License - Feel free to use and modify for your needs.