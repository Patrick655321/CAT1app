
import group

def return_to_main():
    system('clear')
    main_menu()

onshift = {
    "mgr" : ["Moe"],
    "bar" : [],
    "rest" : []
    }

staff_list = list(group.staff_avail.keys())
manager = input(str("Who will be managing this shift? "))
bartender = input("Who will be tending the bar this shift? ")
waitstaff = input("Who will be the wait staff for this shift? ")
anyone_else = input("Anyone else? ")

def add_staff():
    if manager in staff_list and not manager in onshift:
        onshift["mgr"] += [manager]
        

    else:
        onshift["mgr"] = onshift["mgr"]
        return onshift


