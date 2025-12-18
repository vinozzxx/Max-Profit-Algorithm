# 🚀 Max Profit Problem – Python Application

A **Python-based solution** for the **Max Profit optimization problem**, built as part of an interview assignment. The project calculates the **optimal mix of properties** (Theatres, Pubs, Commercial Parks) to **maximize total earnings** within a given time constraint.

---

## 📌 Project Need / Purpose

This project demonstrates:

* **Algorithmic thinking & optimization**
* Ability to translate a **business problem into code**
* Use of **Python logic** for decision-making problems
* Clean project structure suitable for **technical interviews**

The scenario simulates real-world **resource planning**, where limited time must be used to achieve **maximum profit**.

---

## 🧠 Problem Statement

Mr. X owns infinite land on Mars. He can develop the land with the following properties:

| Property            | Build Time | Land Size | Earnings per Unit |
| ------------------- | ---------- | --------- | ----------------- |
| Theatre (T)         | 5 units    | 2x1       | $1500             |
| Pub (P)             | 4 units    | 1x1       | $1000             |
| Commercial Park (C) | 10 units   | 3x1       | $2000             |

### Constraints

* Only **one property can be built at a time**
* Total available time = **n units (input)**
* Goal: **maximize earnings**

### Output Format

```
T:<count> P:<count> C:<count>
```

---

## 📊 Sample Test Cases

### Test Case 1

```
Input  : 7
Output : Earnings = $3000
T:1 P:0 C:0
```

### Test Case 2

```
Input  : 8
Output : Earnings = $4500
T:1 P:0 C:0
```

### Test Case 3

```
Input  : 13
Output : Earnings = $16500
T:2 P:0 C:0
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Virtual Environment (.venv)**
* Standard Python libraries only

---

## 📂 Project File Structure

```
MAX/
│
├── app.py             # Main Python logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Ignored files
└── .venv/             # Virtual environment
```

---

## ⚙️ How the Solution Works

1. Take **n (time units)** as input
2. Evaluate all possible combinations of properties
3. Ensure total build time ≤ n
4. Calculate total earnings for each combination
5. Select the **maximum profit combination**
6. Display the result in the required format

This ensures the **optimal earning strategy**.

---

## 📸 Screenshot

### 🔹 Project Structure & Output

![Max Profit Output](./screenshot.png)

> 📌 *Shows project files and execution result*

---

## 🚀 How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/max-profit-problem.git
   ```

2. Navigate to the project folder

   ```bash
   cd MAX
   ```

3. (Optional) Activate virtual environment

   ```bash
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

4. Run the application

   ```bash
   python app.py
   ```

---

## 🎯 Learning Outcomes

* Solving optimization problems
* Writing clean Python code
* Interview-ready project documentation
* Real-world business logic implementation

---

## 👨‍💻 Author

**Vino**
Aspiring Data Scientist | Python & Algorithms Enthusiast

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Improve the logic

---

Happy Coding 😊
