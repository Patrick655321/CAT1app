

def monday_day_req():
    if group.mon_day_staff != group.week_day_shift:
        print(f"""
        -Mon
        Management: {group.week_day_shift["mgr"] - group.mon_day_staff["mgr"]}
        Bar: {group.week_day_shift["bar"] - group.mon_day_staff["bar"]}
        Wait Staff: {group.week_day_shift["rest"] - group.mon_day_staff["rest"]}
        """)