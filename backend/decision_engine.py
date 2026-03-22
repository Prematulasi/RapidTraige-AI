def generate_action(query):
    q = query.lower()

    if "no pulse" in q:
        return "Start CPR immediately"
    elif "chest pain" in q:
        return "Administer aspirin and perform ECG"
    elif "bleeding" in q:
        return "Apply pressure to stop bleeding"
    elif "unconscious" in q:
        return "Check airway and provide oxygen"
    else:
        return "Monitor vitals and assess patient"