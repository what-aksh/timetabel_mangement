from timetable import Timetable
from clash_detector import display_clashes
from timetable_tools import show_free_slots, show_analytics


def show_menu():
    print("\n========== SMART TIMETABLE ==========")
    print("1. Add class")
    print("2. View timetable")
    print("3. Check clashes")
    print("4. Find free slots")
    print("5. Search class")
    print("6. Remove class")
    print("7. View analytics")
    print("8. Exit")
    print("====================================")


def main():

    timetable = Timetable()

    while True:

        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":

            subject = input("Enter subject: ")
            day = input("Enter day: ")
            start = input("Enter start time (HH:MM): ")
            end = input("Enter end time (HH:MM): ")
            room = input("Enter room: ")

            timetable.add_class(
                subject, day, start, end, room
            )

        elif choice == "2":

            timetable.view_timetable()

        elif choice == "3":

            display_clashes(timetable.get_classes())

        elif choice == "4":

            day = input("Enter day: ")
            show_free_slots(
                timetable.get_classes(),
                day
            )

        elif choice == "5":

            keyword = input("Enter subject to search: ")
            results = timetable.search_class(keyword)

            if not results:
                print("No matching classes found.")
            else:
                print("\nSearch results:")
                for c in results:
                    print(
                        f"{c.subject} | {c.day} | "
                        f"{c.start_time}-{c.end_time} | {c.room}"
                    )

        elif choice == "6":

            subject = input("Enter subject: ")
            day = input("Enter day: ")
            start = input("Enter start time (HH:MM): ")

            timetable.remove_class(
                subject, day, start
            )

        elif choice == "7":

            show_analytics(
                timetable.get_classes()
            )

        elif choice == "8":

            print("\nThank you for using Smart Timetable!")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
