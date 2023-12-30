from bowling.scorer import Scorer


class Game:
    def __init__(self):
        self._its_current_frame = 1
        self._first_throw_in_frame = True
        self._its_scorer = Scorer()

    def score(self):
        return self.score_for_frame(self._its_current_frame)

    def add(self, pins):
        self._its_scorer.add_throw(pins)
        self._adjust_current_frame(pins)

    def _adjust_current_frame(self, pins):
        if self._last_ball_in_frame(pins):
            self._advance_frame()
        else:
            self._first_throw_in_frame = False

    def _last_ball_in_frame(self, pins):
        return self._strike(pins) or (not self._first_throw_in_frame)

    def _strike(self, pins):
        return self._first_throw_in_frame and pins == 10

    def _advance_frame(self):
        self._its_current_frame += 1
        self._its_current_frame = min(10, self._its_current_frame + 1)

    def score_for_frame(self, the_frame):
        return self._its_scorer.score_for_frame(the_frame)


