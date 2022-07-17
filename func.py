from ast import Import
import group
import seeshifts
import addstaff
import removestaff
import contactdeets
from os import system

def roster_intro():
    print("Welcome to RosterRight, your one-stop anachronistic rostering service that noone will probably use!")
    print("According to shift prerequisites the following shifts require staff:")


def monday_day_req():
    if group.mon_day_staff != group.week_day_shift:
        print(f"""
        -Mon
        Management: {group.week_day_shift["mgr"] - group.mon_day_staff["mgr"]}
        Bar: {group.week_day_shift["bar"] - group.mon_day_staff["bar"]}
        Wait Staff: {group.week_day_shift["rest"] - group.mon_day_staff["rest"]}
        """)
user_input = ""
def _main_menu():
    while user_input != "exit":
        print("Please select from one of the following options:")
        print("1. See staff on shift")
        print("2. Add staff to shift")
        print("3. Remove staff from shift")
        print("4. Staff contact details")
        print("Enter 'main!' at any point to return to this menu")
        user_input = input("You may enter a number or quote the option:  ")
        if user_input == "1" or "see" in user_input.lower():
            return seeshifts._see_shift()
        elif user_input == "2" or "add" in user_input.lower():
            return addstaff.add_staff()
        elif user_input == "3" or "remove" in user_input.lower():
            return removestaff.remove_staff()
        elif user_input =="4" or "contact" in user_input.lower():
            return contactdeets.staff_deets
