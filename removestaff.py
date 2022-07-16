import group

onshift = {
    "mgr" : ["moe"],
    "bar" : [],
    "rest" : []
    }

staff_list = list(group.staff_avail.keys())

onshift = {
    "mgr" : ["moe"],
    "bar" : [],
    "rest" : []
    }

def remove_staff():
    remove = input(str.lower("Who would you like to remove from this shift? "))
    if remove in onshift["mgr"]:
        onshift["mgr"].remove(remove)
        return onshift

print(onshift)
remove_staff()
print(onshift)
