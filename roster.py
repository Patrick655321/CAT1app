import func
from schedule import schedule
input_day = ""
input_role = ""
input_shift = ""
user_input = ""
# snake_case for functions and variables
# - PascalCase for classes
# - ALL_CAPS for constant variables
# - _leading_underscore() for private methods
# - four spaces for indenting (which in VSCode can be applied with the tab key)
# - avoid extremely long lines (I am sometimes guilty of this one too)
# - use quotation marks consistently 
def leading_qs():
    input_day = input(str.lower("Which day are you working with? "))
    input_shift = input(str.lower("Which shift are you working with? "))
    input_role = input(str.lower("Which role are you working with? "))
    return input_day, input_role, input_shift

def _add_staff():
    leading_qs()
    test2 = input("Which staff would you like to add to this shift? ")
    schedule[input_day][input_shift][input_role] += [test2]

print(schedule["monday"]["day"])
_add_staff()
print(schedule["monday"]["day"])



