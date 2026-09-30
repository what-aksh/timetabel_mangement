# Smart Student Timetable & Free-Slot Manager

## Project Overview

The **Smart Student Timetable & Free-Slot Manager** is a terminal-based Python application designed to help students organize and manage their weekly academic timetable.

The application allows users to add, view, search, and remove classes while detecting timetable clashes and identifying available free-time slots. It also provides basic timetable analytics such as total classes, scheduled class-hours, number of clashes, and the busiest day.

The project demonstrates Python programming concepts including data structures, functions, classes, loops, conditional statements, searching, sorting, time comparison, input validation, error handling, and modular programming.

---

## Features

- Add classes to the weekly timetable
- View the complete weekly timetable
- Search for classes by subject
- Remove scheduled classes
- Detect overlapping timetable clashes
- Find available free-time slots
- View timetable analytics
- Validate user input
- Handle invalid inputs and menu choices

---

## Functional Modules

| Module | Description |
|---|---|
| Timetable Management | Add, view, search, and remove classes |
| Clash Detection | Detect overlapping classes |
| Free-Slot Finder | Find available periods between classes |
| Timetable Analytics | Display timetable statistics |
| Input Validation | Validate days, times, and time ranges |
| User Interaction | Provide the terminal menu and handle user input |

---

## Technologies Used

- **Python 3**
- **Terminal / Command Line Interface**
- **Git**
- **GitHub**

### Python Concepts Used

- Lists
- Dictionaries
- Tuples
- Functions
- Classes and Objects
- Loops
- Conditional Statements
- Searching
- Sorting
- Time Comparison
- Input Validation
- Exception Handling
- Modular Programming

The project uses Python's built-in features and does not require external Python libraries.

---

## Project Structure

```text
Smart-Student-Timetable/
│
├── README.md
├── statement.md
│
├── src/
│   ├── schedule.py
│   ├── validators.py
│   ├── timetable.py
│   ├── clash_detector.py
│   ├── timetable_tools.py
│   └── main.py
│
└── tests/
    └── test_timetable.py
System Workflow
Start
  ↓
Display Main Menu
  ↓
Select Operation
  ↓
Enter Required Input
  ↓
Validate Input
  ↓
Perform Operation
  ↓
Display Result
  ↓
Return to Main Menu
  ↓
Exit
Setup and Installation
Prerequisites

Make sure Python 3.x is installed on your system.

No external Python libraries are required.

Clone the Repository
git clone <repository-url>
cd Smart-Student-Timetable

Replace <repository-url> with the URL of this GitHub repository.

Run the Project

Navigate to the src folder:

cd src

Run the application:

python main.py
How to Use

After running the application, the following menu is displayed:

========== SMART TIMETABLE ==========
1. Add class
2. View timetable
3. Check clashes
4. Find free slots
5. Search class
6. Remove class
7. View analytics
8. Exit
====================================

Enter the number corresponding to the required operation.

1. Add Class

Enter:

Subject
Day
Start time
End time
Room

Example:

Enter subject: Python
Enter day: Monday
Enter start time (HH:MM): 09:00
Enter end time (HH:MM): 10:00
Enter room: A101
2. View Timetable

Displays the scheduled classes organized by day and sorted according to their start time.

3. Check Clashes

Checks for overlapping classes scheduled on the same day and displays the conflicting classes.

4. Find Free Slots

Enter a day to find available periods between scheduled classes.

The current timetable range for free-slot detection is:

08:00 - 18:00
5. Search Class

Searches for classes using the subject name or a keyword.

6. Remove Class

Removes a scheduled class using:

Subject
Day
Start time
7. View Analytics

Displays:

Total number of classes
Total scheduled class-hours
Number of clashes
Busiest day
8. Exit

Closes the application.

Input Validation

The application validates important user inputs before processing them.

Examples:

Empty subjects are rejected.
Invalid day names are rejected.
Incorrect time formats are rejected.
End time must be after start time.
Invalid menu choices are handled with an error message.
Testing

The project includes automated tests in:

tests/test_timetable.py

The tests cover:

Valid and invalid time formats
Valid and invalid time ranges
Adding classes
Clash detection
Non-overlapping classes
Free-slot detection

To run the tests from the project root:

python -m unittest discover tests
Screenshots

Screenshots demonstrating the application can be added here.

Recommended screenshots:

Main menu
Adding classes
Weekly timetable
Clash detection
Free-slot detection
Timetable analytics
Project Limitations

The current version has the following limitations:

Timetable data is stored only during program execution.
Data is not permanently saved after the program is closed.
The application is terminal-based.
Multiple-user functionality is not implemented.
Notifications and reminders are not implemented.
Automatic timetable generation is not implemented.
Future Enhancements

Possible future improvements include:

Persistent timetable storage
Database integration
Graphical user interface
Automatic timetable generation
Class reminders and notifications
PDF or CSV timetable export
Mobile application
Advanced timetable analytics
Author

Name: Akshat sahu
registration no :26BCE11701
Institution: VIT Bhopal University

Academic Year: 2026–27

Project Status

This project was developed as part of the VITyarthi – Build Your Own Project evaluation.

Status: Completed 


### Your GitHub root should now look like this

```text
📁 Smart-Student-Timetable
│
├── 📄 README.md          ← THIS FILE
├── 📄 statement.md
│
├── 📁 src
│   ├── main.py
│   ├── schedule.py
│   ├── timetable.py
│   ├── validators.py
│   ├── clash_detector.py
│   └── timetable_tools.py
│
└── 📁 tests
    └── test_timetable.py
