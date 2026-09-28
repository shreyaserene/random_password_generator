# Module Design

## SecurePass – Random Password Generator

SecurePass is divided into separate modules. Each module performs
a specific task, making the project easier to understand, maintain
and modify.

## Modules

### 1. main.py

**Purpose:**  
Controls the overall execution of the SecurePass program.

**Main Responsibilities:**
- Displays the SecurePass interface.
- Takes input from the user.
- Calls the required modules.
- Displays the generated password and results.

---

### 2. password_generator.py

**Purpose:**  
Generates secure random passwords.

**Main Responsibilities:**
- Accepts the required password length.
- Uses uppercase letters, lowercase letters, numbers and
  special characters.
- Ensures selected character types are included.
- Randomly rearranges the generated characters.
- Returns the generated password.

---

### 3. strength_analyzer.py

**Purpose:**  
Analyzes the strength of a password.

**Main Responsibilities:**
- Counts uppercase letters.
- Counts lowercase letters.
- Counts numbers.
- Counts special characters.
- Checks password length.
- Calculates a basic strength score.
- Displays the password strength.

---

### 4. password_history.py

**Purpose:**  
Maintains the history of generated passwords during the
current program session.

**Main Responsibilities:**
- Adds generated passwords to the history.
- Displays stored passwords.
- Clears the password history.

---

### 5. validator.py

**Purpose:**  
Validates user input.

**Main Responsibilities:**
- Checks whether the password length is valid.
- Checks whether at least one character type is selected.
- Helps prevent invalid input.

---

## Module Interaction

```text
                 ┌─────────────┐
                 │   main.py   │
                 └──────┬──────┘
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
 ┌────────────────┐ ┌──────────────┐ ┌─────────────────┐
 │ password_      │ │ strength_    │ │ password_       │
 │ generator.py   │ │ analyzer.py  │ │ history.py      │
 └────────────────┘ └──────────────┘ └─────────────────┘
          │
          ▼
 ┌────────────────┐
 │ validator.py   │
 └────────────────┘

 ## Advantages of Modular Design

1. **Easy to Understand**  
   Each module performs a specific task, making the code easier to understand.

2. **Easy to Maintain**  
   Changes can be made to one module without affecting the entire program.

3. **Easy to Debug**  
   Errors can be located more easily because the program is divided into smaller modules.

4. **Code Reusability**  
   Functions from a module can be reused whenever required.

5. **Better Organization**  
   Dividing the program into separate modules keeps the project organized.

6. **Easy to Expand**  
   New features can be added by creating or modifying individual modules.

7. **Improved Readability**  
   Smaller and well-organized files make the overall project easier to read.