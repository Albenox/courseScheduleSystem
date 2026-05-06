# main.py
# This file drives the program and loads the CSV data

import csv
from schedule import Schedule
from schedule_item import ScheduleItem


def load_courses(filename):
    schedule = Schedule()

    with open(filename, encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            item = ScheduleItem(
                row["Subject"],
                row["Catalog"],
                row["Section"],
                row["Component"],
                row["Session"],
                int(row["Units"]),
                int(row["TotEnrl"]),
                int(row["CapEnrl"]),
                row["Instructor"]
            )

            schedule.add_entry(item)

    return schedule


if __name__ == "__main__":
    filename = "STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv"
    schedule = load_courses(filename)
    schedule.print()

    input("Press Enter to exit...")