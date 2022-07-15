class Trainer:
    PERSONAL_ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.PERSONAL_ID
        Trainer.PERSONAL_ID += 1

    @staticmethod
    def get_next_id():
        return Trainer.PERSONAL_ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
    