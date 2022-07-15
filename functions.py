import groupings

def roster_intro():
    print("Welcome to RosterHelper! Current empty shifts are:")
    print(f"""Monday: \nManager:{groupings.monday.day["manager"]} \nBartender:{groupings.monday.day["bar"]} \nWaiter:{groupings.monday.day["waiter"]} \nTotal: {groupings.mon_tot}""")




