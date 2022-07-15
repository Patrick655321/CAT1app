from noclassfunc import monday_day_req


def _which_day():
    day_input = str.lower(input("Which day would you like to view? "))
    return day_input

def _which_shift():
    shift_input = str.lower(input("Day or night shift?"))
    return shift_input

def _see_shift():
    if "mon" in _which_day():
        if "day" in _which_shift():
            print("This will be the roster for that shift")

_see_shift()
        
