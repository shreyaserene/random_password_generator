# Design Decisions and Rationale

## SecurePass – Random Password Generator

The following design decisions were made while developing the
SecurePass project.

### 1. Python as the Programming Language

Python was selected because it is simple, readable and suitable
for developing beginner-level applications.

### 2. Modular Programming

The project is divided into different modules such as password
generation, password analysis, password history and validation.

This makes the project easier to understand, maintain and expand.

### 3. Secure Random Generation

The Python `secrets` module is used for password generation because
it is designed for generating random values suitable for security
related applications.

### 4. Basic Input Validation

Input validation is included to prevent invalid password lengths
and incorrect selections.

### 5. Password Strength Analysis

A basic scoring system is used to analyze passwords based on
length and the presence of uppercase letters, lowercase letters,
numbers and special characters.

### 6. Session-Based Password History

Generated passwords are stored in a list during the current
program session. This provides a simple way to view previously
generated passwords.

### 7. Command-Line Interface

A command-line interface is used because it is simple to implement
and matches the Python concepts learned in the course.

### 8. Standard Library

The project uses Python's standard library wherever possible.
Therefore, no external packages are required.

### 9. Future GUI Enhancement

A graphical user interface can be added in the future. It is not
included in the current version because the current project focuses
on core Python programming concepts.