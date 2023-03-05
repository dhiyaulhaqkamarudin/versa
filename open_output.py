import json

# 'r' is for read mode
with open('output.json', 'r') as f:
    data = json.load(f)

print(data)