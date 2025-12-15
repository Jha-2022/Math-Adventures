class AdaptiveEngine:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]

    def adapt(self, current_level, accuracy, avg_time):
        idx = self.levels.index(current_level)

        if accuracy >= 0.8 and avg_time < 5:
            idx = min(idx + 1, len(self.levels) - 1)

        elif accuracy <= 0.5:
            idx = max(idx - 1, 0)

        return self.levels[idx]
