



import pandas as pd
import json
import os
import logging

class SequenceGenerator:
    def __init__(self):
        self.logger = logging.getLogger('SequenceGenerator')
        self.vertebrae = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']


    def generate_sequences(self, df):
         ###RF*S How do we handle slides with multiple vertebrae in it?!
        """ Generates sequences of slides per vertebrae 
        df input: dataframe with detected vertebrae
        returns dictionary containing sequences for each vertebrae"""

        try:
            self.logger.info('generating sequences...')
            sequences = {v: {} for v in self.vertebrae}
            for v in vertebrae:
                vertebrae_df = df[df['VertebraeDetected'].apply(lambda x: v in x)]
                grouped = vertebrae_df.groupby("StudyInstanceUID")
                for study_uid, group in grouped:
                    sequences = group.sort_values("slice")["slice"].tolist()
                    sequences[v][study_uid]

                self.logger.info("sequences generated sucessfuly")
                return sequences
            
        except Exception as e:
            self.logger.error(f"error during sequence generation: {e}")
        
    
