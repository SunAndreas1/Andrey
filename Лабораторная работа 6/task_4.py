import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line ='\n') -> list[dict]:
    jsonArray = []
    with open(filename, 'r') as f:
        first_line = f.readline().strip(new_line).split(delimiter)
        for row in f:
            jsonArray.append({})
            for i, header in enumerate(first_line):
                jsonArray[-1][header] = row.strip(new_line).split(delimiter)[i]

    return json.dumps(jsonArray, indent=4)

print(csv_to_list_dict(INPUT_FILE))