#!/usr/bin/python3
"""this module contains the entry point of the command interpreter.

"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


hbnb_classes = {'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review
                }


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel, save it and
        print id."""

        if not arg:
            self.default("** class name missing **")
        elif arg not in hbnb_classes:
            self.default("** class doesn't exist **")
        else:
            model = hbnb_classes[arg]()
            model.save()
            print(model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""

        args = line.split()
        if len(args) < 1:
            self.default("** class name missing **")
        elif args[0] not in hbnb_classes:
            self.default("** class doesn't exist **")
        elif len(args) < 2:
            self.default("** instance id missing **")
        else:
            cls = args[0]
            Id = args[1]
            instance = cls + "." + Id
            instances = storage.all()
            if instance in instances:
                print(instances[instance])
            else:
                self.default("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""

        args = line.split()
        if len(args) < 1:
            self.default("** class name missing **")
        elif args[0] not in hbnb_classes:
            self.default("** class doesn't exist **")
        elif len(args) < 2:
            self.default("** instance id missing **")
        else:
            cls = args[0]
            Id = args[1]
            instance = cls + "." + Id
            instances = storage.all()
            if instance in instances:
                del instances[instance]
                storage.save()
            else:
                self.default("** no instance found **")

    def do_all(self, arg):
        """prints the list of all objects stored."""

        if arg and arg not in hbnb_classes:
            self.default("** class doesn't exist **")
        elif not arg:
            objs = storage.all()
            print([str(v) for v in objs.values()])
        elif arg:
            objs = storage.all()
            print([str(objs[k]) for k in objs if k.split('.')[0] == arg])

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute."""

        args = line.split()
        if len(args) < 1:
            self.default("** class name missing **")
        elif args[0] not in hbnb_classes:
            self.default("** class doesn't exist **")
        elif len(args) < 2:
            self.default("** instance id missing **")
        else:
            cls = args[0]
            Id = args[1]
            inst = cls + "." + Id
            instances = storage.all()
            if inst in instances:
                if len(args) < 3:
                    self.default("** attribute name missing **")
                
                """if dictionary of attrs is passed."""
                try:
                    if type(eval(args[2].replace("|", ' '))) is dict:
                        dict_attrs = eval(args[2].replace("|", ' '))
                        for attr, value in dict_attrs.items():
                            setattr(instances[inst], attr, value)
                        instances[inst].save()
                except NameError:
                    if len(args) < 4:
                        self.default("** value missing **")
                    else:
                        attr = args[2]
                        value = args[3]
                        if attr in instances[inst].__dict__:
                            setattr(instances[inst], attr, value)
                        else:
                            setattr(instances[inst], attr, value)
                        instances[inst].save()
            else:
                self.default("** no instance found **")

    def do_count(self, arg):
        """counts the number of instances a class has."""

        objs = storage.all()
        print(len([objs[k] for k in objs if k.split('.')[0] == arg]))

    def do_EOF(self, arg):
        """EOF(end of file) i.e Ctrl+D"""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def parseline(self, line):
        """Parse the line into a command name and a string containing
        the arguments.  Returns a tuple containing (command, args, line).
        'command' and 'args' may be None if the line couldn't be parsed."""

        parsed_tup = cmd.Cmd.parseline(self, line)
        tmp = parsed_tup[-1].split('.')
        if len(tmp) == 2:
            cmd_inst = tmp[1].split('(')
            if len(cmd_inst) < 2:
                return parsed_tup
            command = cmd_inst[0]
            inst = cmd_inst[1]
            cls = tmp[0]
            if len(inst) > 1:
                if command == 'update':
                    arg = inst.split('{')

                    """if dictionary of attrs is passed."""
                    if len(arg) == 2:
                        Id = arg[0][:-2].replace('"', '')
                        attrs = '{' + arg[1][:-1].replace(" ", '|')
                        line = f'{command} {cls} {Id} {attrs}'
                        return cmd.Cmd.parseline(self, line)

                    arg = inst.split(', ')
                    if len(arg) == 1:
                        Id = arg[0].replace('"', '')
                        line = f'{command} {cls} {Id}'
                    elif len(arg) == 2:
                        Id = arg[0].replace('"', '')
                        attr = arg[1].replace('"', '')
                        line = f'{command} {cls} {Id} {attr[:-1]}'
                    else:
                        Id = arg[0].replace('"', '')
                        attr = arg[1].replace('"', '')
                        val = arg[2].replace('"', '')
                        line = f'{command} {cls} {Id} {attr} {val[:-1]}'
                else:
                    line = f'{command} {cls} {inst[1:-2]}'
            else:
                line = f'{command} {cls}'
            parsed_tup = cmd.Cmd.parseline(self, line)
        return parsed_tup

    def emptyline(self):
        """Ignores when empty line or ENTER is being entered"""

        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.

        If this method is not overridden, it prints an error message and
        returns."""

        print(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
