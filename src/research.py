
import re


def search_notes(query: str, notes: list[str]) -> list[str]:
    query_words = re.findall(r"\b\w+\b", query.lower())

    if not query_words:
        return []

    scored_notes = []

    for note in notes:
        note_words = set(re.findall(r"\b\w+\b", note.lower()))
        score = sum(word in note_words for word in query_words)

        if score > 0:
            scored_notes.append((score, note))

    scored_notes.sort(key=lambda item: item[0], reverse=True)

    return [note for score, note in scored_notes]
