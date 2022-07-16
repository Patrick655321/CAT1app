import group
import seeshifts
from os import system

def roster_intro():
    print("Welcome to RosterRight, your one-stop anachronistic rostering service that noone will probably use!")
    print("According to shift prerequisites the following shifts require staff:")


def monday_day_req():
    if group.mon_day_staff != group.week_day_shift:
        print(f"""
        -Mon
        Management {group}
        Bar {group.week_day_shift["bar"] - group.mon_day_staff["bar"]}
        """)

def _main_menu():
    print("Please select from one of the following options:")
    print("1. See staff on shift")
    print("2. Add staff to shift")
    print("3. Remove staff from shift")
    print("4. Staff contact details")
    print("Enter 'main!' at any point to return to this menu")
    user_input = input("You may enter a number or quote the option:  ")
    if user_input == "1" or user_input == "See staff on shift":
        return seeshifts._see_shift()

def return_to_main():
    system('clear')


