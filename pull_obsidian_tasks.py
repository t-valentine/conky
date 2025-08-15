#!/usr/bin/env python3
with open('/home/shared/OMSCS/2_AutomatedNotes/conky.md', 'r') as file:
    data = file.read().replace('\n', '')
# split data & get only the tasks
fileContents = data.split("%%")
taskArray = fileContents[2].split("- [ ] ")
clippedArray = taskArray[1:4] #excluding first blank item, only get 3 most recent To Dos
for task in clippedArray:
    onlyTask = task.split("📅")[0] # due dates are after a calendar emoji
    # over 40 characters will clip conky window, so if it's over 40 they get shortened w/ellipses
    # this is fine since conky window isn't the source of truth for tasks
    if len(onlyTask) > 40:
        print(f'- {onlyTask[:40]}...')
    else:
        print(f'- {onlyTask}') 