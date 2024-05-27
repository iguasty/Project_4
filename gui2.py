import tkinter as tk

class Gui2:
    def __init__(self):
        self.root = tk.Tk(className="GUI2")
        self.root.minsize(800, 400)
        
        self.last_smallest = None #used for storing the last smallest number

        
        self.title_label = tk.Label(self.root, text="BASIC GUI 2!")
        self.prompt_label = tk.Label(self.root, text="Type text and press enter to change this!")
        self.entry_box = tk.Entry(self.root)
        
        self.entry_boxes = []
        
        #creates 10 text boxes and appends them to list
        for i in range(10):
            self.entry_box = tk.Entry(self.root)
            self.entry_box.pack()
            self.entry_boxes.append(self.entry_box)
        
        
        self.enter_button = tk.Button(self.root, text="Enter", command=self.find_smallest_num)
        self.title_label.pack()
        self.prompt_label.pack()
        
        self.enter_button.pack()
        self.root.mainloop()
    
    def find_smallest_num(self):
        """finds next smallest number in entry boxes"""
        smallest_num = None        
        for self.entry_box in self.entry_boxes:
            try:
                text = self.entry_box.get().strip()
                number = float(text)
                
                if (self.last_smallest is None or number > self.last_smallest) and (smallest_num is None or number < smallest_num):
                    smallest_num = number
                  #  smallest_entry = self.entry_box
            except ValueError:
                continue
            
        if smallest_num is not None:
            self.last_smallest = smallest_num
            self.update_label(smallest_num)
        else:
            self.update_label("No valid number found that is greater than the previous smallest number.")
                 
    def update_label(self,newtext):
        """update label text"""
        self.prompt_label.config(text=newtext)
    
