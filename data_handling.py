# data_handling.py

import pandas as pd
import logging

class DataHandler:
    def __init__(self, config):
        """
        Initialize the DataHandler with configuration settings.
        
        param config: Dictionary containing configuration parameters, this can be found & changed in config.yaml"
        """
        self.file_paths = config['data_paths']
        self.data = {}
        self.logger = logging.getLogger('DataHandler')

    def load_data(self):
        """
        Load data from file paths
        """
        try:
            self.logger.info('Loading data...')
            for name, path in self.file_paths.items():
                self.data[name] = pd.read_csv(path)
                self.logger.info(f'{name} loaded successfully from {path}')
        except Exception as e:
            self.logger.error(f'Error loading data: {e}')
            raise

    def preprocess_data(self):
        """
        Preprocess the loaded data & handle missing values. REMINDER for self!!! watch out with this, since this might in the future cause issues 
        because missing values are handled incorrectly!
        """
        try:
            self.logger.info('Preprocessing data...')
            # Handle missing values
            for df_name, df in self.data.items():
                self.data[df_name] = df.dropna()
                self.logger.info(f'{df_name}: Missing values handled.')
            
            # Below add the other preprocessing steps as merging etc. This module is totally useless still because the 
            # way the files are now composed doesnt do shit :0:). 
        except Exception as e:
            self.logger.error(f'Error during preprocessing: {e}')
            raise

    def get_data(self):
        """
        Returns the preppropd data =*)
        """
        return self.data
