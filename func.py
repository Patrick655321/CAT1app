import group
from schedule import schedule
import func


user_input = ""

def primary_input():
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        input_role = input(str.lower("Which role are you working with? "))


def _add_staff():
    _continue = "Y"
    while _continue.upper() != "N":
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        input_role = input(str.lower("Which role are you working with? "))
        test2 = input("Which staff would you like to add to this shift? ")
        schedule[str.lower(input_day)][str.lower(input_shift)][str.lower(input_role)] += [test2]
        _continue = input("Add more staff (Y/N)?")


def remove_staff():
    _continue = "Y"
    while _continue.upper() != "N":
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        input_role = input(str.lower("Which role are you working with? "))
        remove = input(str.lower("Who would you like to remove from this shift? "))
        if remove in schedule[input_day][input_shift][input_role]:
            schedule[input_day][input_shift][input_role].remove(remove)
        else:
            print("Invalid Input")
        _continue = input("Remove more staff (Y/N)?")

def _see_shift():
    _continue = "Y"
    while _continue.upper() != "N":
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        print(schedule[input_day][input_shift])
        _continue = input("View another shift?")
    else:
        _main_menu()



def roster_intro():
    print("Welcome to RosterRight, your one-stop anachronistic rostering service that noone will probably use!")

def _main_menu():
    user_input = "empty"
    while not "x" in user_input.lower():
        print("Please select from one of the following options:")
        print("1. See staff on shift")
        print("2. Add staff to shift")
        print("3. Remove staff from shift")
        print("4. Staff contact details")
        print("Enter 'main!' at any point to return to this menu. Type ")
        user_input = input("You may enter a number or quote the option:  ")
        if user_input == "1" or "see" in user_input.lower():
            return _see_shift()
        elif user_input == "2" or "add" in user_input.lower():
            return _add_staff()
        elif user_input == "3" or "remove" in user_input.lower():
            return remove_staff()
        elif user_input =="4" or "contact" in user_input.lower():
            return contactdeets.staff_deets
        else:
            print("\n\nInvalid Command\n------------\n")
    return exit

_main_menu()



