import pandas as pd


def read_text_console():
    """
    Converts the text from console into string and returns it

    :return:
        str. The string from console
    """
    return input()


def read_file_python(filename):
    """
    Converts the text from file into string and returns it using python capabilities

    :param filename:
        str. Name of the file to read from

    :return:
        str. The text from the file
    """
    with open(f"./data/{filename}") as file:
        content = file.read()
        return content


def read_file_pandas(filename):
    """
    Converts the text from file into string and returns it using pandas capabilities

    :param filename:
        str. Name of the file to read from

    :return:
        DataFrame. The data from file
    """
    return pd.read_csv(f"./data/{filename}")
