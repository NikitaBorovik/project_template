import app.io.input as data_input
import app.io.output as data_output


def main():
    read_data = [data_input.read_text_console(),
                 data_input.read_file_python("input.csv"),
                 data_input.read_file_pandas("input.csv")]
    for i in range(len(read_data)):
        data_output.write_text_console(read_data[i])
        data_output.write_file_python(str(read_data[i]), f"output{i}.csv")


if __name__ == "__main__":
    main()