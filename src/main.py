from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def main():
    print("🎮 Welcome to Math Adventures!")
    name = input("Enter your name: ")

    difficulty = input("Choose starting difficulty (Easy / Medium / Hard): ").title()
    if difficulty not in ["Easy", "Medium", "Hard"]:
        difficulty = "Easy"

    generator = PuzzleGenerator()
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()

    print(f"\nHello {name}! Let's begin...\n")

    for i in range(5):
        question, answer = generator.generate(difficulty)
        print(f"Puzzle {i+1} [{difficulty}]: {question}")

        start = tracker.start_timer()
        user_answer = input("Your answer: ")
        time_taken = tracker.stop_timer(start)

        try:
            correct = float(user_answer) == float(answer)
        except:
            correct = False

        tracker.log(correct, time_taken, difficulty)

        accuracy = tracker.accuracy()
        avg_time = tracker.average_time()

        difficulty = engine.adapt(difficulty, accuracy, avg_time)

        print("✅ Correct!" if correct else f"❌ Incorrect. Correct answer: {answer}")
        print(f"⏱ Time: {time_taken}s | 📊 Accuracy: {accuracy:.0%}")
        print(f"➡ Next Difficulty: {difficulty}\n")

    print("\n📘 Session Summary")
    print(f"Final Accuracy: {tracker.accuracy():.0%}")
    print(f"Average Response Time: {tracker.average_time():.2f} seconds")
    print(f"Recommended Next Level: {difficulty}")

if __name__ == "__main__":
    main()
