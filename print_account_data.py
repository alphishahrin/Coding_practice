import re
import sys

# def print_data(account_number, datafile):
#     with open(datafile, 'r') as file:
#         for line in file:
            

def main(datafile, account_number):
    flag = False
    with open(datafile, 'r') as file:
        for line in file:
            match = re.match(r'^200.*?~02(\d+)~', line)
            if flag:
                if line.startswith('200'):
                    break
                print(line.strip())
            if line.startswith('200') and match.group(1)==account_number:
                print(f"Account Number {account_number} exist!")
                print()
                flag = True
                print(line.strip())
            

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <datafile> <account_number>")
        sys.exit(1)

    datafile = sys.argv[1]
    account_number = sys.argv[2]
    main(datafile, account_number)
