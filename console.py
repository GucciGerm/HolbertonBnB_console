#!/usr/bin/python3
"""
Command interpreter for managing objects


"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Creating a command interpreter that implents:

    quit & EOF: to exit the program
    help: given by default by cmd(updated and documented)
    custom prompt: (hbnb) ,
    an empty lin or ENTER shouldn't execute anything

    """
    prompt = "(hbnb) "
    methods = ["BaseModel", "Amenity", "User", "State",
               "City", "Place", "Review"]

    def emptyline(self):
        """
        Use emptyline to make sure command does not repeat itself
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if len(arg) < 1:
            print("** class name missing **")
            return False

        if arg not in self.models:
            print("** class name doesn't exist **")
            return False

        createit = eval("{}()".format(arg))
        createit.save()
        print(createit.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        if len(arg) < 1:
            print("** class name is missing **")
            return False

        cn = arg.split()[0]
        if cn not in self.methods:
            print("** class doesn't exist **")
            return False

        try:
            id = arg.split()[1]

        except BaseException:
            print("** instance id missing **")
            return False

        dictionary = storage.all()
        for key in dictionary:
            if key == "{}.{}".format(cn, id):
                print(dictionary[key])
                return False
        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if len(arg) < 1:
            print("** class name missing **")
            return False

        cn = arg.split()[0]
        if cn not in self.methods:
            print("** class doesn't exist **")
            return False

        try:
            id = arg.split()[1]

        except BaseException:
            print("** instance id missing **")
            return False

        dictionary = storage.all()

        for key in dictionary:
            if key == "{}.{}".format(cn, id):
                dictionary.pop(key)
                storage.save()
                return False
        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """
        if arg and arg not in self.methods:
            print("** class does't exist **")
            return False

        dictionary = storage.all()

        if arg:
            for key in dictionary:
                if key.startswith(arg):
                    print(dictionary[key])
            return False

        for element in self.methods:
            for key in dictionary:
                if key.startswith(arg):
                    print(dictionary[key])
            return False

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute (save the change
        into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        if len(arg) < 1:
            print("** class name missing **")
            return False

        cn = arg.split()[0]
        if cn not in self.methods:
            print("** class doesn't exist **")
            return False

        try:
            id = arg.split()[1]
        except BaseException:
            print("** instance id missing **")
            return False

        try:
            an = arg.split()[2]
        except BaseException:
            print("** atrribute name missing **")
            return False

        try:
            av = arg.split()[3]
        except BaseException:
            print("** value missing **")
            return False

        dictionary = storage.all()

        try:
            index = dictionary["{}.{}".format(cn, id)]
        except KeyError:
            print("** no instance found **")
            return False

        if av.isdecimal():
            setattr(index, an, int(av))
            storage.save()
        else:
            try:
                setattr(index, an, float(av))
                storage.save()
            except ValueError:
                setattr(index, an, av)
                storage.save()

    do_EOF = do_quit

if __name__ == "__main__":
    HBNBCommand().cmdloop()
