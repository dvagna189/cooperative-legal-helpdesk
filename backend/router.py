def classify_query(question):

    question = question.lower()

    governance_words = [
        "election",
        "voting",
        "committee",
        "meeting",
        "member",
        "registration",
        "bylaw"
    ]

    legal_words = [
        "complaint",
        "grievance",
        "rights",
        "legal",
        "fraud",
        "dispute",
        "law"
    ]

    for word in governance_words:
        if word in question:
            return "governance"

    for word in legal_words:
        if word in question:
            return "legal"

    return "general"
