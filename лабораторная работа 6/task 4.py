import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=",", new_line="\n") -> list[dict]:
    slovari = []
    with open(filename) as file:  # TODO реализовать конвертер из csv в json
        file_text = "".join(file.readlines())
        stroki = [stroka.strip().split(delimeter) for stroka in file_text.split(new_line)]

    for data in stroki[1:]:
        slovari.append({stroki[0][i]: data[i] for i in range(len(data))})

    return slovari

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
