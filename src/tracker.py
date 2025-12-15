import time

class PerformanceTracker:
    def __init__(self):
        self.records = []

    def start_timer(self):
        return time.time()

    def stop_timer(self, start_time):
        return round(time.time() - start_time, 2)

    def log(self, correct, time_taken, difficulty):
        self.records.append({
            "correct": correct,
            "time": time_taken,
            "difficulty": difficulty
        })

    def accuracy(self):
        if not self.records:
            return 0
        correct_count = sum(1 for r in self.records if r["correct"])
        return correct_count / len(self.records)

    def average_time(self):
        if not self.records:
            return 0
        return sum(r["time"] for r in self.records) / len(self.records)
