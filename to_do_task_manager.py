#To_D0_Task-Manager
import os
import json
import re
from datetime import datetime
#global variables.
user_file="users.json"
users={}
current_user=None
task_request=None
password=None
current_time=datetime.now()
def save_data(): #The function to save users data in the jason file.
    with open(user_file,"w")as file:
        json.dump(users,file,indent=4,default=str)
        print(f"Data saved successfully.")

#The function to load data from the file.
def load_data():
    global users
    if os.path.exists(user_file):
        try:
          with open(user_file,"r")as file:
            users=json.load(file)
            print("saveed data load successfully.")
        except json.JSONDecodeError:
              print(f"Error reading data. start with fresh.")
              users={}
    else:
        print(f"No saved data found.Starting fresh.") 
        users={}
#The function to authenticate the user.
def user_authentication():
  print(f"\nWelcome to 'To-Do-Task Manager.'")
  print(f"\n1.Register. \n2.Login.")
  user_react_1=input(f"If you are new to'To-Do-Task-Manager'you need to register here.so enter 1 and if you already registered here enter 2 to login:  ")
  if user_react_1== "1":
    user_registration()
  elif user_react_1=="2":
    user_login()
  else:
    print(f"\nInvalid input.Please enter 1 or 2.")
    return user_authentication()
#The function to regiter new users.
def user_registration():
    global current_user
    global user_file
    load_data()
    while True:
     username=input(f"\nEnter the username: ")
     if username in users:
      print(f"\nThis username already exists.Please enter another username.")
     else:
      break
    while True:
      password=input(f"\nEnter a password which include more than six characters: ")
      if len(password)>=6:
        users[username]={"password":password,"task_names":[],"tasks":[] }
        save_data()
        current_user=username
        print(f"\nRegistration successfull!")
        print(f"\nyour username is {username} \nyour password is {password}")
        break
      else:
        print(f"\nPassword too short.Try again.")
#The function to user login.
def user_login():
   global current_user,password
   load_data()
   username=input(f"\nEnter the username: ")
   if username in users:
      current_user=username
      user_password()
   else:
      print(f"\nUsername not found.Please try below options.")
      print(f"\n1.Try again \n2.Register as new user.")
      user_react_4=input(f"Enter the option number which you prefer to use: ")
      if user_react_4=="1":
         return user_login()
      elif user_react_4=="2":
         user_registration()
      else:
         print(f"\nInvalid option.")
         return user_authentication()
#The function to resolve the user problems related to user-password.
def user_password():
   global current_user
   password=users[current_user].get("password")
   en_password=input(f"\nEnter the password: ")
   if password==en_password:
      print(f"\nLogin successfull.")
   else:
      print(f"\nWrong password.")
      print(f"\n1.Try again \n2.Forget password.")
      user_react_3=input(f"You can choose above 1 or 2 option.\n Enter the option number(1 or2): ")
      if user_react_3=="1":
         return user_password()
      elif user_react_3=="2":
         new_password=input(f"\nEnter your new password: ")
         users[current_user]["password"]=new_password
         save_data()
         print(f"\nyour new password is {new_password} please keep it save somewhere. ")
      else:
         print(f"\nInvalid option.Please try again.")
         return user_authentication()
#The function to view task list.
def view_tasks():
   global current_tasks
   task_names=users[current_user].get("task_names",[])
   tasks=users[current_user].get("tasks",[])
   print(f"\nYour tasks list:")
   if tasks:
      task_no=1
      for task in (task_names): 
         print(task_no,task)
         task_no=task_no+1
      print(f"\nPlease choose one of below options")
      print(f"\n1.View task details. \n2.Edit task deatils \n3.Menu ")
      user_react_5=input(f"Enter your choice: ")
      if user_react_5=="1":
         view_task_details()
      elif user_react_5=="2":
         edit_task_details()
      elif user_react_5=="3":
         print(f"\nMenu:")
      else:
         print(f"\nInvalid input.Try again.")
         return view_tasks()
   else:
       print(f"\nNo tasks available.")
