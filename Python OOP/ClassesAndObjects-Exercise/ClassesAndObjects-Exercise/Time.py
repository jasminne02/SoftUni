class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hours = str(self.hours)
        minutes = str(self.minutes)
        seconds = str(self.seconds)
        if int(hours) < 10:
            hours = '0' + hours
        if int(minutes) < 10:
            minutes = '0' + minutes
        if int(seconds) < 10:
            seconds = '0' + seconds
        return f"{hours}:{minutes}:{seconds}"

    def next_second(self):
        self.seconds += 1
        if self.seconds> Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
print()

time = Time(10, 59, 59)
print(time.next_second())
print()

time = Time(23, 59, 59)
print(time.next_second())
