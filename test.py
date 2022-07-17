from schedule import schedule
import func
user_input = ""




def _add_staff():
    _continue = "Y"
    while _continue == "Y":
        input_day = input(str.lower("Which day are you working with? "))
        input_shift = input(str.lower("Which shift are you working with? "))
        input_role = input(str.lower("Which role are you working with? "))
        test2 = input("Which staff would you like to add to this shift? ")
        schedule[str.lower(input_day)][str.lower(input_shift)][str.lower(input_role)] += [test2]
        _continue = input("Add more staff?")
    else:
        func._main_menu

_add_staff()
print(schedule["monday"]["day"])
# def leading_qs():
#     input_day = input(str.lower("Which day are you working with? "))
#     input_shift = input(str.lower("Which shift are you working with? "))
#     input_role = input(str.lower("Which role are you working with? "))
#     return input_day, input_role, input_shift