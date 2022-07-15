import noclassgroup

def roster_intro():
    print("Welcome to RosterRight, your one-stop anachronistic rostering service that noone will probably use!")
    print("According to shift prerequisites the following shifts require staff:")


def monday_day_req():
    if noclassgroup.mon_day_staff != noclassgroup.week_day_shift:
        print(f"""Bar {noclassgroup.week_day_shift["bar"] - noclassgroup.mon_day_staff["bar"]}""")

def _main_menu():
    print("""
    - "1. See staff on shift"
    - "2. Add staff to shift"
    - "3. Remove staff from shift"
    - "4. Staff contact details"
    """)
    user_input_menu = input("What would you like to do? ")
    return user_input_menu



def staff_on_shift():
    pass

def main_menu():
    print("Please select from one of the following options:")
    print("1. See staff on shift")
    print("2. Add staff to shift")
    print("3. Remove staff from shift")
    print("4. Staff contact details")
    user_input = input("You may enter a number or quote the option:  ")
    if user_input == "1" or user_input == "See staff on shift":
        return staff_on_shift()
