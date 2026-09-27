from validators import time_to_minutes


def find_clashes(classes):

    clashes = []

    for i in range(len(classes)):

        for j in range(i + 1, len(classes)):

            class1 = classes[i]
            class2 = classes[j]

            # Classes can clash only if they are on the same day
            if class1.day == class2.day:

                start1 = time_to_minutes(class1.start_time)
                end1 = time_to_minutes(class1.end_time)

                start2 = time_to_minutes(class2.start_time)
                end2 = time_to_minutes(class2.end_time)

                # Check if the two time periods overlap
                if start1 < end2 and start2 < end1:
                    clashes.append((class1, class2))

    return clashes


def display_clashes(classes):

    clashes = find_clashes(classes)

    if len(clashes) == 0:
        print("\nNo timetable clashes found.")
        return

    print("\n========== TIMETABLE CLASHES ==========")

    for class1, class2 in clashes:

        print(f"\nClash on {class1.day}")

        print(
            f"1. {class1.subject} | "
            f"{class1.start_time}-{class1.end_time} | "
            f"{class1.room}"
        )

        print(
            f"2. {class2.subject} | "
            f"{class2.start_time}-{class2.end_time} | "
            f"{class2.room}"
        )

    print("\n=======================================")
