from handy_funcs import add_note, get_note, clear_notes


def test_add_note():
    clear_notes()
    noteId = 1
    note_text = "yoo"
    add_note(note_text, noteId)
    assert get_note(noteId) == note_text