import noclassgroup

def staff_deets():
    staff_list = list(noclassgroup.staff_avail.keys())
    for i in staff_list:
        print(i)
    detail_request = input("Which staff member are yout trying to reach?")
    print(detail_request)

staff_deets()

# >>> newdict = {1:0, 2:0, 3:0}
# >>> newdict.keys()
# [1, 2, 3]