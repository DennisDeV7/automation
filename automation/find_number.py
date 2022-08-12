import re


def get_numbers(file_path):
    with open(file_path) as f:
        text_from_file = f.read()

    pattern = r"(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})"
    phone_numbers = re.findall(pattern, text_from_file)

    with open("phone_numbers.txt", "w+") as f:
        for group in sorted(set(phone_numbers)):
            phone_number = '-'.join([group[0], group[2], group[4]])
            f.write(f"{str(phone_number)}\n")

def get_emails(file_path):
    with open(file_path) as f:
        text_from_file = f.read()

    pattern = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+)"
    emails = re.findall(pattern, text_from_file)

    with open("emails.txt", "w+") as f:
        for group in sorted(set(emails)):
            f.write(f"{str(group)}\n")


if __name__ == "__main__":
    get_numbers("assets/potential-contacts.txt")
    get_emails("assets/potential-contacts.txt")