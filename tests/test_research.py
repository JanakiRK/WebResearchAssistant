from src.research import search_notes


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

