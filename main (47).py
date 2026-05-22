from logger_setup import setup_logger

def main():
    # Set up the logger
    logger = setup_logger()
    
    logger.info("AI Project Main Module starts...")
    
    # main logic of the AI project would go here
    print("Hello! AI Project is running.")
    
    logger.info("Task completed successfully.")

if __name__ == "__main__":
    main()