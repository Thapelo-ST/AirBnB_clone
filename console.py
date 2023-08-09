#!/usr/bin/python3
import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    console for the airbnb project
    """
    prompt = "(hbnb) "
    valid_class_names = ["BaseModel", "User"]

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
            return

        if arg not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

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

    def do_destroy(self, args):
        """
        deletes an instance based on the class name and id
        """
        arguments = args.split()
        if not arguments:
            print("** class name missing **")
            return

        name = arguments[0]
        if name not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        id = arguments[1]
        key = "{}.{}".format(name, id)
        all_objects = FileStorage.all(self)
        if key in all_objects:
            del all_objects[key]
            FileStorage.save(self)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        if not arg or arg in HBNBCommand.valid_class_names:
            all_objs = FileStorage.all(self)
            list_of_instances = []
            for key, obj in all_objs.items():
                if key.split('.')[0] == arg:
                    list_of_instances.append(str(obj))
            print(json.dumps(list_of_instances))
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        updates an instance based on class id and adding or updating attribute
        """
        arguments = args.split()
        if not arguments:
            print("** class name missing **")
            return

        name = arguments[0]
        if name not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        id = arguments[1]
        key = "{}.{}".format(name, id)
        all_objects = FileStorage.all(self)
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(arguments) < 4:
            print("** attribute missing **")
            return

        attribute_name = arguments[2]
        if len(arguments) < 4:
            print("** value missing **")
            return

        attribute_value = " ".join(arguments[3:])

        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]

        obj = all_objects[key]
        setattr(obj, attribute_name, attribute_value)

        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
