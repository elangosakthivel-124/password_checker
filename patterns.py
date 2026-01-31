import re
from constants import KEYBOARD_PATTERNS


def has_sequential_chars(password: str, seq_len: int = 4) -> bool:
    for i in range(len(password) - seq_len + 1):
        chunk = password[i:i + seq_len]

        if all(ord(chunk[j]) + 1 == ord(chunk[j + 1]) for j in range(len(chunk) - 1)):
            return True

        if all(ord(chunk[j]) - 1 == ord(chunk[j + 1]) for j in range(len(chunk) - 1)):
            return True

    return False


def has_repeated_chars(password: str, repeat_len: int = 3) -> bool:
    pattern = r"(.)\1{" + str(repeat_len - 1) + r",}"
    return bool(re.search(pattern, password))


def contains_keyboard_pattern(password: str) -> bool:
    pwd = password.lower()
    return any(pattern in pwd for pattern in KEYBOARD_PATTERNS)
