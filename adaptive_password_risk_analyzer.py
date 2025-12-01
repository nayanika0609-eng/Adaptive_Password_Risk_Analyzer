import math
import string
import re

# -----------------------
# Password Risk Analyzer
# -----------------------

COMMON_WORDS = [
    "password", "admin", "user", "login", "welcome", "qwerty",
    "abc", "pass", "letmein", "love", "god", "hello", "iloveyou"
]


def calculate_entropy(password):
    """Calculate entropy based on character variety."""
    char_sets = 0

    if any(c.islower() for c in password):
        char_sets += 26
    if any(c.isupper() for c in password):
        char_sets += 26
    if any(c.isdigit() for c in password):
        char_sets += 10
    if any(c in string.punctuation for c in password):
        char_sets += len(string.punctuation)

    if char_sets == 0:
        return 0

    entropy = len(password) * math.log2(char_sets)
    return round(entropy, 2)


def contains_common_words(password):
    """Check for dictionary/common weak words."""
    findings = []
    lower = password.lower()

    for word in COMMON_WORDS:
        if word in lower:
            findings.append(word)

    return findings


def has_repeated_patterns(password):
    """Detect repeated characters or sequences like aaa, 111, !!!."""
    repeats = re.findall(r"(.)\1{2,}", password)
    return repeats


def detect_sequences(password):
    """Detect keyboard or numeric sequences like 1234, abcd."""
    sequences = []

    # Numeric patterns
    if re.search(r"123|234|345|456|567|678|789|012", password):
        sequences.append("numeric sequence")

    # Alphabetic sequences
    if re.search(r"abc|bcd|cde|def|xyz", password.lower()):
        sequences.append("alphabet sequence")

    # Keyboard pattern
    keyboard_patterns = ["qwerty", "asdf", "zxcv"]
    for pat in keyboard_patterns:
        if pat in password.lower():
            sequences.append("keyboard pattern: " + pat)

    return sequences


def get_risk_level(score):
    if score >= 80:
        return "LOW"
    elif score >= 50:
        return "MEDIUM"
    else:
        return "HIGH"


def analyze_password(password):
    reasons = []
    score = 100  # Start full score, subtract weaknesses

    # Length checks
    if len(password) < 8:
        score -= 25
        reasons.append("Very short password")
    elif len(password) < 12:
        score -= 10
        reasons.append("Moderate length, could be longer")

    # Entropy
    entropy = calculate_entropy(password)
    if entropy < 28:
        score -= 25
        reasons.append("Low entropy (weak character variety)")
    elif entropy < 40:
        score -= 10
        reasons.append("Medium entropy")

    # Repeated patterns
    repeats = has_repeated_patterns(password)
    if repea
