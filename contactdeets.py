import group

def staff_deets():
    staff_list = list(group.staff_avail.keys())
    for i in staff_list:
        print(i)
    detail_request = input("Which staff member are yout trying to reach?")
    if detail_request.lower() in group.staff_avail.keys():
        print(group.staff_avail[detail_request])

staff_deets()