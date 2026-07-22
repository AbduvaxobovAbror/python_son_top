# 🎯 Number Guessing Game

A simple Python terminal game where the user and the computer compete to guess numbers with the fewest attempts.

## 📖 About the Project

This project consists of two game modes:

### 1. User Guesses the Number
- The computer randomly selects a number between **1** and **x**.
- The player tries to guess the number.
- After each incorrect guess, the program gives a hint whether the correct number is **higher** or **lower**.

### 2. Computer Guesses the Number
- The user thinks of a number between **1** and **x**.
- The computer keeps making guesses.
- The user responds with:
  - `+` if the secret number is higher.
  - `-` if the secret number is lower.
  - `t` if the computer guessed correctly.

At the end of the game, the program compares the number of attempts and announces the winner.

---

## ✨ Features

- Random number generation
- Interactive command-line interface
- User vs Computer gameplay
- Tracks the number of guesses
- Option to play multiple rounds

---

## 🛠 Requirements

- Python 3.x

No external libraries are required.

---

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/AbduvaxobovAbror/your-repository-name.git
```

Navigate to the project directory:

```bash
cd your-repository-name
```

Run the program:

```bash
python main.py
```

---

## 💻 Example

```
I have chosen a number between 1 and 10. Can you guess it?

>>> 5
Wrong! My number is higher.

>>> 8
Wrong! My number is lower.

>>> 7
Congratulations! You guessed the number in 3 attempts.
```

---

## 📁 Project Structure

```
Number-Guessing-Game/
│
├── main.py
└── README.md
```

---

## 📚 Technologies Used

- Python 3
- Random module

---

## 👨‍💻 Author

**Abror Abduvahobov**

GitHub: https://github.com/AbduvaxobovAbror

---

## 📄 License

This project is open source and available under the MIT License.
