import string
import secrets


def generate_password(
    length,
    use_uppercase=True,
    use_lowercase=True,
    use_numbers=True,
    use_special=True
):
    """
    Generate a secure random password.
    """

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character type must be selected.")

    all_characters = "".join(character_sets)

    password_characters = []

    # Add at least one character from each selected category
    for character_set in character_sets:
        password_characters.append(secrets.choice(character_set))

    # Fill the remaining positions
    remaining_length = length - len(password_characters)

    for i in range(remaining_length):
        password_characters.append(secrets.choice(all_characters))

    # Randomly rearrange the characters
    for i in range(len(password_characters) - 1, 0, -1):
        j = secrets.randbelow(i + 1)

        password_characters[i], password_characters[j] = (
            password_characters[j],
            password_characters[i]
        )

    return "".join(password_characters)