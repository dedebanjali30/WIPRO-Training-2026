import csv


def read_test_data(file_path):

    with open(file_path, "r", newline="") as file:

        reader = csv.DictReader(file)

        data = list(reader)

    return data


if __name__ == "__main__":

    file_path = "TestData/login_data.csv"

    data = read_test_data(file_path)

    for row in data:

        print("Name:", row["name"])
        print("Email:", row["email"])

    print("CSV test data read successfully")