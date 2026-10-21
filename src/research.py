
def search_notes(query: str, notes: list[str]) -> list[str]:
    query_words = query.lower().split()

    results = []

    for note in notes:
        note_lower = note.lower()

        if all(word in note_lower for word in query_words):
            results.append(note)

    return results


def search_notes(query: str, notes: list[str]) -> list[str]:
    query_words = query.lower().split()

    if not query_words:
        return []

    scored_notes = []

    for note in notes:
        note_lower = note.lower()
        score = sum(word in note_lower for word in query_words)

        if score > 0:
            scored_notes.append((score, note))

    scored_notes.sort(key=lambda item: item[0], reverse=True)

    return [note for score, note in scored_notes]


def search_notes(query: str, notes: list[str]) -> list[str]:
    query_words = query.lower().split()

    if not query_words:
        return []

    scored_notes = []

    for note in notes:
        note_lower = note.lower()
        score = sum(word in note_lower for word in query_words)

        if score > 0:
            scored_notes.append((score, note))

    scored_notes.sort(key=lambda item: item[0], reverse=True)

    return [note for score, note in scored_notes]
