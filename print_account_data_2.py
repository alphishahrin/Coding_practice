# account list input hisehbe niben
# meaning arek ta file input niben jeikhane onek gulo account no likha ache
# oi account no gular data arek ta file e write korben instead of print


import re
import sys

def print_data(datafile, account_numbers, output_file):
    with open(datafile, 'r') as file, open(output_file, 'a') as output:
        flag = False
        for line in file:
            match = re.match(r'^200.*~02(\d+)~', line)
            if line.startswith('200') and int(match.group(1))==int(account_numbers):
                output.write(f"------------ ACCOUNT NUMBER {match.group(1)} EXISTS! ------------\n")
                output.write(line.strip() + '\n')
                flag = True
            elif flag and line.startswith('200'):
                flag = False
                break
            elif flag:
                output.write(line.strip() + '\n')


def main(datafile, account_numbers_file, output_file):
    open("output_file.txt", "w").close()

    with open(account_numbers_file, 'r') as accounts_file:
        for line in accounts_file:
            account_numbers = line.strip()
            print_data(datafile, account_numbers, output_file)
        


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <datafile> <account_number_file.txt> <output_file.txt>")
        sys.exit(1)

    datafile = sys.argv[1]
    account_numbers_file = sys.argv[2]
    output_file = sys.argv[3]

    main(datafile, account_numbers_file, output_file)
