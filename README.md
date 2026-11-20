Blood Bank Management System

Project Overview

The Blood Bank Management System is a Python-based console application designed to help blood bank staff manage blood donations, issue blood, view available stock, and search for donors according to their blood groups.

The system uses Python dictionaries, lists, and file handling to maintain blood stock and donor records.

Features

1. Add Donor: Add a new donor with their name, blood group, and donated units.
2. Issue Blood: Issue blood to patients only when sufficient units are available.
3. View Stock: Display the available units of all blood groups.
4. Search Donors: Search for donors based on their blood group.
5. Exit: Exit the application.

Technologies Used

- Programming Language: Python 3
- Concepts:
  - Dictionaries
  - Lists
  - File Handling
  - Searching
  - Conditional Statements
  - Loops
  - Functions

Supported Blood Groups

- A+
- A-
- B+
- B-
- AB+
- AB-
- O+
- O-

Initial Blood Stock

Blood Group| Units
A+| 10
B+| 5
O+| 8
AB+| 2
Others| 0

File Handling

Donor information is stored in a text file named "donors.txt".

The donor records are maintained using a list of dictionaries, and the records are saved to the file.

Input Validation

- Only eight valid blood groups are accepted.
- Only positive whole-number units are allowed.
- Blood cannot be issued if sufficient stock is unavailable.
- Invalid blood groups are rejected.

Project Structure

Blood-Bank-Management-System/
│
├── blood_bank.py
├── donors.txt
├── README.md
└── SUMMARY.md


How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

python blood_bank.py

5. Select an option from the menu and follow the instructions.

Test Cases

The project is tested using four test cases:

1. Normal Input – Adding a donor.
2. Boundary Input – Issuing the minimum available AB+ stock.
3. Invalid Input – Testing insufficient stock and invalid blood groups.
4. Different Valid Scenario – Searching donors with blood group O+.

Conclusion

The Blood Bank Management System provides a simple and organized way to manage blood donations and stock. It demonstrates the practical implementation of Python dictionaries, lists, searching, and file handling.
