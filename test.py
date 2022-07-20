from fileinput import filename
import group
from schedule import schedule
import os
import csv

def save_roster():
    w = csv.writer(open(f"New Roster.csv", "w"))
    for key, val in schedule.items():
        w.writerow([key, val])

save_roster()
