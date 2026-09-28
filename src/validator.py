def check_length(length):

    if length < 8:
        return False

    return True


def check_character_selection(
    uppercase,
    lowercase,
    numbers,
    special
):

    if (
        uppercase == False
        and lowercase == False
        and numbers == False
        and special == False
    ):
        return False

    return True