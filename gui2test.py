import pytest
import tkinter as tk
from gui2 import Gui2

@pytest.fixture 
def gui():
    gui_instance = Gui2()
    return gui_instance

def test_entry_value():
    gui = Gui2()
    # Simulate entering number in the entry boxes
    for i in gui.entry_boxes:
        gui.entry_box.insert(0, i)
        print(i)
    # Assert the entry number is as expected into the boxes
    for i in gui.entry_boxes:
        assert gui.update_label() == i

if __name__ == "__main__":
    pytest.main()

