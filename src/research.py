
def search_notes(query: str, notes: list[str]) -> list[str]:
    query_words = query.lower().split()

    results = []

    for note in notes:
        note_lower = note.lower()

        if all(word in note_lower for word in query_words):
            results.append(note)

    return results
