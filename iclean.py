DONETAG = "IS DONE!"

def main():
    # user onboarding innitial setup
    rooms = input_rooms()
    tasks = add_cleaning_tasks(rooms)
    # task completion loop
    todo_list(tasks)
    # all tasks done: quit
    print("Go take a nap!")
    print("Bye!")

def input_rooms():
    print("Welcome to iClean task manager. Let's note what needs to be done in your house.")
    scope = get_integer(f"Do you want to focus on one room(1) or your whole house(2)? \n", 1,2, "Input must be 1 or 2.")
    if scope == 1:
        rooms = [input(f"What room are you cleaning? \n")]
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
        print(f"There are {len(rooms)} rooms to clean in your house. \n")
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
    for i in range(num_rooms):
        rooms.append(input(f"Name {room_type} {i+1}: \n"))
        while rooms[i].isspace() or rooms[i] == "":
            print("Room Name cannot be blank.")
            rooms.append(input(f"Name bedroom {i+1}:\n"))
    return rooms

def add_cleaning_tasks(rooms):
    tasks = []
    room_index = 0
    task_index = 0
    # Walk through
    print("Walk through each room in your house and note what needs to be done. \n")
    for room in rooms:
        print(f"What needs to be done in the {room}? Add a task and press enter to add another. Press enter when done go to the next room.")
        tasks.append(f'Task #{task_index +1} {room}: {input()}')
        while tasks[len(tasks)-1] != f"Task #{task_index +1} {room}: ":
            task_index +=1
            print(f"What else needs to be done in the {room}?")
            tasks.append(f'Task #{task_index +1} {room}: {input()}')
        del tasks[len(tasks)-1]
        room_index +=1
    return tasks

def todo_list(tasks):
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
        if task_done <= len(tasks):
            if f"{tasks[task_done -1]}" not in tasks_done:
                tasks_done.append(f"{tasks[task_done -1]} {DONETAG}")
                num_tasks_remaining = len(tasks) - len(tasks_done)
                tasks[task_done -1] = f"{tasks[task_done -1]} {DONETAG}"
        else:
            print(f"Task #{task_done} is not on the list. \nThere are only {len(tasks)} tasks on the list. \nAdd more next time.")
    print("Done:")
    for task in tasks_done:
        print(task)
    print()
    print("No more tasks to complete!")
    print()

if __name__ == "__main__":
    main()