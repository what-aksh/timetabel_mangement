from schedule import ClassEntry
from validators import DAYS, validate_day, validate_time_range, time_to_minutes


class Timetable:

    def __init__(self):
        self.classes = []

    def add_class(self, subject, day, start_time, end_time, room):

        if subject.strip() == "":
            print("Error: Subject cannot be empty.")
            return False

        if not validate_day(day):
            print("Error: Invalid day.")
            return False

        if not validate_time_range(start_time, end_time):
            print("Error: Invalid time range.")
            return False

        new_class = ClassEntry(
            subject,
            day.capitalize(),
            start_time,
            end_time,
            room
        )

        self.classes.append(new_class)

        print("Class added successfully!")
        return True

    def view_timetable(self):

        if len(self.classes) == 0:
            print("\nYour timetable is empty.")
            return

        print("\n========== WEEKLY TIMETABLE ==========")

        for day in DAYS:

            day_classes = []

            for class_entry in self.classes:
                if class_entry.day == day:
                    day_classes.append(class_entry)

            day_classes.sort(
                key=lambda x: time_to_minutes(x.start_time)
            )

            if len(day_classes) > 0:

                print(f"\n--- {day} ---")

                for class_entry in day_classes:
                    print(
                        f"{class_entry.start_time} - "
                        f"{class_entry.end_time} | "
                        f"{class_entry.subject} | "
                        f"{class_entry.room}"
                    )

        print("\n======================================")

    def search_class(self, keyword):

        results = []

        for class_entry in self.classes:

            if keyword.lower() in class_entry.subject.lower():
                results.append(class_entry)

        return results

    def search_by_day(self, day):

        results = []

        for class_entry in self.classes:

            if class_entry.day.lower() == day.lower():
                results.append(class_entry)

        return results

    def remove_class(self, subject, day, start_time):

        for class_entry in self.classes:

            if (
                class_entry.subject.lower() == subject.lower()
                and class_entry.day.lower() == day.lower()
                and class_entry.start_time == start_time
            ):

                self.classes.remove(class_entry)

                print("Class removed successfully!")
                return True

        print("Class not found.")
        return False

    def get_classes(self):
        return self.classes
