from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room_number == room.number:
                check = room.take_room(people)
                if check:
                    return
                self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room.number:
                guest = room.guests
                check = room.free_room()
                if check:
                    return
                self.guests -= guest

    def status(self):
        free_rooms = []
        taken_rooms = []

        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
            else:
                free_rooms.append(room.number)

        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(str(x) for x in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"
