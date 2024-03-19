import pandas as pd


def write_text_console(output_text):
    """
    Writes text to the console.

    :param output_text:
        str. The text to write to console.
    """
    print(output_text)


def write_file_python(output_text, output_file_name):
    """
    Writes text to the file using python capabilities.

    :param output_text:
        str. The text to write to file.
    :param output_file_name:
        str. Name of the file to write text in.
    """
    with open(f"./data/{output_file_name}", mode="w") as file:
        file.write(output_text)


def write_file_pandas(output_data, output_file_name):
    """
    Writes data to the file using pandas capabilities.

    :param output_data:
        DataFrame. The data to write to file.
    :param output_file_name:
        str. Name of the file to write data in.
    """
    output_data.to_csv(f"./data/{output_file_name}")
