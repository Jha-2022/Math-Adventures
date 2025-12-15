
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

## 🧠 Adaptive Learning Approach
This prototype uses a **rule-based adaptive engine**:

- ✅ If the learner answers correctly and quickly → **Increase difficulty**
- ❌ If the learner answers incorrectly or slowly → **Decrease difficulty**
- ➖ Otherwise → **Maintain current difficulty**

Difficulty Levels:
- **Easy** → Simple addition / subtraction
- **Medium** → Mixed operations with larger numbers
- **Hard** → Multiplication / division or higher ranges

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

## Installtion Peocess:
### go through the given steps to install and use the above project: 

 - Enter the project directory
```
cd Math-Adventures
```
 - Cloning the repository:
```
git clone https://github.com/Jha-2022/Math-Adventures.git
```
 - Making a virtual environment for the peoject to download deliverables: 
```
python -m venv venv
```
 - Activating the python environment - windows
```
venv\Scripts\activate
```
 - Activating the python environment - mac, linux
```
source venv/bin/activate
```
### Now the user can access the project writting this command in the terminal:-
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


## Here I am attaching the github link to GUI version of the same webapp:-  
 ``` 
  https://github.com/Jha-2022/math-adventure-ai.git
 ```
## Live working demo for the same GUI version:-
 ```
 https://math-adventure-ai.vercel.app/
 ```
