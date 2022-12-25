import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line ='\n') -> list[dict]:
    with open(filename, 'r') as f:
        first_line = f.readline().strip(new_line).split(delimiter)
        json_array = [dict(zip(first_line, row.strip(new_line).split(delimiter))) for row in f]
    return json.dumps(json_array, indent=4)

print(csv_to_list_dict(INPUT_FILE))