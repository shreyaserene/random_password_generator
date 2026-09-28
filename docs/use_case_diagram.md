# Use Case Diagram

## SecurePass – Random Password Generator

### Actor

**User**

### Use Cases

The user can:

1. Generate a random password
2. Analyze password strength
3. View password history
4. Exit the program

### Use Case Flow

                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       Generate Password  Analyze Strength  View History
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                         Exit Program
                         | Use Case          | Description                                                             |
| ----------------- | ----------------------------------------------------------------------- |
| Generate Password | Generates a random password based on the specified length.              |
| Analyze Strength  | Checks password length and character types and determines its strength. |
| View History      | Displays passwords generated during the current session.                |
| Exit Program      | Terminates the SecurePass program.                                      |