def analyze_password(password):

    length = len(password)

    uppercase = 0
    lowercase = 0
    numbers = 0
    special = 0

    for ch in password:

        if ch >= 'A' and ch <= 'Z':
            uppercase = uppercase + 1

        elif ch >= 'a' and ch <= 'z':
            lowercase = lowercase + 1

        elif ch >= '0' and ch <= '9':
            numbers = numbers + 1

        else:
            special = special + 1

    score = 0

    if length >= 8:
        score = score + 1

    if uppercase > 0:
        score = score + 1

    if lowercase > 0:
        score = score + 1

    if numbers > 0:
        score = score + 1

    if special > 0:
        score = score + 1

    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"

    print("\nPassword Analysis")
    print("------------------")
    print("Length:", length)
    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)
    print("Numbers:", numbers)
    print("Special characters:", special)
    print("Score:", score)
    print("Strength:", strength)