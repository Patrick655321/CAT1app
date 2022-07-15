import noclassgroup

onshift = {
    "mgr" : [],
    "bar" : [],
    "rest" : []
    }

staff_list = list(noclassgroup.staff_avail.keys())
manager = input("Who will be managing this shift? ")
bartender = input("Who will be tending the bar this shift? ")
waitstaff = input("Who will be the wait staff for this shift? ")

def add_staff():
    if manager in staff_list and not manager in onshift:
        onshift["mgr"] = manager
        return onshift

add_staff()
