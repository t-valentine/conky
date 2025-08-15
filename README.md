# conky

Conky config file, python script, and bash script for my student profile. Config file includes boring stuff like the current academic calendar and big assignments due. The python script pulls text from an Obsidian markdown file (more on this below). The script just starts conky w/the correct config file.

## Obsidian

`pull_obsidian_tasks.py` gets data from a Markdown file in my local [Obsidian]() vault. This file pulls all weekly to-do items from my tasks using the following custom plugins:

- Dataview
- Dataview Publisher
- Tasks

My `conky.md` file is in a folder named `2_AutomatedNotes`. That whole folder has been excluded from the dataview query- if conky.md is included, then the combo of the dataview & tasks plugins will create duplicate tasks. Here is the contents of that markdown file:

````
%% DATAVIEW_PUBLISHER: start
```dataview
TASK
FROM -"2_AutomatedNotes"
WHERE !completed
```
%%
<this is where your markdown will publish>
%% DATAVIEW_PUBLISHER: end %%
````
