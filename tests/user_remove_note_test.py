from handy_funcs import delete_note, get_note, add_note, clear_notes


def test_user_can_delete_note(): 
    clear_notes()

    #first add 2 notes
    note_1_text = "note 1"
    note_2_text = "note 2"
    add_note(note_1_text,1)
    add_note(note_2_text,2)

    #delete note 2 
    delete_note(2)
    assert get_note(1) == note_1_text
    assert get_note(2) == None