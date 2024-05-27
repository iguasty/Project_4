import tkinter as tk

class Gui1: 
    
    def __init__(self):
        self.root = tk.Tk(className="GUI1")
        self.root.minsize(800, 400)

        self.title_label = tk.Label(self.root, text="BASIC GUI 1!")
        self.prompt_label = tk.Label(self.root, text="Type text and press enter to change this!")
        self.entry_box = tk.Entry(self.root)
        self.exit_label = tk.Label(self.root, text="Close this window to open GUI2!")
        self.enter_button = tk.Button(self.root, text="Enter", command=self.update_label)
        self.title_label.pack()
        self.prompt_label.pack()
        self.entry_box.pack()
        self.enter_button.pack()
        self.exit_label.pack()
        self.root.mainloop()
        
    def update_label(self):
        """update label text"""
        newtext = self.entry_box.get()
        self.prompt_label.config(text=newtext)
        return newtext
    
    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
        gui = Gui1()
        gui.run()