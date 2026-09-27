from validators import time_to_minutes
from clash_detector import find_clashes


DAY_START = "08:00"
DAY_END = "18:00"


def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    return f"{hours:02d}:{minutes:02d}"


def find_free_slots(classes, day):

    day_classes = []

    for class_entry in classes:
        if class_entry.day.lower() == day.lower():
            day_classes.append(class_entry)

    if len(day_classes) == 0:
        return [(DAY_START, DAY_END)]

    day_classes.sort(
        key=lambda x: time_to_minutes(x.start_time)
    )

    free_slots = []
    current_time = time_to_minutes(DAY_START)

    for class_entry in day_classes:

        start = time_to_minutes(class_entry.start_time)
        end = time_to_minutes(class_entry.end_time)

        if current_time < start:
            free_slots.append(
                (
                    minutes_to_time(current_time),
                    minutes_to_time(start)
                )
            )

        if end > current_time:
            current_time = end

    end_of_day = time_to_minutes(DAY_END)

    if current_time < end_of_day:
        free_slots.append(
            (
                minutes_to_time(current_time),
                minutes_to_time(end_of_day)
            )
        )

    return free_slots


def display_free_slots(classes, day):

    free_slots = find_free_slots(classes, day)

    print(f"\n========== FREE SLOTS - {day.capitalize()} ==========")

    if len(free_slots) == 0:
        print("No free slots found.")
        return

    for start, end in free_slots:
        print(f"{start} - {end}")

    print("======================================")


def total_classes(classes):
    return len(classes)


def total_scheduled_hours(classes):

    total_minutes = 0

    for class_entry in classes:

        start = time_to_minutes(class_entry.start_time)
        end = time_to_minutes(class_entry.end_time)

        total_minutes += end - start

    return round(total_minutes / 60, 2)


def total_clashes(classes):

    clashes = find_clashes(classes)

    return len(clashes)


def busiest_day(classes):

    if len(classes) == 0:
        return "No classes"

    day_counts = {}

    for class_entry in classes:

        day = class_entry.day

        if day not in day_counts:
            day_counts[day] = 0

        day_counts[day] += 1

    busiest = max(day_counts, key=day_counts.get)

    return busiest


def display_analytics(classes):

    print("\n========== TIMETABLE ANALYTICS ==========")

    print(f"Total classes       : {total_classes(classes)}")
    print(f"Scheduled hours     : {total_scheduled_hours(classes)}")
    print(f"Timetable clashes   : {total_clashes(classes)}")
    print(f"Busiest day         : {busiest_day(classes)}")

    print("==========================================")
