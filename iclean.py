# Outline Your Project
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

# user onboarding innitial setup
input_rooms()
add_cleaning_tasks()
set_reminders()
set_priorities()

# user interface
show_tasks()
update_tasks()


def input_rooms()
    #TODO
    num_floors = int(input("Is your home a single-level or multi-level?" ))
        #TODO validity check
        # get the total num floors excluding attic and other non-habitable areas
    # let's assume 3 levels: basement, ground, upstairs/level2
    # floor 1 - basement: How many rooms of each type
    num_bedrooms = int(input("How many bedrooms are in your home?" ))
    num_bathrooms = int(input("How many bathrooms are in your home?" ))
    num_livingrooms = int(input("How many living rooms are in your home?" ))
    num_offices = int(input("How many office rooms are in your home?" ))

    # Walk th



# TODO Set Up Your Basic Structure

# TODO Develop Task List Functionality

# TODO Create a Reminder System

# TODO Add Basic Statistics and Visual Indicators

# TODO Test Your Application

# TODO Improve and Expand