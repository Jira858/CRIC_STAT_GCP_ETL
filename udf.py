import json

def transform(line):
    values = line.split(',')
    # Create a dictionary
    obj = {
        "rank": values[0],
        "name": values[1],
        "country": values[2]
    }
    # Convert to JSON string
    return json.dumps(obj)
