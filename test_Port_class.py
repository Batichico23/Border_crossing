import pandas as pd

import numpy as np

class top_port():

    def __init__(self, port_name, wait_time, position):
        """ description : Begins to asses the port of entry name, the wait time to cross the border, and the position
        
        Parameters
        _____________
        
        dataset : DataFrame
        
        variable : name of row and column in data to summarize (string)
            represents specified variable in the input DataFrame
        
        Retuns
        
        port_name : name of port of entry in the specified variable in input DataFrame
        
        wait_time  : number of total responses
        position : position of total wait_time (usually 6)
        """
        self.port_name = port_name
        self.wait_time = wait_time
        self.position = position
        
    def get_port_name(self):
        """ description : Takes the entire dataframe and get ports of entry names
        
        Parameters
        _____________
        
        data : DataFrame
        
        variable : 
        
            port_name : string, default:6
               port_name refers to the port name of items dataset it will show
        
        Retuns
        ______
            self.port_name :list of DataFrame(s)
                              will return a list of dataframes.
                    Each dataframes in the list will be a subsets of a csv file that is specify by user input.
        
        """
        return self.port_name
    
    def get_wait_time(self):
        """ 
        
        Parameters
        _____________
        
        dataset : DataFrame
        
        variable : column and rows : int
        
        Retuns
        ______
        self.wait_time[0]: CSV File
            returns wait time values by the CSV File
        """
        return self.wait_time
    
    def get_position(self):
        """ 
        
        Parameters
        _____________
        
        dataset : DataFrame
        
        variable : column : int
        
        Retuns
        ______
        self.position: CSV File
            returns sorted values by the CSV File
        """
        return self.position
    
    def print_class(self):
        """ 
        
        Parameters
        _____________
        
        dataset : DataFrame
        
        variable : column and rows : string
        
        Retuns
        ______
        self.position: CSV File
            prints sorted values by the CSV File
            
        self.port_name: CSV File
            prints port of entry names by the CSV File
            
        wait_time: CSV File
            prints waiting time by the CSV File
            
        """
        print(self.position, self.port_name, 'Wait time:', self.wait_time)