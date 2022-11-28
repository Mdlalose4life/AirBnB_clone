#!/usr/bin/python3
"""This Program contains entry point for command interpreter"""

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
  prompt = "hbnb "

  clss = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity
  }

  clss1 = {
  	"State": State,
  	"City": City,
  	"Review": Review,
  	"place": Place
  	}


  clss.update(clss1)


def do_quit(self, line):
  """Does nothing."""
  return True


def emptyline(self):
  """ Called when the user enters the emptyline on the console"""
  pass


def do_EOF(self, line):
  """closes and exits the console"""
  print("")
  return True


def do_create(self, line):
  """Creates a new instance for the BaseModel"""

  line = line.split()

  if len(line) == 0:
    print("** class name missing **")
    return

  elif line[0] in HBNBCommand.clss:
    new_obj = HBNBCommand.clss[line[0]]()

  else:
    print("** class doesn't exist **")
    return

  new_obj.save()
  print(new_obj.id)


def do_show(self, line):
  """Prints instances based on class names and id"""

  line = line.split()

  if len(line) == 0:
    print("** class name missing **")
    return

  elif line[0] not in HBNBCommand.clss:
    print("** class doesn't exist **")
    return

  elif len(line) == 1:
    print("** instance id missing ** ")
    return

  else:
    bool = False
    compare = f"{line[0]}.{line[1]}"
    all_objs = storage.all()
    for key in all_objs.keys():
      if compare == key:
        bool == True
        print(all_objs[key])
        break

      if bool is False:
        print("** no instance found **")


def do_destroy(self, line):
  """Deletes an instance based on the class name and id"""

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
    compare = f"{line[0]}.{line[1]}"
    for key in storage.all():
      if compare == key:
        bool = True
        storage.all().pop(key)
        storage.save()
        break

    if bool is False:
      print("** no instance found **")


def do_all(self, line):
  """ Prints the string representation of instances
  based on the class name """

  line = line.split()
  list = []
  all_objs = storage.all()

  if len(line) == 0:
    for key, value in all_objs.items():
      list.append(str(value))
    print(list)

  elif len(line) == 1:
    if line[0] in HBNBCommand.clss:
      for key, value in all_objs.items():
        if line[0] in key:
          list.append(str(value))
      print(list)
    else:
      print("** class doesn't exist **")


def do_update(self, line):
  """ updates an instance based on the class name and id """

  line - line.split()

  if len(line) == 0:
    print("** class name missing **")
    return

  elif line[0] not in HBNBCommand.clss:
    print("** class doesn't exist **")
    return

  elif len(line) == 1:
    print("** instance id missing **")
    return

  compare = f"line{0}.{line[1]}"
  if compare in storage.all().key():
    if len(line) == 2:
      print("** attribute name missing **")
      return

    if len(line) == 3:
      print("** value missing **")
      return

    new_instance = storage.all()[compare]
    setattr(new_instance, line[2], line[3].strip('"'))
    storage.save()
  else:
    print("** no instance found **")
    return


def precmd(self, line):
  if "." in line:
    line = line.split(".")
    clase = line[0]
    line[1] = line[1].strip("()")
    command = line[1] + " " + clase
    return command
  return line


if __name__ == '__main__':
  HBNBCommand().cmdloop()

