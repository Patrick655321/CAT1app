import schedule



def test1():
    test2 = input("testing: ")
    schedule.schedule["monday"]["day"]["manager"] += [test2]

# test1()
print(schedule.schedule["monday"]["day"])

        # _manager = input(str("Who will be managing this shift? "))
        #  _manager in staff_list and not _manager in onshift:
        #     onshift["mgr"] += [_manager]