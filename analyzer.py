from typing import Dict, List
from constants import COMMON_PASSWORDS
from entropy import shannon_entropy
from patterns import (
    has_sequential_chars,
    has_repeated_chars,
    contains_keyboard_pattern
)


def character_sets(password: str) -> Dict[str, bool]:
    return {
        "lower": any(c.islower() for c in password),
        "upper": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "symbol": any(not c.isalnum() for c in password),
    }


def password_strength(password: str) -> Dict[str, object]:
    score = 0
    feedback: List[str] = []

    length = len(password)
    sets = character_sets(password)
    entropy = shannon_entropy(password)

    # Length
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    else:
        feedback.append("Password must be at least 8 characters long")

    # Character variety
    variety = sum(sets.values())
    score += variety * 10

    if variety < 3:
        feedback.append("Use uppercase, lowercase, digits, and symbols")

    # Entropy
    if entropy >= 60:
        score += 25
    elif entropy >= 40:
        score += 15
    else:
        feedback.append("Password is predictable")

    # Penalties
    pwd_lower = password.lower()

    if pwd_lower in COMMON_PASSWORDS:
        score -= 40
        feedback.append("Common password detected")

    if has_sequential_chars(password):
        score -= 15
        feedback.append("Sequential characters detected")

    if has_repeated_chars(password):
        score -= 10
        feedback.append("Repeated characters detected")

    if contains_keyboard_pattern(password):
        score -= 15
        feedback.append("Keyboard pattern detected")

    score = max(0, min(100, score))

    if score >= 80:
        verdict = "Very Strong"
    elif score >= 60:
        verdict = "Strong"
    elif score >= 40:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return {
        "score": score,
        "verdict": verdict,
        "entropy": round(entropy, 2),
        "length": length,
        "character_sets": sets,
        "feedback": feedback or ["Good password"]
    }
