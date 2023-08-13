#!/usr/bin/python3
import cmd
import json

# from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    console for the airbnb project
    """
    prompt = "(hbnb) "
    valid_class_names = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with Ctrl+D and or Ctrl+Z"""
        print()
        return True

    def do_help(self, arg):
        """Display help message"""
        if arg:
            doc = getattr(self, "do_" + arg).__doc__
            if doc:
                print(doc)
        else:
            super().do_help(arg)

    def emptyline(self):
        """Do nothing in cases of an empty line pass"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a model"""
        if arg is None:
            print(" ** class name missing ** ")
            return

        if arg not in self.valid_class_names:
            print("** class doesn't exist **")
            return

        if arg == "User":
            new_instance = User()
        elif arg == "BaseModel":
            new_instance = BaseModel()
        elif arg == "State":
            new_instance = State()
        elif arg == "City":
            new_instance = City()
        elif arg == "Amenity":
            new_instance = Amenity()
        elif arg == "Place":
            new_instance = Place()
        elif arg == "Review":
            new_instance = Review()
        else:
            print("** class doesn't exist **")
            return

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.valid_class_names:
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arguments = arg.split()
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
# ============================================================

    def onecmd(self, line):
        """Modified onecmd to handle custom commands"""
        cmd, *args = line.split('.')

        if cmd in self.valid_class_names and args and args[0] == 'all()':
            self.do_all(cmd)
        elif cmd in self.valid_class_names and args and args[0] == 'count()':
            self.do_count(cmd)
        else:
            parts = line.split('.')
            if len(parts) == 2:
                class_name, func_with_args = parts
                func_parts = func_with_args.split('(')
                if len(func_parts) == 2:
                    func_name, args = func_parts
                    if args.endswith(')'):
                        arg_parts = args[:-1].split(',')
                        if func_name == "update":
                            if len(arg_parts) >= 3:
                                obj_id = arg_parts[0].strip().strip('"')
                                attr_name = arg_parts[1].strip().strip('"')
                                attr_value = arg_parts[2].strip().strip('"')
                                self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")
                            else:
                                print("** Missing arguments for update **")
                        elif func_name in ['show', 'destroy']:
                            obj_id = args[:-1].strip().strip('""')  # Remove the trailing ')'
                            if func_name == 'show':
                                self.do_show(f"{class_name} {obj_id}")
                            elif func_name == 'destroy':
                                self.do_destroy(f"{class_name} {obj_id}")
                        else:
                            return super().onecmd(line)
                    else:
                        return super().onecmd(line)
                else:
                    return super().onecmd(line)
            else:
                return super().onecmd(line)

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        class_name = arg.split()[0]

        if class_name in self.valid_class_names:
            all_objs = FileStorage.all(self)
            count = sum(1 for key in all_objs if key.startswith(class_name + "."))
            print(count)
        else:
            print("** class doesn't exist **")

    # ============================================================

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if len(args) == 0:
            all_objs = FileStorage.all(self)
            for obj_key in all_objs:
                print(all_objs[obj_key])
        elif not arg or arg in self.valid_class_names:
            all_objs = FileStorage.all(self)
            list_of_instances = []
            for key, obj in all_objs.items():
                if key.split('.')[0] == arg:
                    list_of_instances.append(str(obj))
            print(json.dumps(list_of_instances))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class id and adding or updating attribute"""
        arguments = arg.split()
        if not arguments:
            print("** class name missing **")
            return

        name = arguments[0]
        if name not in self.valid_class_names:
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
