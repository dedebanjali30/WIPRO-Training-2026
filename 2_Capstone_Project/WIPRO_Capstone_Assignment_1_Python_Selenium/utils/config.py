import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

TEST_DATA_FILE = PROJECT_ROOT / "test_data" / "test_data.json"
CREDENTIALS_FILE = PROJECT_ROOT / "test_data" / "credentials.json"


def load_test_data():

    with open(
        TEST_DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def load_credentials():

    with open(
        CREDENTIALS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)