
import group


onshift = {
    "mgr" : [],
    "bar" : [],
    "rest" : []
    }

staff_list = list(group.staff_avail.keys())
# _bartender = input("Who will be tending the bar this shift? ")
# _waitstaff = input("Who will be the wait staff for this shift? ")
# _anyone_else = input("Anyone else? ")

def _which_day():
    day_input = str.lower(input("Which day would you like to view? "))
    return day_input

def _which_shift():
    shift_input = str.lower(input("Day or night shift?"))
    return shift_input

def add_staff():
    _which_day()
    _which_shift()

    if int(len(onshift["mgr"]) < int(group.week_day_shift["mgr"])):
        _manager = input(str("Who will be managing this shift? "))
        if _manager in staff_list and not _manager in onshift:
            onshift["mgr"] += [_manager]
        else:
            onshift["mgr"] = onshift["mgr"]
        return onshift








