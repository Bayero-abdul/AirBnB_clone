#!/usr/bin/python3
"""this module contains the entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""

    def do_EOF(self, arg):
        """end of file i.e ctrl+d"""
        try:
            input()
        except EOFError:
            exit()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def create:
        if ARG(CLASSNAME)
            create a BASEMODEL INSTANCE
            SAVE it to the json file
            print ID
        else if If the class name is missing:
            print ** class name missing **
        else if class name does not exist:
            print ** class doesn't exist **



    def emptyline(self):
        """Ignores when empty line or ENTER is being pressed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