#The function to view a task details.
def view_task_details():
    global current_user,task_request,current_time,time_remaining,update_dead
    task_names=users[current_user].get("task_names",[])
    tasks=users[current_user].get("tasks",[])
    task_no=1
    print(f"\nyour tasl list:")
    for task in (task_names): 
      print(task_no,task)
      task_no=task_no+1
    try:
     task_num=int(input(f"\nEnter the number of the task which you need to see the details: "))
     try:
      task_request=tasks[task_num-1]
      print("\nTask name:",task_request["Task name"])
      print("Discription:",task_request["Description"])
      print("Deadline:",task_request["Deadline"])
      print("Time-remaining:",task_request["Time-remaining"],"had since you add this task to 'To-Do Task Manager'")
      user_reply=input("\nDo you want to know the remain time for this task from this moment(yes/no)? ")
      if user_reply=="yes":
         view_time_remain()
         after_task_details()
      else:
       after_task_details()
     except IndexError:
       print(f"Invalid task number.")
       return view_task_details()
    except ValueError:
       print(f"Invalid input.Enter a number of the task.")
#The function to get remain time from crrent time
def view_time_remain():
   deadline_input=input("\nEnter the deadline of this task to see the remain time from this moment(dd/mm/yyyy-HH:MM): ")
   #Regular expression pattern to validate deadline formate
   deadline_pattern=r"^\d{2}/\d{2}/\d{4}-\d{2}:\d{2}$"
   if re.match(deadline_pattern,deadline_input):
       try:
          deadline_input=datetime.strptime(deadline_input,"%d/%m/%Y-%H:%M")
          if deadline_input<current_time:
           time_remaining="The deadline for this task has passed."
           print(f"\n{time_remaining}")
          else:
             time_remaining=str(deadline_input-current_time).split(".")[0]
             print(f"\nThe reamain time for this task is {time_remaining} from this moment.")
       except ValueError:
                print(f"\nInvalid date or time.Please check and try again.")
                return view_task_details()
   else:
     print(f"\nInvalid formate.Please use 'dd/mm/yyyy-hh:mm'. ")
     return view_time_remain()
          
#The fuction to select options after viewing a task details.
def after_task_details():
   print(f"\n1.Edit task details \n2.View task details \n3.Menu")
   print(f"\nPlease choose one of above options.")
   user_react_6=input(f"Enter your choice: ")
   if user_react_6=="1":
      edit_task_details()
   elif user_react_6=="2":
      return view_task_details()
   elif user_react_6=="3":
      print(f"\nMenu:")
   else:
      print(f"Invalid choice.")
      return after_task_details()
# The function to change /edit task details.
def edit_task_details():
   global current_user,task_request,current_time
   task_names=users[current_user].get("task_names",[])
   tasks=users[current_user].get("tasks",[])
   print(f"your tasl list:")
   task_no=1
   for task in (task_names): 
     print(task_no,task)
     task_no=task_no+1
   try:
     task_num=int(input(f"\nEnter the number of the task which you need to change the details: "))
     try:
      task_request=tasks[task_num-1]
      task=task_names[task_num-1]
      print(f"\n1.Task name \n2.Description \n3.Deadline \n4.Menu ")
      user_react_7=input(f"Enter the number of the item that you need to change: ")
      if user_react_7=="1":
         new_task_name=input(f"\nEnter the new task name: ")
         task_request=new_task_name
         task_names[task_num-1]=new_task_name
         task_dict=tasks[task_num-1]
         task_dict["Task name"]=new_task_name
         save_data()
         print(f"\nyour task name changed as {new_task_name}.")
      elif user_react_7=="2":
         new_description=input(f"\nEnter the new description: ")
         task_request["Description"]=new_description
         save_data()
         print(f"\nThe description of the {task} is changed as {new_description}")
      elif user_react_7=="3":
         while True:
          new_deadline=input(f"\nEnter the new deadline(dd/mm/yyyy-hh:mm): ")
          #Regular expression pattern to validate deadline formate
          deadline_pattern=r"^\d{2}/\d{2}/\d{4}-\d{2}:\d{2}$"
          if re.match(deadline_pattern,new_deadline):
             try:
                new_deadline=datetime.strptime(new_deadline,"%d/%m/%Y-%H:%M")
                if new_deadline>current_time:
                  break
                else:
                   print(f"\nThe deadline you entered has been already passed.Please check it and enter correctly.")
             except ValueError:
                print(f"\nInvalid date or time.Please check and try again.")
          else:
            print(f"\nInvalid formate.Please use 'dd/mm/yyyy-hh:mm'. ")
         new_time_remaining=str(new_deadline-current_time).split(".")[0]
         task_request["Deadline"]=new_deadline
         task_request["Time-remaining"]=new_time_remaining
         save_data()
         print(f"\nDeadline of the {task} is changed as {new_deadline}.")
      elif user_react_7=="4":
         print("\nMenu:")
      else:
         print(f"\nInvalid choice.Try again.\n")
         return edit_task_details()
     except IndexError:
        print(f"\nInvalid index number.Please try again.\n")
        return edit_task_details()
   except ValueError:
      print(f"\nInvalid input. Please enter the number of the task.\n")
      return edit_task_details()
