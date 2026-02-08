import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone number to standard format.

    Algorythm:
    1. Removes all characters exept digits and '+'.
    4. If number starts with '+380' returns it.
    2. If number starts with '380' adds '+' in the beginning and returns is.
    3. If number starts with '0' adds '+38' in the beginning and returns is.

    :param phone_number: string with phone number unformatted
    :return: Normalized phone number in format: +380XXXXXXXXX
    """

    # Removing all characters exept digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    # If number starts with international code
    if cleaned.startswith("+380"):
        return cleaned

    # If number starts with international '380' adding '+'
    if cleaned.startswith("380"):
        return f"+{cleaned}"

    # If number starts with international '0' adding '+38'
    if cleaned.startswith("0"):
        return f"+38{cleaned}"