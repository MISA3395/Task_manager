# The following programme allows users to register and manage tasks.

import os
from datetime import datetime, date

# Define the format for date strings.
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt file if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Open the tasks.txt file and read all of the data using split function. 
with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

# Set a list to store user data.
task_list = []
for t_str in task_data:
    # Set a dictionary to store the current task with index.
    curr_t = {}

    # Split by semicolon and manually add each component.
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    # Append the current task with the index to the list.
    task_list.append(curr_t)

# ---Define functions---
# Define the reg_user function to register a new user to the user.txt file. 
def reg_user():
    # Request input of a new username.
    new_username = input("New Username: ")

    # Check if the username already exists.
    if new_username in username_password:
        print("Username already exists. Please try a different username.")
        return

    # Request input of a new password.
    new_password = input("New Password: ")

    # Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # If they are the same, add them to the user.txt file
        print("New user added")
        username_password[new_username] = new_password

        # Open the user.txt file and write the new user name and new password to it.
        with open("user.txt", "w") as out_file:
            # Set a list to store the new user name and new password.
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # The error message below will be output if the New Password and Confirm Password the user input are not the same.
    else:
        print("Passwords do not match")

# Define the add_task function to add a new task.
def add_task():
    '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and 
    - The due date of the task.'''

    # Request input on the name of the person assigned to the task.
    task_username = input("Name of person assigned to task: ")

    # If the task_username is not in username_password, prompt to re-enter task_username.
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    
    # The program below(from the line 91) will be executed if the task_username is in username_password.
    # Request input on the title and description of the task.
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            # Request input on the due date of the task.
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        
        # If the user input an invalid datetime such as 'mm-yyyy-dd', the error message below will be output and prompt to re-enter a valid datetime.
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
    Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Append the new task data the user input into task_list.
    task_list.append(new_task)

    # Open the tasks.txt file and write the new task data to it.
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")

# Define the view_all function to view all tasks.
def view_all():
    # Prints tasks from task.txt file.
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

# Define the view_mine function to view all the tasks that have been assigned to them.
def view_mine():
    # Reads the tasks from task.txt file, user can select and edit tasks
    while True:
        print("My Tasks:")
        # Number each task using enumerate so that each task can be searched by number.
        for num, t in enumerate(task_list, 1):
            if t['username'] == curr_user:
                disp_str = f"Task Number: {num}\n"
                disp_str += f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                disp_str += f"Completed: \t {t['completed']}\n"
                print(disp_str)
        
        # Request input on the task number the user want to view.
        print("Select a task number to perform an action (enter -1 to return to the main menu): ")
        task_num = input()
        
        # If they enter -1, return to the main menu.
        if task_num == '-1':
            break
        
        try:
            task_num = int(task_num)
            # The error message below will be executed if they enter an invalid number and prompt to re-enter a task number.
            if task_num < 1 or task_num > len(task_list):
                print("Invalid task number. Please try again.")
                continue
        # The error message below will be executed if they enter an invalid character(not number) and prompt to re-enter a task number or -1.
        except ValueError:
            print("Invalid input. Please enter a task number or -1.")
            continue
        
        # The task numbers are numbered sequentially from 1, so they are subtracted by -1 to match the correct index number.
        selected_task = task_list[task_num - 1]
        
        # Outputs the task data they chose.
        print("Selected Task:")
        disp_str = f"Task Number: {task_num}\n"
        disp_str += f"Task: \t\t {selected_task['title']}\n"
        disp_str += f"Assigned to: \t {selected_task['username']}\n"
        disp_str += f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {selected_task['description']}\n"
        disp_str += f"Completed: \t {selected_task['completed']}\n"
        print(disp_str)
        
        # Request input on a number if they want to mark it as completed or edit the chosen task.
        print("Select an action:")
        print("1. Mark as completed")
        print("2. Edit task")
        action = input()
        
        # Mark as completed the task if they input '1'.
        if action == '1':
            # If message below will be output if the task is already marked as completed.
            if selected_task['completed']:
                print("Task is already marked as completed.")
            # Mark as completed if the task has not been marked.
            else:
                selected_task['completed'] = True
                print("Task marked as completed.")

        # Edit the task if they input '2'.
        elif action == '2':
            # If the task is already completed, it can not be edit.
            if selected_task['completed']:
                print("Task is already completed. Cannot edit.")
            # Edit the task if it has not been completed.
            else:
                print("Select an option to edit:")
                print("1. Edit username")
                print("2. Edit due date")
                option = input()
                
                # Edit the current user name to a new one.
                if option == '1':
                    # Request input on a new user name and the message below will be output if edited successfully.
                    new_username = input("Enter a new username: ")
                    selected_task['username'] = new_username
                    print("Username updated.")

                # Edit the current due date to a new one.
                elif option == '2':
                    # Request input on a new due date.
                    new_due_date = input("Enter a new due date (YYYY-MM-DD): ")
                    try:
                        # The message below will be output if edited successfully.
                        due_date = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT).date()
                        selected_task['due_date'] = due_date
                        print("Due date updated.")
                    # If the user input different format such as 'mm-dd-yyyy', the error message below will be output.
                    except ValueError:
                        print("Invalid date format. Please try again.")
                # The error message below will be output if they input an invalid number and prompt to re-enter a number to choose edit user name or due date.
                else:
                    print("Invalid option. Please try again.")
        # The error message below will be output if they input an invalid number and prompt to re-enter a number to choose mark or edit the task.
        else:
            print("Invalid action. Please try again.")

        # Open the tasks file and write the marked or edited task to the file.
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))

# Define the reports function to generate the task overview and user overview. 
def reports():
    # ---Generate Task Overview Report---
    # How to calculate the number of tasks, the number of completed and uncompleted tasks.
    total_tasks = len(task_list)
    completed_tasks = sum(t['completed'] for t in task_list)
    uncompleted_tasks = total_tasks - completed_tasks

    while True:
        try:
            # How to calculate the percentage of tasks not completed and out of date tasks.
            overdue_tasks = sum(t['completed'] is False and t['due_date'].date() < date.today() for t in task_list)
            incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
            overdue_percentage = (overdue_tasks / total_tasks) * 100
            break

        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

    task_overview = f"Task Overview\n" \
                    f"----------------\n" \
                    f"Total tasks: {total_tasks}\n" \
                    f"Completed tasks: {completed_tasks}\n" \
                    f"Uncompleted tasks: {uncompleted_tasks}\n" \
                    f"Overdue tasks: {overdue_tasks}\n" \
                    f"Incomplete percentage: {incomplete_percentage:.2f}%\n" \
                    f"Overdue percentage: {overdue_percentage:.2f}%"

    # Open the task_overview file and write the above task_overview to it.
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(task_overview)
        print(task_overview)

    # ---Generate User Overview Report---
    # Total number of users.
    total_users = len(username_password.keys())
    user_overview = f"User Overview\n" \
                    f"----------------\n" \
                    f"Total users: {total_users}\n"

    # Task details per user.
    for username in username_password.keys():
        user_tasks = [t for t in task_list if t['username'] == username]
        total_user_tasks = len(user_tasks)
        completed_user_tasks = sum(t['completed'] for t in user_tasks)
        uncompleted_user_tasks = total_user_tasks - completed_user_tasks
        overdue_user_tasks = sum(t['completed'] is False and t['due_date'].date() < date.today() for t in user_tasks)

        # How to calculate the percentage of total tasks, task completed, uncompleted and tasks uncompleted and overdue.
        percentage_total_user_tasks = (total_user_tasks / total_tasks) * 100
        percentage_completed_user_tasks = (completed_user_tasks / total_user_tasks) * 100
        percentage_uncompleted_user_tasks = (uncompleted_user_tasks / total_user_tasks) * 100
        percentage_overdue_user_tasks = (overdue_user_tasks / total_user_tasks) * 100

    user_overview += f"\nUsername: {username}\n" \
                    f"Total tasks assigned: {total_user_tasks}\n" \
                    f"Percentage of total tasks: {percentage_total_user_tasks:.2f}%\n" \
                    f"Percentage of tasks completed: {percentage_completed_user_tasks:.2f}%\n" \
                    f"Percentage of tasks uncompleted: {percentage_uncompleted_user_tasks:.2f}%\n" \
                    f"Percentage of tasks uncompleted and overdue: {percentage_overdue_user_tasks:.2f}%\n"
            
    # Open the user_overview txt file and write the above user_overview data.
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(user_overview)
        print(user_overview)

    # The message below will be output if both of the overviews are generated successfully.
    print("Reports generated successfully.")

# ---Login Section---
# Read usernames and passwords from the user.txt file to allow a user to login.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read user_data.
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary.
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# If the user cannot be logged in the program below will be executed.
logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")

    # If the user name they entered isn't in user.txt file, the error message below will be output and prompt to re-enter username and password.
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue

    # If the password they entered isn't in user.txt file, the error message below will be executed and prompt to re-enter username and password.
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue

    # If they are logged in successfully, the message below will be output.
    else:
        print("Login Successful!")
        logged_in = True

# ---Menu section---
while True:
    # Present the menu to the user and make sure that the user input is converted to lowercase.
    print()
    menu = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        reports()
    elif menu == 'ds' and curr_user == 'admin':
    # If the user is an admin, they can display statistics about the number of users and tasks.
        with open("user.txt", "r") as user_file:
            user_data = user_file.read().split("\n")
        num_users = len(user_data) 

        with open("tasks.txt", "r") as task_file:
            task_data = task_file.read().split("\n")
        num_tasks = len(task_data) 

        completed_tasks = sum(task.split(";")[5] == "Yes" for task in task_data if task != "")
        uncompleted_tasks = num_tasks - completed_tasks

        overdue_tasks = sum(
            task.split(";")[5] == "No" and datetime.strptime(task.split(";")[3], DATETIME_STRING_FORMAT).date() < date.today()
            for task in task_data if task != ""
        )

        incomplete_percentage = (uncompleted_tasks / num_tasks) * 100
        overdue_percentage = (overdue_tasks / num_tasks) * 100

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print(f"Number of completed tasks: \t {completed_tasks}")
        print(f"Number of uncompleted tasks: \t {uncompleted_tasks}")
        print(f"Number of uncompleted and overdue tasks: {overdue_tasks}")
        print(f"Percentage of incomplete tasks: \t {incomplete_percentage:.2f}%")
        print(f"Percentage of overdue tasks: \t {overdue_percentage:.2f}%")
        print("-----------------------------------")

    # If the user entered, 'e', the program will be ended.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # If the user inputs an invalid character, the else statement will be executed and prompt to re-enter a character for the menu.
    else:
        print("You have made a wrong choice. Please try again.")
