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

    

    Design: 

        I decided to use only one driver file to demonstrate both programs. I made a menu for in the driver file to select which program you would like to run. I did this so I wouldn't have to make a whole new repository and it made reusing code a little bit easier. 