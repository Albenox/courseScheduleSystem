# schedule.py
# This file contains the Schedule class, which stores and searches course schedule items

class Schedule:
    def __init__(self):
        # Dictionary that stores all ScheduleItem objects
        self.courses = {}

    def add_entry(self, item):
        # Adds one ScheduleItem object into the dictionary using its unique key
        self.courses[item.get_key()] = item

    def print_header(self):
        # Prints the column headers for the course schedule
        print(f"{'Subject':<8}"
              f"{'Catalog':<9}"
              f"{'Section':<9}"
              f"{'Component':<11}"
              f"{'Session':<9}"
              f"{'Units':<8}"
              f"{'TotEnrl':<10}"
              f"{'CapEnrl':<10}"
              f"{'Instructor'}")

        print("-" * 90)

    def print(self):
        # Prints all courses in the dictionary
        self.print_header()

        for item in self.courses.values():
            item.print()

    def find_by_subject(self, subject):
        # Searches for courses by subject using a list comprehension
        return [item for item in self.courses.values()
                if item.subject.upper() == subject.upper()]

    def find_by_subject_catalog(self, subject, catalog):
        # Searches for courses by subject and catalog using a list comprehension
        return [item for item in self.courses.values()
                if item.subject.upper() == subject.upper()
                and item.catalog == catalog]

    def find_by_instructor_last_name(self, last_name):
        # Searches for courses by instructor last name using a list comprehension
        return [item for item in self.courses.values()
                if last_name.lower() in item.instructor.lower()]