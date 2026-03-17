# Mini CBT (Computer-Based Test) Engine

## Project Description

This project is a Mini CBT (Computer-Based Test) Engine built using **Flask**, a lightweight Python web framework. The application allows users to take a multiple-choice test through a web browser. It demonstrates key programming concepts such as Object-Oriented Programming (OOP), data structures, and web development with Flask.

The app presents a series of questions, tracks the user's score, and displays a timestamped result page upon completion. It is designed as a portfolio piece to showcase practical skills in Python, Flask, and version control.

---

## Features

- Interactive multiple-choice test with a series of questions.
- Score tracking and result display.
- Timestamping of test completion using Python's `datetime` module.
- Simple, clean user interface styled with CSS.
- Ability to retake the test.
- Uses OOP principles to model questions and test logic.
- Implements question management with queue-like logic.

---

## Project Structure

mini_cbt/ │ ├── app.py # Main Flask application with routes and logic ├── models.py # Contains Question and CBT classes ├── static/ │ └── style.css # CSS styles for the web pages └── templates/ ├── index.html # Template for displaying questions └── result.html # Template for displaying results


---

## How to Run the Application Locally

### Prerequisites

- Python 3.x installed on your system.
- Internet connection to install Flask if not already installed.

### Steps

1. Clone or download the project files to your local machine.

2. Open a terminal or command prompt and navigate to the project directory:

(Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install Flask:
pip install flask
Run the Flask application:
python app.py
Open your web browser and go to:
http://127.0.0.1:5000/
This will start the test.
