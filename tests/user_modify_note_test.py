from handy_funcs import add_note, modify_note, get_note, clear_notes


def test_modify_note():
    clear_notes()
    note_txt_before = 'yooo'
    note_txt_after = 'yooo, its rewind time'
    note_id = '121'

    add_note(note_txt_before, note_id)
    old_note = get_note(note_id)
    assert old_note == note_txt_before

    modify_note(note_txt_after, note_id)
    new_note = get_note(note_id)
    assert new_note == note_txt_after
    