
import json


output = []


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        output.append("BIGBANG")
    elif i % 3 == 0:
        output.append("BIG")
    elif i % 5 == 0:
        output.append("BANG")
    else:
        output.append(str(i))

# 'w' is for write mode which is to create new file or overwrite it
with open('output.json', 'w') as f:
    json.dump(output, f)