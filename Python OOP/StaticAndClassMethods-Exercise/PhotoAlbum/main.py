import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages  # each page can contain 4 photos
        self.photos = [[] for page in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                photo_idx = self.photos[page].index(label)
                return f"{label} photo added successfully on page {page+1} slot {photo_idx+1}"
        return f"No more free slots"

    def display(self):
        result = f"{'-'*11}\n"
        for page in range(len(self.photos)):
            photos_count = len(self.photos[page])
            photos = '' if photos_count == 0 else ['[]'] * photos_count
            result += f"{' '.join(photos)}\n"
            result += f"{'-'*11}\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
