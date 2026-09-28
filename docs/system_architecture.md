# System Architecture

## SecurePass – Random Password Generator

SecurePass follows a modular architecture in which different
functions of the system are divided into separate Python modules.

## Architecture Components

### 1. User
The user provides input such as password length and selects the
required operation.

### 2. main.py
The main module controls the overall execution of the program
and connects the different modules.

### 3. password_generator.py
This module generates random passwords using selected character
types and secure random generation.

### 4. strength_analyzer.py
This module analyzes the generated password based on its length,
uppercase letters, lowercase letters, numbers and special characters.

### 5. password_history.py
This module stores generated passwords during the current program
session and allows the user to view the history.

### 6. validator.py
This module checks whether user inputs satisfy basic requirements.

## Data Flow

User Input
↓
main.py
↓
Password Generator
↓
Generated Password
↓
Strength Analyzer
↓
Password History

## Architecture Diagram

User
↓
main.py
↓
├── password_generator.py
├── strength_analyzer.py
├── password_history.py
└── validator.py