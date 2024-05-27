# gui1.py
import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test GUI")

        self.label = tk.Label(self.root, text="Enter something:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

    def get_entry_value(self):
        return self.entry.get()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()

