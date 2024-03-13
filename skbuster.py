import requests
import argparse
import sys


def print_logo():
    logo = """
    \033[91m _______  _______  _______  _______  _______ 
    |       ||       ||       ||       ||       |
    |  _____||   _   ||    ___||    _  ||  _____|
    | |_____ |  | |  ||   |___ |   |_| || |_____ 
    |_____  ||  |_|  ||    ___||    ___||_____  |
     _____| ||       ||   |___ |   |     _____| |
    |_______||_______||_______||___|    |_______|
    
    Sandeep's Online Enumeration and Pentesting Suite 
    Directory and File Enumeration Tool \033[0m
    """
    print(logo)

# Function to check URL validity
def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code, response.url
    except requests.exceptions.RequestException as e:
        return None, str(e)

def main():
    print_logo()  # Print the SKDirB logo when the tool starts
    parser = argparse.ArgumentParser(description="SKDirB - A simple directory and file enumeration tool")
    parser.add_argument("url", help="The target URL to scan")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file (default: wordlist.txt)", default="wordlist.txt")
    parser.add_argument("-e", "--extensions", help="File extensions to search for (comma-separated, e.g., php,html)", default=None)
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as f:
            wordlist = f.read().splitlines()
    except FileNotFoundError:
        print("Wordlist file not found.")
        sys.exit(1)

    extensions = args.extensions.split(",") if args.extensions else None

    print(f"[*] Starting SKDirB scan on {args.url}")

    for path in wordlist:
        url = args.url.rstrip("/") + "/" + path
        status_code, final_url = check_url(url)
        if status_code:
            print(f"[+] Found: {final_url} (Status Code: {status_code})")
        elif status_code is None:
            print(f"[!] Error occurred: {final_url}")
        else:
            print(f"[-] Not found: {final_url}")

if __name__ == "__main__":
    main()

