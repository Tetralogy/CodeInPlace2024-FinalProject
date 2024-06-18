# CodeInPlace2024-FinalProject


Temp name: iClean

## Outline of Project

- [x] 1. input the rooms/areas in your house
    - [x] start with a simple list
    - [ ] make templates of common configurations to make onboarding faster
    - [ ] could expand to a map with a "heatmap" of tasks in each area
- [x] 2. iterate through the rooms and make a list of current things to clean
    - [x] mark tasks as done
    - [ ] persistent list between sessions
    - [ ] could also specify which part of the room to focus on when adding tasks
    - [ ] add item and desired frequency
    - [ ] a time estimate can be added, maybe also based on how dirty or cluttered the item/area is
- [ ] 3. set reminders that go off when a maintenance item is overdue
- [ ] 4. set priorities by ranking importance
- [ ] 5. statistics on each task/area
- [ ] 6. cleaning advice based on individual tasks
    - [ ] could be a chatbot / or an expert sourced list
    - [ ] relevan product recommendations and potentially $$$ affiliate referrals or subscriptions to monetize $$$
- [ ] 7. inventory of supplies needed and currently available in the house with reminders when low
- [ ] 8. gardening/outdoors maintanance expansion
- [ ] 9. GUI
- [ ] 10. gamification elements to make it not feel like a chore

### variables to keep track of
## house
- room_names
- room_zones
- layout
- supplies
- repairs
- upgrades

## user
- tasks
- deadlines or reminders
- schedule
- routines
- mood_energy


## TODO Improve and Expand

    # room1 = "uniquely name the rooms on the ground floor. Currently labeled room1, enter to accept" if empty, name default. if name is already on list, "you can't use the same name twice"

        #can add more later
    #!! user draws ground floor layout and adds room labels to the canvas using draw rectangle()
    #!! user chooses which side of the house has the front door 
    # (this location is their start and dictates the order of the room task audit. 

        #set_reminders()
    #set_priorities()

    # user interface
    #layout_map()
    #show_tasks()

