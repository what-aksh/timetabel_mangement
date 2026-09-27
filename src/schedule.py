class ClassEntry:

    def __init__(self, subject, day, start_time, end_time, room):
        self.subject = subject
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.room = room

    def display(self):
        print(f"Subject : {self.subject}")
        print(f"Day     : {self.day}")
        print(f"Time    : {self.start_time} - {self.end_time}")
        print(f"Room    : {self.room}")
