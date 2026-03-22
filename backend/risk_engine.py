def calculate_risk(query):
    q = query.lower()
    score = 0

    if "no pulse" in q:
        score += 100
    if "unconscious" in q:
        score += 70
    if "chest pain" in q:
        score += 50
    if "bleeding" in q:
        score += 60
    if "shortness of breath" in q:
        score += 40
    if "diabetes" in q:
        score += 20

    return score


def get_priority(score):
    if score >= 100:
        return "🔴 CRITICAL"
    elif score >= 60:
        return "🟠 HIGH"
    elif score >= 30:
        return "🟡 MEDIUM"
    else:
        return "🟢 LOW"