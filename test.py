from fileinput import filename
import group
from schedule import schedule
import os
import csv
import time


def _create_staff():
    new_name = input("What is the name of the staff member you wish to create?")
    if not new_name in group.staff_avail.keys():
        full_name = input("Please type complete name  you wish to appear in the database:  ")
        phone_no = input("Please enter their phone number:  ")
        email_add = input("Please enter a valid email address for staff:  ")
        group.staff_avail[new_name] = [full_name, phone_no, email_add]
    return group.staff_avail
_create_staff()
