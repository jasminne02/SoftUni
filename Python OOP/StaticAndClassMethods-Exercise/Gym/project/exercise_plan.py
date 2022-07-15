class ExercisePlan:
    PERSONAL_ID = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.duration = duration
        self.equipment_id = equipment_id
        self.id = ExercisePlan.PERSONAL_ID
        ExercisePlan.PERSONAL_ID += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        return ExercisePlan.PERSONAL_ID

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
