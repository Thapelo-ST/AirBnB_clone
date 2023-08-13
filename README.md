# AirBnB Clone (The Console)

Welcome to the AirBnB clone console! This is the main engine of the project, allowing you to interact with and manage objects through a command-line interface.

## Description of the Command Interpreter

The AirBnB clone console provides a command-line interface for interacting with objects in your project. You can create, retrieve, update, and delete instances of various classes, such as `BaseModel`, `User`, `State`, and more.

The console supports the following commands:
- `all <class_name>`: Displays all instances of the specified class or all classes if no class name is provided.
- `count <class_name>`: Counts the number of instances of the specified class.
- `show <class_name> <id>`: Displays the details of an instance based on its class name and ID.
- `destroy <class_name> <id>`: Deletes an instance based on its class name and ID.
- `<class_name>.update(<id>, <attribute_name>, <attribute_value>)`: Updates an instance's attribute based on its class name, ID, attribute name, and new value.

## How to Start the Console

To start the console, simply run the `console.py` file using Python:

$ python console.py


## How to Use the Console

Once the console is running, you can enter various commands to interact with your objects. The general format for commands is:

  (hbnb) <command>


Where `<command>` is one of the commands mentioned above.

For the `update` command, you should use the following format:

(hbnb) <class_name>.update(<id>, <attribute_name>, <attribute_value>)

Replace `<class_name>`, `<id>`, `<attribute_name>`, and `<attribute_value>` with the appropriate values.

## Examples

- To create an instance:

(hbnb) create class-name

example: create User


- To display all instances of a class:

(hbnb) all class-name

example: (hbnb) all BaseModel

or 

(hbnb) class-name.all()

example: (hbnb) User.all()

- To count the number of instances of a class:

(hbnb) count class name

example: (hbnb) count BaseModel

or 

(hbnb) class-name.count()

example: (hbnb) BaseModel.count()


- To display the details of an instance:

(hbnb) show class-name id

(hbnb) show BaseModel 6d954471-d02f-4a0a-a13e-cc77533aca50

or 

(hbnb) class-name.show(id)

example: (hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")


- To update an instance's attribute:

(hbnb) class-name.update(id, attribute name, attribute value)

example: (hbnb)  User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")

or 

(hbnb) update class-name id attribute name "attribute value"

example: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"


- To destroy an instance

(hbnb) destroy class-name id

example: (hbnb) destroy User 38f22813-2753-4d42-b37c-57a17f1e4f88

or 

(hbnb) destroy.class-name(id)

example: (hbnb) destroy.User("38f22813-2753-4d42-b37c-57a17f1e4f88")


Remember to replace the placeholders with actual values when using these commands.


Enjoy using the AirBnB clone console to manage your objects efficiently!
