class Frame:
    def __init__(self):
        self.its_score = 0

    def get_score(self):
        return self.its_score

    def add(self, pins: int):
        self.its_score += pins
