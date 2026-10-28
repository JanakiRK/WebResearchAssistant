from src.research import search_notes
import re


def test_search_notes_finds_relevant_note():
    notes = [
        "RAG retrieves relevant documents for AI answers",
        "Python is a programming language",
        "Agents can use tools to complete tasks",
    ]

    results = search_notes("RAG documents", notes)

    assert results == ["RAG retrieves relevant documents for AI answers"]


def test_search_notes_returns_empty_list_when_no_match():
    notes = [
        "RAG retrieves relevant documents",
        "Python is a programming language",
    ]

    results = search_notes("database", notes)

    assert results == []


def test_search_notes_ignores_case():
    notes = ["RAG helps retrieve documents"]

    results = search_notes("rag", notes)

    assert results == ["RAG helps retrieve documents"]


def test_search_notes_ranks_best_match_first():
    notes = [
        "Python is a programming language",
        "RAG retrieves relevant documents",
        "RAG documents help AI systems",
    ]

    results = search_notes("RAG documents AI", notes)

    assert results == [
        "RAG documents help AI systems",
        "RAG retrieves relevant documents",
    ]

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

def test_search_notes_does_not_match_partial_words():
    notes = [
        "Training improves software skills",
        "AI helps with research",
    ]

    results = search_notes("AI", notes)

    assert results == ["AI helps with research"]