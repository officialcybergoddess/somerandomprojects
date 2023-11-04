import os
import re

# Define a list of patterns to identify potential malware or suspicious content.
suspicious_patterns = [
    r"virus",
    r"malware",
    r"hack",
]

def scan_file(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            content = file.read()
            for pattern in suspicious_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    return True
    except Exception as e:
        print(f"Error scanning {file_path}: {e}")
    return False

def main():
    directory_to_scan = "C:/Users/Cyber Goddess/Desktop/projects/"  # Replace with the directory you want to scan

    for root, _, files in os.walk(directory_to_scan):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path):
                print(f"Suspicious file detected: {file_path}")

if __name__ == "__main__":
    main()
