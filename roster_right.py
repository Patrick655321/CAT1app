import group
from schedule import schedule
import os
import csv
import time


def _shift_funnel():
    input_day = input(str.lower("Which day are you working with? "))
    input_shift = input(str.lower("Which shift are you working with? "))
    input_role = input(str.lower("Which role are you working with? "))
        #return the 3 inputs in a list
    return [input_day, input_shift, input_role]


def frontend():
    print("Welcome to Roster-Right, your one-stop anachronistic rostering service!")
    print("Please select from one of the following options:")
    print("1. See staff on shift")
    print("2. Add staff to shift")
    print("3. Remove staff from shift")
    print("4. Staff contact details")
    print("5. Create a new staff member profile")
    print("6. Export roster to 'Latest Roster' File")
    print("Type 'exit' to exit program.")

def _add_staff():
    _continue = "Y"
    while _continue.upper() != "N":
        funnel_info = _shift_funnel()
        add_staff = input("Which staff would you like to add to this shift? ")
        if str.lower(add_staff) in group.staff_avail:
            try:
                schedule[str.lower(funnel_info[0])][str.lower(funnel_info[1])][str.lower(funnel_info[2])].append(add_staff)
            except KeyError:
                print("Please check your spelling and try again")
            _continue = input("Add more staff (Y/N)?")
    os.system('clear')
    main_menu()

def _remove_staff():
    _continue = "Y"
    while _continue.upper() != "N":
        funnel_info = _shift_funnel()
        remove = input(str.lower("Who would you like to remove from this shift? "))
        if str.lower(remove) in schedule[funnel_info[0]][funnel_info[1]][funnel_info[2]]:
            try:
                schedule[str.lower(funnel_info[0])][str.lower(funnel_info[1])][str.lower(funnel_info[2])].remove(str.lower(remove))
            except KeyError:
                print("Please check your spelling and try again")
        _continue = input("Remove more staff (Y/N)?")
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

def _see_shift():
    _continue = "Y"
    while _continue.upper() != "N":
        funnel_info = _shift_funnel()
        try:
            print(schedule[str.lower(funnel_info[0])][str.lower(funnel_info[1])])
        except KeyError:
            print("Please check your spelling and try again")
        _continue = input("View another shift?")
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

def _staff_deets():
    _continue = "Y"
    while _continue.upper() != "N":
        staff_list = list(group.staff_avail.keys())
        for i in staff_list:
            print(str.capitalize(i))
        detail_request = input("Which staff member are yout trying to reach?")
        if detail_request.lower() in group.staff_avail.keys():
            try:
                print(group.staff_avail[detail_request.lower()])
            except KeyError:
                print("Please check your spelling and try again")
        _continue = input("View another shift?")
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

def _create_staff():
    new_name = input("What is the name of the staff member you wish to create?")
    if not new_name in group.staff_avail.keys():
        full_name = input("Please type complete name  you wish to appear in the database:  ")
        phone_no = input("Please enter their phone number:  ")
        email_add = input("Please enter a valid email address for staff:  ")
        group.staff_avail[new_name] = [full_name, phone_no, email_add]
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

def save_roster():
    w = csv.writer(open(f"New Roster.csv", "w"))
    for key, val in schedule.items():
        w.writerow([key, val])

def main_menu():
    user_input = "empty"
    while not "x" in user_input.lower():
        frontend()
        user_input = input("You may enter a number or quote the option:  ")
        if user_input == "1" or "see" in user_input.lower():
            return _see_shift()
        elif user_input == "2" or "add" in user_input.lower():
            return _add_staff()
        elif user_input == "3" or "remove" in user_input.lower():
            return _remove_staff()
        elif user_input =="4" or "contact" in user_input.lower():
            return _staff_deets()
        elif user_input == "5" or "create" in user_input.lower():
            return _create_staff()
        elif user_input =="6" or "save" in user_input.lower():
            save_roster()
        elif not "x" in user_input:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\nInvalid Command\n------------\n")
            time.sleep(1)
    return quit()

main_menu()