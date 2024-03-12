# HBNB clone - The Console

The HBNB Console is a command line interpreter that manages your AirBnB clone objects. This application allows you to create new objects (ex: User, Place), retrieve an object from a file, a database etc., do operations on objects (count, compute stats, etc.), update attributes of an object, and destroy an object.

## Features

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc.
- Do operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

## Installation

To install the HBNB Console, follow these steps:

```bash
git clone https://github.com/LCahid/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB_clone
```

## Usage

To launch the console application, navigate to the application directory and type `./console.py` or `python3 console.py` in your terminal. The prompt `(hbnb)` should appear, indicating that the console is running.

## Commands

The console supports various commands for data management:

**create**: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. `Usage: create <class name>`

**show**: Prints the string representation of an instance based on the class name and id. `Usage: show <class name> <id>`

**destroy**: Deletes an instance based on the class name and id (save the change into the JSON file). `Usage: destroy <class name> <id>`

**all**: Prints all string representation of all instances based or not on the class name. `Usage: all or all <class name>`

**update**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). `Usage: update <class name> <id> <attribute name> "<attribute value>"`

**quit or EOF**: Exit the console

***Examples***
```
(hbnb) create User
(hbnb) show User user_id
(hbnb) all User
(hbnb) update User user_id email "aibnb@holbertonschool.com"
(hbnb) destroy User user_id
```
We welcome contributions to the HBNB Console. To contribute, please fork the repository, create a new branch for your feature or bugfix, and submit a pull request.

## Classes

- `BaseModel`: Defines all common attributes/methods for other classes.
- `User`: User information.
- `State`: State information.
- `City`: City information relative to a state.
- `Amenity`: Amenity information.
- `Place`: Place information.
- `Review`: Review information.
