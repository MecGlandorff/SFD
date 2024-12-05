



# NS*F = note for self
# N*W = not working
# RS*F = reminder for self


# Main
import logging
import yaml
import argparse
from seq_output import SequenceGenerator

def setup_logging(log_level=logging.INFO):
    # NF*S https://docs.python.org/3/library/logging.html
    """
    Logging function. You can determine here how much logging info you want
    """  
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[
            logging.FileHandler('slice_detector.log', mode='w'),
            logging.StreamHandler()
                    ])
    
def load_config(config_path):
    """ Load the configuration settings from a YAML file"""
   
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def main():

    parser = argparse.ArgumentParser(description='SliceDetector Program')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to the configuration file')
    args = parser.parse_args()

    # Setting up loggger
    setup_logging()
    logger = loggin.getLogger("main")

    try:
        pass

    except Exception as e:
        pass