#The function to add a new task to the list
def add_task():
   global current_user,current_time,users
   task_names=users[current_user].get("task_names",[])
   tasks=users[current_user].get("tasks",[])
   new_task=input("\nEnter the task name(short_name to identify task): ")
   description=input("\nEnter a description about this task: ")
   while True:
    deadline=input(f"\nEnter the deadline(dd/mm/yyyy-hh:mm): ")
    #Regular expression pattern to validate deadline formate
    deadline_pattern=r"^\d{2}/\d{2}/\d{4}-\d{2}:\d{2}$"
    if re.match(deadline_pattern,deadline):
         try:
            deadline=datetime.strptime(deadline,"%d/%m/%Y-%H:%M")
            if deadline>current_time:
              break
            else:
               print(f"\nThe deadline you entered has been already passed.Plese check it and enter correctly.")
         except ValueError:
                print(f"\nInvalid date or time.Please check and try again.")
    else:
     print(f"\nInvalid formate.Please use 'dd/mm/yyyy-hh:mm'. ")
   time_remaining=str(deadline-current_time).split(".")[0]
   task_names.append(new_task)
   new_task_details={"Task name":new_task,"Description":description,"Deadline":deadline,"Time-remaining":time_remaining}
   tasks.append(new_task_details)
   save_data()
   print(f"\nTask added successfully.")
#The function to remove tasks after they compleated.
def remove_task():
   global current_user,task_names
   task_names=users[current_user].get("task_names",[])
   tasks=users[current_user].get("tasks",[])
   if tasks:
      task_no=1
      print(f"\nYour tasks list: ")
      for task in (task_names): 
         print(task_no,task)
         task_no=task_no+1
      try:
       rem_task_num=int(input("\nEnter the task number which you need to remove from the list: "))
       try:
         rem_task_name=task_names[rem_task_num-1]
         rem_task=tasks[rem_task_num-1]
         user_react_8=input(f"\nAre you sure that you want to remove {rem_task_name} from the list (yes/no): ")
         if user_react_8=="yes":
            tasks.remove(rem_task)
            task_names.remove(rem_task_name)
            save_data()
            print(f"\ntask:{rem_task_name} removed successfully.")
         elif user_react_8=="no":
            print(f"\n1.Go to remove tasks again.\n2.Menu")
            user_react_9=input("Enter you choicen(1 or 2): ")
            if user_react_9=="1":
               print(f"\n")
               return remove_task()
            elif user_react_9=="2":
               print("\nMenu:")
            else:
               print(f"\nInvalid choice number.")
         else:
            print(f"\nInvalid answer.")
            return remove_task()
       except IndexError:
         print(f"\nInvalid task number.Please enter a valid task number.")
         return remove_task()
      except ValueError:
         print(f"\nInvalid input.Please enter a valid number.")
   else:
      print(f"\nNo tasks available.")
# The menu function to connect all the functions
def menu():
    global current_user,current_time,task_request,users,user_file
    print(f"\n1.View tasks \n2.add tasks \n3.Remove tasks \n4.Exit")
    user_react_2=input(f"Enter your choice: ")
    if user_react_2=="1":
       view_tasks()
       return menu()
    elif user_react_2=="2":
       add_task()
       return menu()
    elif user_react_2=="3":
       remove_task()
       return menu()
    elif user_react_2=="4":
       print(f"\nExixting the program. \n Good bye!")
    else:
       print("\nInvalid choice.")
       return menu()
def main():
   user_authentication()
   menu()
#To start the program
main()

       

    
   