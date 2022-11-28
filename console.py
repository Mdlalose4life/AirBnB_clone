#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""

import models
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    clss = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "User": User
    }
    
    clss_1 = {
    "State": State,
    "City": City,
    "Review": Review,
    "Place": Place
    }

    clss.update(clss_1)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass
        
    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        line = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return

        elif line[0] in HBNBCommand.clss:
            new_obj = HBNBCommand.clss[arg[0]]()

        else:
            print("** class doesn't exist **")
            return
            
        new_obj.save()
        print(new_obj.id)
    
    def do_show(self, line):
        """Prints the string representation of an instance"""

        line = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return

        elif line[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
            return

        elif len(line) == 1:
            print("** instance id missing **")
            return

        else:
            bool = False
            compare = f"{arg[0]}.{arg[1]}"
            all_objs = storage.all()
            for key in all_objs.keys():
                if compare == key:
                    bool = True
                    print(all_objs[key])
                    break

            if bool is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
            return

        elif len(arg) == 1:
            print("** instance id missing **")
            return

        else:
            bool = False
            compare = f"{arg[0]}.{arg[1]}"
            for key in storage.all():
                if compare == key:
                    bool = True
                    storage.all().pop(key)
                    storage.save()
                    break

            if bool is False:
                print("** no instance found **")

    def do_all(self, line):
        """Prints string representation of all instances
        based or not on the class name."""

        line = line.split()
        list = []
        my_objs = storage.all()

        if len(line) == 0:
            for each_key, each_value in my_objs.items():
                list.append(str(each_value))
            print(list)

        elif len(line) == 1:
            if arg[0] in HBNBCommand.clss:
                for each_key, each_value in my_objs.items():
                    if line[0] in each_key:
                        list.append(str(each_value))
                print(list)
            else:
                print("** class doesn't exist **")
                
    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        line = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return

        elif line[0] not in HBNBCommand.clss:
            print("** class doesn't exist **")
            return

        elif len(line) == 1:
            print("** instance id missing **")
            return

        compare = f"{arg[0]}.{arg[1]}"
        if compare in storage.all().keys():
            if len(line) == 2:
                print("** attribute name missing **")
                return

            if len(line) == 3:
                print("** value missing **")
                return

            new_instance = storage.all()[compare]
            setattr(new_instance, arg[2], arg[3].strip('"'))
            storage.save()
        else:
            print("** no instance found **")
            return
            
    def precmd(self, line):
        if "." in line:
            line = line.split(".")
            clase = args[0]
            args[1] = args[1].strip("()")
            command = args[1] + " " + clase
            return command
        return line
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
