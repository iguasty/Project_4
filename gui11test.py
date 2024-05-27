# test_gui1.py
import pytest
import tkinter as tk
from gui1 import Gui1

@pytest.fixture 
def gui():
    gui_instance = Gui1()
    return gui_instance

def test_entry_value(gui):
    # Access the entry widget
    entry_widget = gui.entry_box
    
    # Simulate entering text in the entry widget
    entry_widget.insert(0,"test input")
    
    # Assert the entry value is as expected
    assert gui.update_label() == "test input"

if __name__ == "__main__":
    pytest.main()

