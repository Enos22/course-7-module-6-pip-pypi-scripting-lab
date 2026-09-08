from datetime import datetime

def generate_log(data):
    # 1. Validate input type - must be ValueError
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # 2. Filename pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # 3. Write - creates file even if list is empty
    # 4. Content exactly matches input list
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # 5. Print confirmation including filename
    print(f"Log written to {filename}")
    
    return filename