#!/usr/bin/python3
"""this module contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""

    prompt = '(hbnb) '
   

    def do_EOF(self, arg):
        """EOF(end of file) i.e Ctrl+D"""
        try:
            input()
        except EOFError:
            exit()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()


    def emptyline(self):
        """Method called when an empty line is entered in \
response to the prompt"""
        pass

if  __name__ == '__main__':
    HBNBCommand().cmdloop()