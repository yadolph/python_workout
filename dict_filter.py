import json


full_dict = {}

with open('dictionary.json', 'r') as f:
    full_dict = json.load(f)

short_dict = {}
for key, val in full_dict.items():
    if len(key) == 5:
        short_dict[key] = val

short_dict = dict(sorted(short_dict.items()))

with open('short_dictionary.json', 'w') as f:
    json.dump(short_dict, f)
