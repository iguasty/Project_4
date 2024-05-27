# test_gui1.py
import pytest
import tkinter as tk
from gui1 import Gui1

@pytest.fixture 
def gui():
    gui_instance = Gui1()
    return gui_instance

def test_entry_value(gui):
    gui = Gui1()
    # Simulate entering text in the entry widget
    gui.entry_box.insert(0, str("test input"))
    
    # Assert the entry value is as expected
    assert gui.update_label() == "test input"

if __name__ == "__main__":
    pytest.main()

