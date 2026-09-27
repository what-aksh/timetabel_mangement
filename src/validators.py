DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


def validate_subject(subject):
    """Check that the subject name is not empty."""
    return subject.strip() != ""


def validate_day(day):
    """Check whether the day is valid."""
    return day.strip().capitalize() in DAYS


def validate_time(time):
    """Check whether time follows HH:MM format."""
    try:
        hours, minutes = map(int, time.split(":"))

        if hours < 0 or hours > 23:
            return False

        if minutes < 0 or minutes > 59:
            return False

        return True

    except (ValueError, AttributeError):
        return False


def time_to_minutes(time):
    """Convert HH:MM time into total minutes."""
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def validate_time_range(start_time, end_time):
    """Check that both times are valid and end time is after start time."""
    if not validate_time(start_time):
        return False

    if not validate_time(end_time):
        return False

    start = time_to_minutes(start_time)
    end = time_to_minutes(end_time)

    return start < end
