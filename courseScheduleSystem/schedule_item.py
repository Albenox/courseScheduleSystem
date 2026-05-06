# schedule_item.py
# This file contains the ScheduleItem class, which stores information for one course

from dataclasses import dataclass


@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    total_enrolled: int
    capacity_enrolled: int
    instructor: str

    def get_key(self):
        # Creates a unique dictionary key using subject, catalog, and section
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        # Prints one course row in a formatted way
        print(f"{self.subject:<8}"
              f"{self.catalog:<9}"
              f"{self.section:<9}"
              f"{self.component:<11}"
              f"{self.session:<9}"
              f"{self.units:<8}"
              f"{self.total_enrolled:<10}"
              f"{self.capacity_enrolled:<10}"
              f"{self.instructor}")