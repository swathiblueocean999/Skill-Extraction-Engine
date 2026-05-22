import logging
import os

def setup_logger():
    # 1. Create a folder named 'logs' if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # 2. Basic Configuration
    logging.basicConfig(
        filename='logs/ai_system.log', # Where to save the log
        level=logging.INFO,             # Type of messages to track
        format='%(asctime)s - %(message)s', # Time and message format
        filemode='w'                    # 'w' means overwrite each time you run
    )

    # 3. Create a logger object
    logger = logging.getLogger()
    
    # 4. Also show the logs in the VS Code Terminal
    console = logging.StreamHandler()
    logger.addHandler(console)

    return logger

if __name__ == "__main__":
    my_logger = setup_logger()
    my_logger.info("Environment setup is successful!")