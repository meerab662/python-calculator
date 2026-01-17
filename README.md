Simple CLI Calculator
A lightweight, interactive Command Line Interface (CLI) calculator built with Python. This tool performs basic arithmetic operations and runs in a continuous loop for multiple calculations.

Features
Basic Arithmetic: Supports Addition, Subtraction, Multiplication, and Division.

Error Handling: Specifically detects and handles "Division by Zero" errors.

Persistent Session: Includes a "Repeat" feature that allows you to perform multiple calculations without restarting the script.

Clean CLI Interface: Simple text-based prompts for easy user interaction.

How to Run the Project
Prerequisites
Ensure you have Python 3.x installed on your system.

Steps
Download the script: Save the code as calculator.py.

Open your Terminal or PowerShell: Navigate to the folder where you saved the file.

Run the program:
      python calculator.py

Example Usage
Once the program is running, you will interact with it as follows:


New Calculation
enter first number:
10
enter second number:
5
Addition of numbers: 15
Subtraction of numbers: 5
Multiplication of numbers: 50
Division of numbers: 2.0

Do you want to continue? (y/n)
n

Code Logic Flow
The program uses a while True loop to maintain the session. Mathematical operations are separated into modular functions for better readability and maintenance.