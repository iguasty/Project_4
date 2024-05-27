# Project_4
 Project 4 for CS162

Here is my Project 4 README file. Here I will discuss the Project 4 questions and the design process of my program. 

Questions: 
    1. Describe a set of data that could be important to someone,(Maybe the set of quarter mile times for a group of racers in a group of cars or lines of code from programmers)

        When I did an internship at Roseburg Forest Products as a Controls and Automation intern, I worked mainly with creating HMI's (human machine interfaces) for the operators in the mill. Some of these HMI's would take sets of data from sensor inputs and display them to the operators graphically. An example of this was the output energy levels from the steam powered generators, or the number of pallets per hour being processed. These data sets are super helpful because they show how well the processes are doing or if there is an issue that needs to be addressed.
    
    2. Describe a sequence of steps to find a useful piece of information in that data set, (Maybe find the best times for individual racers (were they all using the same car))

        To find a useful piece of information in one of the datasets, we could look throught the time stamps of each data point and compare them to a known value. For example if there was a dip in energy levels being output from the steam powered generators then we could find the data points were energy levels were low and see the time they were taken at and then see if there are any corresponding weird values from other sensor inputs at the same time to try and pinpoint the cause of the energy dip. This could all be automated by setting known values for the data to be compared to. If a data point is below that known value then it could send an alert to the automated program, the program could then grab all other sensor values and compare those to a known value and decide what the causation was. 

    3. Discuss ways that grouping or ordering your data might help you find certain items or categories of data, (Maybe find the best times for each car grouped by make or model) 

        As previously discussed, the most useful ways to categorize this data would be by time stamp, low values, and high values. Ordering the data set over long periods of time (like months or years) and seeing the value averages over this time period could be useful to determine if efficiency is slowly degrading and can help with preventative maintenance (example would be to replace certain parts if average efficiency is starting to decline). Another way to categorize the data is by the sensors, for instance, there are usually atleast two sensors taking input for the same measurement. This is for redundancy and to help with accuracy. Categorizing the data per sensor can provide insight on the deviation between input values which would be used for determining whether one of the sensors needs recalibrated or replaced. 

    4. Is there any way to automate some tests on these graphical objects? 
        
        Yes, we can use libraries like PyTest or PyTest for Tkinter to automate some of the tests on graphical interfaces.

    Design: 

        I decided to use only one driver file to demonstrate both programs. I made a menu for in the driver file to select which program you would like to run. I did this so I wouldn't have to make a whole new repository and it made reusing code a little bit easier. 


    PyTest: I attempted to implement PyTest into my code as stated by the requirements for this assignment, however I kept running into the error: 

    ============================================================ FAILURES ============================================================= 
________________________________________________________ test_entry_value _________________________________________________________

gui = <gui1.Gui1 object at 0x0000020FC2B4E5A0>

    def test_entry_value(gui):
        gui = Gui1()
        # Simulate entering text in the entry widget
>       gui.entry_box.insert(0, str("test input"))

gui11test.py:14:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tkinter.Entry object .!entry>, index = 0, string = 'test input'

    def insert(self, index, string):
        """Insert STRING at INDEX."""
>       self.tk.call(self._w, 'insert', index, string)
E       _tkinter.TclError: invalid command name ".!entry"

C:\Users\isaac\AppData\Local\Programs\Python\Python312\Lib\tkinter\__init__.py:3140: TclError
===================================================== short test summary info ===================================================== 
FAILED gui11test.py::test_entry_value - _tkinter.TclError: invalid command name ".!entry"


I got the same error for my gui2test.py program except it said:

FAILED gui2test.py::test_entry_value - _tkinter.TclError: invalid command name ".!entry11" 

the ".!entry11" looks like its correlated to the amount of entry_box 's that are created. I changed the number created in gui2.py to 9 instead of 10 and it changed the error to ".!entry10". My guess is that it is trying to insert a value at an index that does not exist. I messed around with it for a while, but I was unable to figure out how to fully fix the error.

