def check_password(password):

    score = 0

    if len(password) >= 8:
        score += 25
    if any(c.isupper() for c in password):
        score += 25
    if any(c.isdigit() for c in password):
        score += 25
    if any(not c.isalnum() for c in password):
        score += 25

    entropy = len(password) * 4

    if score < 50:
        return "Weak", entropy, score, "Seconds", "red"
    elif score < 75:
        return "Medium", entropy, score, "Hours", "orange"
    else:
        return "Strong", entropy, score, "Years", "lime"
