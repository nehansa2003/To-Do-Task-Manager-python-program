User Manual- To-Do-Task Manager

1.Introduction

1.1 Overview

The To-Do_Task Manager is a robust and user-friendly command-line application designed to 
help users efficiently manage and organize their tasks. It provides a secure and personalized 
environment for adding tasks, viewing , editing and removing tasks. Users can easily log in to the 
application and view their tasks and it’s details and keeping track on deadlines, remaining time for 
each task. Users can plan their days by looking their tasks which they have to do and after 
completing them they can remove those tasks from their list. The program saves user data 
persistently, ensuring continuity across sessions.

1.2 Purpose 

The main purpose of To-Do-Task Manager is to help students, professionals, individuals to 
organize track and manage their tasks effectively by providing a secure and intuitive platform. It 
aims to enhance productivity and ensure users stay on top of their commitments. 
Specific goals 

• Task Organization: Enable users to systematically categorize their tasks with meaningful 
names and descriptions. 

• Deadline Management: Allow users to set deadlines for tasks and track the remaining time 
until their completion. 

• Improved Productivity: Keep users focused by presenting an up-to-date list of tasks, 
helping them prioritize what needs to be done. 

• Data Security and Personalization: Ensure that each user has a private, personalized 
account with exclusive access to their task data.

• Flexibility in Task Updates: Provide the ability to update task details as priorities and 
deadlines change.

• Simple Task Removal: Facilitate the removal of completed or unnecessary tasks, keeping 
the task list clutter-free.

• The main three parties who will be benefited from this application.

Students: Managing assignments, projects, and deadlines.

Professionals: Tracking work tasks, meetings, and deliverables. 

Individuals: Organizing personal goals, reminders, and events.

1.3 Key features

1. User Authentication:
 
   • Registration: New users can create accounts with unique usernames and secure 
passwords. 
   • Login: Registered users can log in to access their tasks. 
   • Password Management: Options to reset forgotten passwords. 

2. Task Management:
    
   • Add Tasks: Users can add tasks with:

          o A short, descriptive name.

          o A detailed description.

          o A specific deadline in the format dd/mm/yyyy-hh:mm.

   • View Tasks: View a list of all tasks with options to: 

   • See detailed task information (name, description, deadline, and time remaining).

   • Check remaining time until a task deadline from the current moment. 

   • Edit Tasks: Modify task details such as name, description, or deadline.

   • Remove Tasks: Remove tasks from the list once completed or no longer needed.

3. Deadline Tracking: 

   • Automatically calculates and displays time remaining for each task.
    
4. Persistent Data Storage: 

   • User data, including tasks, is saved in a JSON file (users.json), ensuring that no progress is lost between sessions. 
5. User-Friendly Interface: 

   • Clear and interactive menus guide users through options.

   • Error handling for invalid inputs and incorrect formats.
    
6. Customizable Options:

   • Flexibility to manage tasks through various actions like viewing, editing, or deleting.

   • Tailored user accounts to maintain privacy and individualized task lists.

2.System requirements and Setup instructions

This program is written in Python, making it platform-independent. However, certain prerequisites 
must be met before running the application. Below are the system requirements and step-by-step 
setup instructions.

2.1 System requirements 

1. Operating System:
    
   • Windows, macOS, or Linux.

2. Python Version: 

   • Python 3.7 or higher is required to run the program. 
3. Python Modules (Built-in):

   • os, json, re, datetime 
4. Storage Space: 

   • Minimal space required (less than 1 MB) to store the users.json file for user and task 
data. 

2.2 Setup instructions

1. Install Python:
    
   • Download and install Python from the official Python website:                                                       
https://www.python.org/.

   • Ensure that Python is added to the system's PATH during installation.

   • Verify Python Installation: 

       o Open a terminal(command prompt, PowerShell, Linux terminal).

       o Type ‘python –version’ and hit Enter key.

       o If you installed python properly it will be display the version of python which you have installed otherwise it will be display python cannot recognize or something which is negative idea related to python installation.

          ✓ It is compulsory that you have to install python setup successfully.

2. Download the Program
   
   • Copy the program code into a file and save it as to_do_task_manager.py.

3. Set Up the users.json File:
   
   • The program will automatically create a users.json file in the same directory on first 
run. 

   • If desired, you can create an empty users.json file manually in the same directory as 
to_do_task_manager.py: {} 

4. Run the Program:
    
   • Open a terminal, navigate to the folder containing the to_do_task_manager.py file, 
and run the program using: python to_do_task_manager.py

3.Getting start with To-Do-Task Manager 

This guide will help you navigate through the To-Do Task Manager and understand its user 
interface. The program runs in a command-line interface (CLI), offering a clear, menu-driven 
navigation system for managing tasks. 

3.1Basic navigation 

The program uses numbered menus and text inputs for user interaction. Follow these steps to get 
started:(below section 4 describes this every step with more guidelines)

Step 1: Launch the Program 

    ❖ Run the program by executing: python to_do_task_manager.py (type this in the terminal.) 
The program will greet you with a welcome message and prompt you to either: 

    ❖ Register (Option 1): If you’re a new user, create a new account.

    ❖ Login (Option 2): If you already have an account, log in to access your tasks. 

Step 2: Registration or Login 

    ❖ If you choose option 1, you can register by giving a username and a password.(it should be 
contain at least 6 characters) Once you registered successfully you will be automatically 
logged in. 

    ❖ If you choose option 2, you can logging by giving username and password correctly. If you 
forgot your username you have to register as a new user and starting fresh and also if you 
forget password you can change your password by selecting forget password option (This 
forget password option can be visible once you failed to give password correctly.)

Step 3: Menu overview

1. View Tasks: Displays a list of all your task’s names.after that you can see task details, 
edit task details if you need.
 
   o Select a task by it’s number to view details and edit task details. 

2. Add Tasks: Allows you to add a new task with,
    
   o A task name.

   o A description.

   o A deadline (formatted as dd/mm/yyyy-hh:mm).

3. Remove Tasks: Displays a list of your tasks.
    
    o Select a task by its number to remove it from the list.

4. Exit: Logs you out and exits the program.
   
3.2Task Management Commands 

Here’s how you can interact with tasks effectively:

1. Viewing Task Details
  
   o Select a task from the list to see: Then you can see,Task name, Description, Deadline and Time Remaining(if you need)

2. Editing Task Details:
    
   o Choose the option to modify: Then you can choose the item number which you want to change, 

       1. Task name
      
       2. Task Description
     
       3. Task Deadline(validated to ensure correct format)
       
3. Removing Tasks:
    
    o Select a task to remove it once completed or no longer needed. 
