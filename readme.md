# SKDirB

SKDirB is a simple directory and file enumeration tool written in Python. It is designed to help cybersecurity professionals and penetration testers in the process of reconnaissance and information gathering during security assessments.

## Features

- Fast and lightweight directory and file enumeration.
- Support for custom wordlists.
- Optional file extension filtering.
- Simple and easy-to-use command-line interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<username>/SKDirB.git
    ```

2. Navigate to the SKDirB directory:

    ```bash
    cd SKDirB
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
python skdirb.py <url> [-w WORDLIST] [-e EXTENSIONS]

- `<url>`: The target URL to scan.
- `-w WORDLIST, --wordlist WORDLIST`: Path to the wordlist file (default: wordlist.txt).
- `-e EXTENSIONS, --extensions EXTENSIONS`: File extensions to search for (comma-separated, e.g., php,html).

Example:

python skdirb.py http://example.com -w wordlist.txt -e php,html

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the MIT License 


