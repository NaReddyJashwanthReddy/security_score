import pandas as pd
from logger import logging

class ExtractData:
    def __init__(self):
        pass

    def csv_file(self,file):
        logging.info("loading csv file started")
        data=pd.read_csv(file)
        logging.info("loading csv file ended")
        return data 
    
    def excel_file(self,file):
        logging.info("loading excel file started")
        data=pd.read_excel(file)
        logging.info("loading excel file ended")
        return data 
    
    def ReadData(self,file,filetype):
        logging.info("Data process started")
        if filetype.lower()=='csv':
            data=self.csv_file(file)
        elif filetype.lower()=='excel':
            data=self.excel_file(file)
        else:
            logging.info("unknown file type")
            exit() 
        logging.info("required data extracted")
        return data 
    


