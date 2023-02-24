import os.path
import csv
import re


def main():
    while True:
        try:
            input_file = input("Input file name: ").strip()
            if not os.path.isfile("Files/" + input_file):
                raise FileNotFoundError
            break
        except FileNotFoundError:
            print("File does not exist!")

    output_file = input("Output file name: ").strip()
    while os.path.isfile("Files/" + output_file):
        overwrite = input("Overwrite existing file (y/n): ").strip().lower()
        while overwrite not in ["y", 'n']:
            overwrite = input("Enter (y/n): ").strip().lower()
        if overwrite == "y":
            break
        output_file = input("New output file name: ")

    with open("Files/" + output_file, "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Email", "Subject", "Confidence"])

        with open("Files/input.txt", 'r') as f:

            emails = []
            commit = []
            confidence = []

            check_1 = "From:"
            check_2 = "Subject:"
            check_3 = "X-DSPAM-Confidence:"

            lines = [line.strip() for line in f.readlines()]
            for line in lines:
                if re.match(r"^" + check_1, line):
                    email = line[len(check_1):].strip()
                    emails.append(email)
                if re.match(r"^" + check_2, line):
                    num = re.compile(r"r\d{5}").findall(line)
                    commit.append(num[0].strip())
                if re.match(r"^" + check_3, line):
                    num = re.compile(r"\d\.\d{4}").findall(line)
                    confidence.append(num[0].strip())
        for i in range(len(emails)):
            row = [emails[i], commit[i], confidence[i]]
            csv_writer.writerow(row)
    print("Data stored!")


if __name__ == "__main__":
    main()
