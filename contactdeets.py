import noclassgroup

def staff_deets():
    staff_list = list(noclassgroup.staff_avail.keys())
    for i in staff_list:
        print(i)
    detail_request = input("Which staff member are yout trying to reach?")
    if "moe" in detail_request:
        print(noclassgroup.moe_deets)

staff_deets()
