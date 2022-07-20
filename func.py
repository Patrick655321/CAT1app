from fileinput import filename
import group
from schedule import schedule
import os
import csv
import time

def get_day():
    day = input(str.lower("Which day are you working with? "))
    return day

def get_shift():
    shift = input(str.lower("Which shift are you working with? "))
    return shift

def get_role():
    role = input(str.lower("Which role are you working with? "))
    return role

def frontend():
    print("Welcome to RosterRight, your one-stop anachronistic rostering service!")
    print("Please select from one of the following options:")
    print("1. See staff on shift")
    print("2. Add staff to shift")
    print("3. Remove staff from shift")
    print("4. Staff contact details")
    print("5. Export roster to Latest Roster File")
    print("Type 'exit' to exit program.")

def _add_staff():
    _continue = "Y"
    while _continue.upper() != "N":
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        input_role = input(str.lower("Which role are you working with? "))
        test2 = input("Which staff would you like to add to this shift? ")
        schedule[input_day][input_shift][input_role] += [test2]
        _continue = input("Add more staff (Y/N)?")
    os.system('cls')
    _main_menu()


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
    os.system('cls')
    _main_menu()

def _see_shift():
    _continue = "Y"
    while _continue.upper() != "N":
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        print(schedule[input_day][input_shift])
        _continue = input("View another shift?")
    os.system('cls')
    _main_menu()

def staff_deets():
    _continue = "Y"
    while _continue.upper() != "N":
        staff_list = list(group.staff_avail.keys())
        for i in staff_list:
            print(str.capitalize(i))
        detail_request = input("Which staff member are yout trying to reach?")
        if detail_request.lower() in group.staff_avail.keys():
            print(group.staff_avail[detail_request.lower()])
        _continue = input("View another shift?")
    os.system('cls')
    _main_menu()

def save_roster():
    w = csv.writer(open(f"New Roster.csv", "w"))
    for key, val in schedule.items():
        w.writerow([key, val])

def _main_menu():
    user_input = "empty"
    while not "x" in user_input.lower():
        frontend()
        user_input = input("You may enter a number or quote the option:  ")
        if user_input == "1" or "see" in user_input.lower():
            return _see_shift()
        elif user_input == "2" or "add" in user_input.lower():
            return _add_staff()
        elif user_input == "3" or "remove" in user_input.lower():
            return remove_staff()
        elif user_input =="4" or "contact" in user_input.lower():
            return staff_deets()
        elif user_input =="5" or "save" in user_input.lower():
            save_roster()
        elif not "x" in user_input:
            os.system('cls')
            print("\n\nInvalid Command\n------------\n")
            time.sleep(1)
    return quit()

_main_menu()