# Outline of Project
'''
?>    1. input the rooms/areas in your house
?>        - start with a simple list
        - make templates of common configurations to make onboarding faster
?        - could expand to a map with a "heatmap" of tasks in each area
?>    2. iterate through the rooms and make a list of current things to clean
?        - could also specify which part of the room to focus on when adding tasks
?        - add item and desired frequency
?        - a time estimate can be added, maybe also based on how dirty or cluttered the item/area is
?>    3. set reminders that go off when a maintenance item is overdue
?    4. set priorities by ranking importance
?    5. statistics on each task/area
?    6. cleaning advice based on individual tasks
?        - could be a chatbot / or an expert sourced list
?        - relevan product recommendations and potentially $$$ affiliate referrals or subscriptions to monetize $$$
?    7. inventory of supplies needed and currently available in the house with reminders when low
?   8. gardening/outdoors maintanance expansion
?   9. GUI
?   10. gamification elements to make it not feel like a chore
    '''
'''
# variables to keep track of
    # house
room_names
room_zones
layout
supplies
repairs
upgrades

    # user
tasks
deadlines or reminders
schedule
routines
mood_energy
'''
DONETAG = "IS DONE!"

def main():
# user onboarding innitial setup
    rooms = input_rooms()
    tasks = add_cleaning_tasks(rooms)
    tasks_done = []
    num_tasks_remaining = len(tasks) - len(tasks_done)
    while num_tasks_remaining > 0:
        print()
        if tasks_done != None:
            print("Done:")
            for task in tasks_done:
                print(task)
        print()
        print("To do:")
        for task in tasks:
            if DONETAG not in task:
                print(task)
        task_done = get_integer(f"When you complete a task enter the task number \n Completed Task #", 1,len(tasks) +1, "Input must be in task list.")
        if f"{tasks[task_done -1]}" not in tasks_done:
            #print(f"test: {tasks[task_done -1]} {DONETAG}")
            tasks_done.append(f"{tasks[task_done -1]} {DONETAG}")
            num_tasks_remaining = len(tasks) - len(tasks_done)
            tasks[task_done -1] = f"{tasks[task_done -1]} {DONETAG}"
        #del tasks[task_done -1]
    print("Done:")
    for task in tasks_done:
        print(task)
    print()
    print("No more tasks to complete!")
    print()
    print("Go take a nap!")
    print("Bye!")




    #set_reminders()
#set_priorities()

# user interface
#layout_map()
#show_tasks()
#update_tasks()
    #print("@ *end of main*")

def input_rooms():
    print("Welcome to iClean task manager. Let's note what needs to be done in your house.")
    scope = get_integer(f"Do you want to focus on one room(1) or your whole house(2)? \n", 1,2, "Input must be 1 or 2.")
    if scope == 1:
        rooms = [input(f"What room are you cleaning? \n")]
        #print(f"rooms: {rooms}")
    elif scope == 2:
        rooms = []
        room_types = ["bedroom", "bathroom", "kitchen", "living room", "other room"]
        floors = ["Ground Floor"]
        min_floors = 1
        num_floors = get_integer(f"Is your home a single-level(1) or multi-level(2+)? Exclude crawlspaces and non-livable attics. \n", min_floors,100, "Input must be a number greater than 0.")
        if num_floors > 1:
            num_basements = get_integer(f"How many of those are below ground levels? \n",0,num_floors -1, f"Input must be a number less than {num_floors}.")
            if num_basements > 0:
                for basement_i in range(num_basements):
                    floors.insert(0,f"Basement {basement_i + 1}")
                upper_levels = (num_floors - num_basements) - 1
                for floor_i in range(upper_levels):
                    floors.append(f"Level {floor_i +2}")
            elif num_floors > 2:
                upper_levels = num_floors - 1
                for floor_i in range(upper_levels):
                    floors.append(f"Level {floor_i +2}")
            else:
                floors.append("Upstairs")
            print(f"Floors: {floors}")
        for floor in range(num_floors):
            for room_type_i in range(len(room_types)):
                num_rooms = get_integer(f"How many {room_types[room_type_i]}s in the {floors[floor]}? \n",0,100, "Input must be a number.")
                rooms = name_rooms(floors[floor], room_types[room_type_i], rooms, num_rooms)
        #num_bathrooms = int(input("How many bathrooms? "))
        #num_livingrooms = int(input("How many living rooms? "))
        #num_otherrooms = int(input("How many other rooms do you want to list? "))
        print(f"There are {len(rooms)} rooms to clean in your house. \n")
    #print(rooms)
    return rooms

def get_integer(prompt: str, min_value, max_value, error_message: str = "") -> int:
   while True:
       try:
            value = int(input(prompt))
            if value >= min_value and value <= max_value:
                return value
            else:
                print(error_message)
       except ValueError:
           print(error_message)

def name_rooms(floor, room_type, rooms, num_rooms):
    #print(f"Uniquely name the {room_type} in the {floor}.")
    for i in range(num_rooms):
        rooms.append(input(f"Name {room_type} {i+1}: \n"))
        while rooms[i].isspace() or rooms[i] == "":
            print("Room Name cannot be blank.")
            rooms.append(input(f"Name bedroom {i+1}:\n"))
    return rooms






    # room1 = "uniquely name the rooms on the ground floor. Currently labeled room1, enter to accept" if empty, name default. if name is already on list, "you can't use the same name twice"

        #can add more later
        #num_offices = int(input("How many office rooms are in your home?" ))
    #!! user draws ground floor layout and adds room labels to the canvas using draw rectangle()
    #!! user chooses which side of the house has the front door 
    # (this location is their start and dictates the order of the room task audit. 


def add_cleaning_tasks(rooms):
    tasks = []
    task = ""
    #reminders = []
    room_index = 0
    task_index = 0
    # Walk through
# closest to the front door is first, furthest is last)
    print("Walk through each room in your house and note what needs to be done. \n")
    for room in rooms:
        print(f"What needs to be done in the {room}? Add a task and press enter to add another. Press enter when done go to the next room.")
        tasks.append(f'Task #{task_index +1} {room}: {input()}')
        #print(tasks[len(tasks)-1])
        while tasks[len(tasks)-1] != f"Task #{task_index +1} {room}: ":
            task_index +=1
            print(f"What else needs to be done in the {room}?")
            task = tasks.append(f'Task #{task_index +1} {room}: {input()}')
            #reminders.append(input(f"When does {tasks[task_index]} to be done in the {room} room?" ))
            #print(tasks[len(tasks)-1])
            #print(f"tasks: {tasks}")
            '''for i, task in enumerate(tasks):
                print(f"Task {i}: {task} A")'''
        del tasks[len(tasks)-1]
        #print(tasks)
        '''for i, task in enumerate(tasks):
            tasks[i] = f"{room} Task #{i +1}: {task}"
            #print(f"Task {i}: {task} B")'''
        room_index +=1
    #print(f"rooms: {rooms}") 
    #print(f"tasks: {tasks}")
    '''for task in tasks:
        print(task)'''
    return tasks #, reminders

    #tasks.append(input(f"what needs to be done in the {rooms[room]} room?" ))




# TODO Set Up Your Basic Structure

# TODO Develop Task List Functionality

# TODO Create a Reminder System

# TODO Add Basic Statistics and Visual Indicators

# TODO Test Your Application

# TODO Improve and Expand

if __name__ == "__main__":
    main()