from validators import time_to_minutes
from clash_detector import find_clashes


DAY_START = "08:00"
DAY_END = "18:00"


def find_free_slots(classes, day):
    day_classes = [
        c for c in classes
        if c.day.lower() == day.lower()
    ]

    day_classes.sort(
        key=lambda c: time_to_minutes(c.start_time)
    )

    free_slots = []
    current = time_to_minutes(DAY_START)

    for c in day_classes:
        start = time_to_minutes(c.start_time)
        end = time_to_minutes(c.end_time)

        if current < start:
            free_slots.append(
                f"{current // 60:02d}:{current % 60:02d} - "
                f"{start // 60:02d}:{start % 60:02d}"
            )

        current = max(current, end)

    end = time_to_minutes(DAY_END)

    if current < end:
        free_slots.append(
            f"{current // 60:02d}:{current % 60:02d} - "
            f"{end // 60:02d}:{end % 60:02d}"
        )

    return free_slots


def show_free_slots(classes, day):
    slots = find_free_slots(classes, day)

    print(f"\n--- Free Slots: {day.capitalize()} ---")

    if not slots:
        print("No free slots.")
    else:
        for slot in slots:
            print(slot)


def show_analytics(classes):

    total_hours = 0
    day_counts = {}

    for c in classes:
        start = time_to_minutes(c.start_time)
        end = time_to_minutes(c.end_time)

        total_hours += end - start
        day_counts[c.day] = day_counts.get(c.day, 0) + 1

    clashes = len(find_clashes(classes))

    busiest = "None"
    if day_counts:
        busiest = max(day_counts, key=day_counts.get)

    print("\n========== ANALYTICS ==========")
    print(f"Total classes     : {len(classes)}")
    print(f"Scheduled hours   : {total_hours / 60:.2f}")
    print(f"Total clashes     : {clashes}")
    print(f"Busiest day       : {busiest}")
    print("===============================")
