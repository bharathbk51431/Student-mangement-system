🎓 Student Information Tracker:

A Lightweight Student Management System
This is a Python-based Student Management System designed to handle student records using a dynamic list structure. It provides a simple, menu-driven interface to manage academic data in real-time.   


🛠️ System Operations

Based on the current source code, the system supports the following five core actions:   

Add Student: Appends a new dictionary containing Name, Roll Number, and Course to the master list.   

View Students: Iterates through the list to display all registered students in a clean format.   

Search Student: Uses a linear search to find a student by their unique Roll Number.   

Update Student: Modifies the Name and Course details of an existing record.   

Delete Student: Permanently removes a student's entry from the list based on their Roll Number.   


🏗️ Technical Implementation

The program is built with a focus on clean, functional Python logic:   

Storage: Uses a global Students = [] list.   

Data Object: Each student is represented as a Dictionary with keys for name, roll, and course.   

Control Flow: A while True loop keeps the system active until the user selects the "Exit" option.   

Linear Search: Functions like search_student and delete_student use iterative loops to match Roll Numbers accurately.   


💻 Console Preview
```
1.Add 
2.View 
3.Search 
4.Update 
5.Delete 
6.Exit
Enter choice: 1   

Enter Name: Bharath B K
Enter Roll No: 101
Enter Course: Python
Student Added Successfully   
```


🚀 How to Use
Environment: Ensure you have Python installed.

Download: Clone the repository:
git clone https://github.com/bharathbk51431/Student-mangement-system

Run: Execute the script via terminal:
python student_management.py   


📝 Developer Notes

In-Memory Storage: Since the system uses a standard Python list, data is stored in the RAM. Exiting the program will reset the list.   

Scalability: The code is designed to be easily expandable with file-handling (CSV/JSON) features in future versions.   


👨‍💻 Developed by 

Bharath B K
An educational project focused on Python Data Structures.
