#!/usr/bin/python3
'''Something usful'''
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    '''Something more useful'''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        exit()

    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        exit()

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif not args[0] in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            zor = args[0] + "." + args[1]
            if zor not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[zor])

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif not args[0] in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            zor = args[0] + "." + args[1]
            if zor not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[zor]
                storage.save()

    def do_all(self, arg):
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(zor) for zor in storage.all().values()])

    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif not args[0] in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            zorkey = args[0] + "." + args[1]
            if zorkey not in storage.all():
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                elif len(args) < 4:
                    print("** value missing **")
                    return
                else:
                    zorobject = storage.all()[zorkey]
                    if args[3].isdigit():
                        value = int(args[3])
                    elif isfloat(args[3]):
                        value = float(args[3])
                    else:
                        value = str(args[3])
                    setattr(zorobject, args[2], value)
                    zorobject.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
