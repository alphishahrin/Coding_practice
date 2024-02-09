# anchor regex for example: 200~ , expteced_customer_regex: 550~
# to oisob customer er data nibe jader 550~ record ache ar ki
# and customer 200~ die suru hobe
# meaning customer ki regex die suru hoi eita argument e bole dicchi 
# + kon regex er sathe match hole bujben oi customer ta dorkar eitao argument e bole dicchi




import re
import sys


def print_data(datafile, output_file, anchor_regex, cust_regex):
    with open(datafile, 'r') as file, open(output_file, 'a') as output:
        data_buffer = []
        for line in file:
            if re.match(anchor_regex, line):
                # print("Anchor found\n")
                # print("DATA BUFFER \n", data_buffer)
                if any(re.search(cust_regex, entry) for entry in data_buffer):
                    # print("Regex found\n")
                    output.write("-------------------- Customer Regex matched! --------------------\n")
                    output.write("".join(data_buffer))
                data_buffer = []
            data_buffer.append(line)
            # print("DATA BUFFER \n", data_buffer)
        if any(re.search(cust_regex, entry) for entry in data_buffer):
            # print("Regex found\n")
            output.write("-------------------- Customer Regex matched! --------------------\n")
            output.write("".join(data_buffer))

def main(datafile, output_file, anchor, customer):
    open(output_file, "w").close()

    # print(anchor)
    # print(customer)

    print_data(datafile, output_file, anchor, customer)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python customer_by_anchor.py <input_file> <output_file> <anchor_regex> <exptected_customer_regex>")
        sys.exit(1)

    datafile = sys.argv[1]
    output_file = sys.argv[2]
    anchor_regex = sys.argv[3]
    cust_regex = sys.argv[4]

    main(datafile, output_file, anchor_regex, cust_regex)
