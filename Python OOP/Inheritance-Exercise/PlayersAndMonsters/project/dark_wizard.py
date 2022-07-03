from project.wizzard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
