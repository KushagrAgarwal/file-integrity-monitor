# File Integrity Monitoring Tool Using SHA-256

## 1. Introduction
This project is a simple Python-based file integrity monitoring tool. It checks whether a file has been modified by calculating and comparing its SHA-256 hash values.

## 2. Objectives
- To understand file integrity monitoring.
- To use Python's `hashlib` module to calculate SHA-256 hashes.
- To use the `os` module to check whether a file exists.
- To detect changes in file contents.

## 3. Technologies Used
- Python
- hashlib
- os
- SHA-256 hashing algorithm

## 4. Working Principle
The program asks the user to enter a file path and calculates its original SHA-256 hash. When the user selects the check option, the program calculates the current hash and compares it with the original hash.

If both hashes match, the file is reported as unchanged. If they differ, the program reports that the file has been modified.

## 5. How to Run
1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   `python file_integrity_checker.py`

5. Enter the file path when prompted.
6. Select option 1 to check the file or option 2 to exit.

## 6. Testing
The program was tested in three scenarios:
1. An unchanged file was correctly identified.
2. A modified file was detected.
3. After restoring the original contents and restarting the program, the file was identified as unchanged.

## 7. Limitations
The original hash is stored only in memory while the program runs. Restarting the program creates a new baseline from the file's current contents. Therefore, this version does not preserve the original hash between program runs.

## 8. Future Improvements
- Save reference hashes in a separate file.
- Monitor multiple files.
- Add a graphical user interface.
- Record detected changes in a log file.

## 9. Conclusion
This project demonstrates how SHA-256 hashing can be used to detect file modifications and understand the basic principles of file integrity monitoring.
