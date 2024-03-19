import pytest
import os
import app.io.input as data_input
import pandas as pd


@pytest.fixture
def setup_files():
    # Setup: Create necessary files and directories
    with open("./data/test_file.txt", "w") as file:
        file.write("Test")
    with open("./data/empty_file.txt", "w") as file:
        pass
    with open("./data/test_data.csv", "w") as file:
        file.write("Test\nTest\nTest")
    with open("./data/empty_data.csv", "w") as file:
        pass

    yield "./data"

    os.remove("./data/test_file.txt")
    os.remove("./data/empty_file.txt")
    os.remove("./data/test_data.csv")
    os.remove("./data/empty_data.csv")


def test_read_file_python(setup_files):
    result = data_input.read_file_python("test_file.txt")
    expected = "Test"
    assert result == expected


def test_read_file_python_empty(setup_files):
    result = data_input.read_file_python("empty_file.txt")
    expected = ""
    assert result == expected


def test_read_file_python_nonexistent(setup_files):
    with pytest.raises(FileNotFoundError):
        data_input.read_file_python("nonexistent_file.txt")


def test_read_file_pandas(setup_files):
    content = data_input.read_file_pandas("test_data.csv")
    assert list(content.columns) == ["Test"]


def test_read_file_pandas_empty(setup_files):
    with pytest.raises(pd.errors.EmptyDataError):
        data_input.read_file_pandas('empty_data.csv')


def test_read_file_pandas_nonexistent(setup_files):
    with pytest.raises(FileNotFoundError):
        data_input.read_file_pandas("nonexistent_data.csv")