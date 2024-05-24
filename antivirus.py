import os

from signatures import signatures

def scan_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            for signature_name, signature in signatures.items():
                if signature in file_content:
                    return signature_name
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return None

def scan_directory(directory):
    infected_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            result = scan_file(file_path)
            if result:
                infected_files.append((file_path, result))
    return infected_files

def main():
    directory_to_scan = input("Enter the directory to scan: ")

    print(f"Scanning directory: {directory_to_scan}")
    infected_files = scan_directory(directory_to_scan)

    if infected_files:
        print("Potential malware detected in the following files:")
        for file_path, signature_name in infected_files:
            print(f"{file_path}: {signature_name}")
    else:
        print("No malware detected.")

if __name__ == "__main__":
    main()
