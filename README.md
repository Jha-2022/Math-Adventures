
# Math-Adventures

## 📘 Overview
**Math Adventures** is a minimal AI-powered adaptive learning prototype designed for children aged **5–10 years**.  
The system dynamically adjusts the difficulty of math puzzles based on the learner’s performance, keeping them in an optimal challenge zone.

This project demonstrates how **adaptive logic** (rule-based or lightweight ML-inspired logic) can personalize learning experiences in real time.


---

## 🎯 Objective
The goal of this project is to build a prototype that:

- Generates math puzzles dynamically
- Tracks user performance (accuracy and response time)
- Automatically adapts difficulty level
- Displays a performance summary at the end of the session

> **Focus:** Adaptive logic and reasoning, not UI or visuals.

---


## Directory Structure
```
📂 Math-Adventures
  ├─ README.md               
  ├─ requirements.txt       
  ├─ src/
    ├─ main.py               
    ├─ puzzle_generator.py   
    ├─ tracker.py            
    └─ adaptive_engine.py  
```

## Installtion Peocess
```
cd Math-Adventures
```
```
git clone https://github.com/Jha-2022/Math-Adventures.git
```
```
python -m venv venv
```
```
venv\Scripts\activate
```

```
source venv/bin/activate
```
now run
```
python src/main.py
```


## 🔄 Example User Flow
1. User enters name and selects an initial difficulty level  
2. A math puzzle is displayed  
3. System records:
   - Correctness
   - Time taken to respond  
4. Adaptive engine decides the next difficulty  
5. After the session, a performance summary is shown

