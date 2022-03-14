import json

finput = "lesson7/chapter16/4.5_month.json"
foutput = "lesson7/chapter16/rdb_4.5_month.json"

with open(finput) as f:
    all_data = json.load(f)

with open(foutput, 'w') as f:
    json.dump(all_data, f, indent=4)
