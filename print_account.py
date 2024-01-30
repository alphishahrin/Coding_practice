import re
import sys

def find_account_number(line):
    match = re.match(r'^200.*?~02(\d+)~', line)
    if match:
        return match.group(1)
    return None

def main(datafile):
    with open(datafile, 'r') as file:
        for line in file:
            if line.startswith('200'):
                account_number = find_account_number(line)
                if account_number:
                    print(f"Account number: {account_number}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <datafile>")
        sys.exit(1)

    datafile = sys.argv[1]
    main(datafile)
