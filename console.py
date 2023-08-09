#!/usr/bin/python3
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    console for the airbnb project
    """
    prompt = "(hbnb) "
    valid_class_names = ["BaseModel", "OtherModel"]

    def do_quit(self, arg):
        """
        exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        exit the program with Ctrl+D
        """
        print()
        return True

    def do_help(self, arg):
        """
        Display help message
        """
        if arg:
            doc = getattr(self, "do_" + arg).__doc__
            if doc:
                print(doc)
        else:
            super().do_help(arg)

    def emptyline(self):
        """
        do nothing in cases of an empty line pass
        """
        return True

    def do_create(self, arg):
        """
        creates a new instance of a model
        """
        if arg is None:
            print(" ** class name missing ** ")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            print(" ---- ")
            print(new_instance)

    def do_show(self, arg):
        """
        prints string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            name = args[0]
            id = args[1]
            key = "{}.{}".format(name, id)
            all_objs = FileStorage.all(self)
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, name, id):
        """
        deletes an instance based on the class name and id
        """
        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(name, id)
            all_objs = FileStorage.all(self)
            if key in all_objs:
                del all_objs[key]
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        if not arg or arg in HBNBCommand.valid_class_names:
            all_objs = FileStorage.all(self)
            for key, obj in all_objs.items():
                print(obj)
        else:
            print(" ** class doesn't exist ** ")

    def do_update(self, name, id, attr_name, attr_value):
        """
        updates an instance based on class id and adding or updating attribute
        """
        if not name:
            print(" ** class name missing ** ")
        elif name not in HBNBCommand.valid_class_names:
            print(" ** class doesn't exist ** ")
        elif not id:
            print(" ** instance id missing ** ")
        elif not attr_name:
            print(" ** attribute name missing ** ")
        elif not attr_value:
            print(" ** value missing ** ")
        elif attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
            print(" ** attribute cannot be updated ** ")
        else:
            key = "{}.{}".format(name, id)
            all_objs = FileStorage.all(self)
            if key in all_objs:
                setattr(all_objs[key], attr_name, attr_value)
                all_objs[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
