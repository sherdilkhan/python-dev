# Imports
import sys
import math
import time

# Global Constants (if needed)
API_KEY = "your_api_key"

# Function Definitions
def main():
    while True:  # This creates a forever loop
        try:
            # Main logic of your script
            result = perform_task()
            print("Task completed successfully:", result)
        except Exception as e:
            # Print a custom error message that includes the exception details
            print("Process terminated due to an exception: {}".format(e))
            # Optionally, you can log the error for debugging
            # logging.exception("An error occurred")


        time.sleep(60)  # Sleep for 60 seconds (adjust as needed)

def perform_task():
    # Your task-specific logic here
    print ("task New")
    # ...
    # If an error occurs, raise an exception

# Entry point for the script
if __name__ == "__main__":
    main()
