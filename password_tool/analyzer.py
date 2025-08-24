import math
import re
from typing import List, Dict, Any

# --- Helper functions ---
def _pool_size(password: str) -> int:
    lowers = any(c.islower() for c in password)
    uppers = any(c.isupper() for c in password)
    digits = any(c.isdigit() for c in password)
    specials = any(not c.isalnum() for c in password)
    size = 0
    if lowers: size += 26
    if uppers: size += 26
    if digits: size += 10
    if specials: size += 33
    return max(size, 1)

def _has_sequence(password: str) -> bool:
    return any(password[i:i+4].isdigit() or password[i:i+4].isalpha()
               for i in range(len(password)-3))

def _has_repetition(password: str) -> bool:
    return re.search(r'(.)\1{2,}', password) is not None

COMMON = {"password", "123456", "qwerty", "admin", "welcome"}

def _entropy_estimate(password: str) -> float:
    pool = _pool_size(password)
    entropy = len(password) * math.log2(pool)
    if _has_sequence(password): entropy -= 10
    if _has_repetition(password): entropy -= 7
    if password.lower() in COMMON: entropy -= 12
    return max(entropy, 0.0)

def _classify(entropy_bits: float) -> str:
    if entropy_bits < 28: return "Very Weak"
    elif entropy_bits < 36: return "Weak"
    elif entropy_bits < 60: return "Fair"
    elif entropy_bits < 80: return "Strong"
    else: return "Very Strong"

# --- Main function ---
def analyze_password(password: str, user_inputs: List[str] = None) -> Dict[str, Any]:
    entropy_bits = _entropy_estimate(password)
    classification = _classify(entropy_bits)
    issues = []
    if len(password) < 8: issues.append("Too short")
    if password.lower() in COMMON: issues.append("Common password")
    if _has_sequence(password): issues.append("Contains sequence")
    if _has_repetition(password): issues.append("Contains repetition")

    return {
        "password": password,
        "length": len(password),
        "entropy_bits": round(entropy_bits, 2),
        "classification": classification,
        "issues": issues,
    }
