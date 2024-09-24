# Star Wars Legion Army List Builder

A GUI-based army list builder application for the Star Wars Legion miniatures game, built using Python's Tkinter library. This app allows users to create, manage, save, and load army lists for different factions. It provides a user-friendly interface for selecting units, adding upgrades, and managing army lists for the game.

I built this as a challenge to practice Python's Tkinter library and learn how to manage UI state and an OOP structure.

## Features

* Select a faction and build an army list.
* Save army lists to a file.
* Load previously saved army lists.
* View unit details and available upgrades.
* Filter upgrades based on unit type, faction, and other restrictions.

## Requirements

* Python 3.x
* Tkinter (Python's standard GUI library)
* Pillow (for handling images)
* Pickle (for saving and loading lists)
* Requests (for fetching images from URLs)

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/legion-army-builder.git
cd legion-army-builder
```

2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the app:
```
python3 main.py
```

2. Building a List:
* Start by selecting a faction.
* Add units from the available options, with each unit displaying details like type and points.
* Customize units by adding upgrades.
* Save your army list using the Save button, where you can provide a name for the army list.
* Load a previously saved army list by clicking the Load button and selecting the file.

3. Saving and loading lists:
* Saved lists are stored as `.pkl` files.
* Lists can be reloaded at any time using the **Load List** button on the main menu.
