import math


def shannon_entropy(password: str) -> float:
    """
    Calculate Shannon entropy of a password.
    Returns entropy in bits.
    """
    if not password:
        return 0.0

    freq = {}
    for char in password:
        freq[char] = freq.get(char, 0) + 1

    entropy = 0.0
    length = len(password)

    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy * length
