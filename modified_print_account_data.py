# account no gulo ekta map/dictionary te nie nen
# and record 200 theke jei account asbe oita jodi oi dictionary te thake tahole oi customer niben




import re
import sys

def create_account_numbers_dict(account_numbers_file):
    with open(account_numbers_file, 'r') as accounts_file:
        return {int(line.strip()) for line in accounts_file}

def print_data(datafile, account_numbers_dict, output_file):
    with open(datafile, 'r') as file, open(output_file, 'a') as output:
        flag = False
        for line in file:
            match = re.match(r'^200.*~02(\d+)~', line)
            if line.startswith('200') and int(match.group(1)) in account_numbers_dict:
                output.write(f"------------ ACCOUNT NUMBER {match.group(1)} EXISTS! ------------\n")
                output.write(line.strip() + '\n')
                flag = True
            elif flag and line.startswith('200'):
                flag = False
                # break
            elif flag:
                output.write(line.strip() + '\n')

def main(datafile, account_numbers_file, output_file):
    dict_account_number = create_account_numbers_dict(account_numbers_file)
    print(dict_account_number)

    open(output_file, "w").close()

    print_data(datafile, dict_account_number, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <datafile> <account_number_file.txt> <output_file.txt>")
        sys.exit(1)

    datafile = sys.argv[1]
    account_numbers_file = sys.argv[2]
    output_file = sys.argv[3]

    main(datafile, account_numbers_file, output_file)
