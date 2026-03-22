def advanced_pruning(records, query):
    keywords = query.lower().split()
    filtered = []

    for record in records:
        # Remove irrelevant history
        if "dental" in record.lower():
            continue

        # Score relevance
        score = 0
        for word in keywords:
            if word in record.lower():
                score += 1

        if score > 0:
            filtered.append((record, score))

    # Sort by relevance
    filtered.sort(key=lambda x: x[1], reverse=True)

    # Return top 3
    return [r[0] for r in filtered[:3]]